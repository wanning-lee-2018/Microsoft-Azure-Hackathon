# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time
import threading
import requests
import json


# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

#help(IoTHubDeviceClient)

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = ""  #INSERT CONNECTION STRING

#Simulating the results from the Custom Vision Prediction API

def PostCVPrediction(image_url):
    url = "" #INSERT CUSTOM VISION PREDICTION API URL
    headers = {
	    'Content-Type': 'application/json',
	    'Prediction-Key': ''} #INSERT PREDICTION KEY FOR CUSTOM VISION PREDICTION API 
    response = requests.request("POST", url, headers=headers, data = image_url)
    results=response.json()
    probs={}
    for pred in results['predictions']:
        probs[pred["tagName"]]=pred["probability"]
    output=max(probs,key=probs.get)
    if output=="Shepherd's Purse":
		HasWeed=1
    else:
		HasWeed=0
    return  HasWeed
#Simulating the inputs to the Custom Vision Prediction API
image_urls = {1:"{\n    \"Url\": \"https://vision.eng.au.dk/wp-content/uploads/2017/11/47-150x150.png\"\n}",0:"{\n    \"Url\": \"https://vision.eng.au.dk/wp-content/uploads/2017/11/391.png\"\n}"}


def PostMLPrediction(data_input):
    # URL for the web service
    scoring_uri = ''  #INSERT URL FOR THE AZURE MACHINE LEARNING WEB SERVICE
    # If the service is authenticated, set the key or token
    key = '' #INSERT THE KEY WITH IT IS SET 
    data = {"data":[data_input]
        }
    # Convert to JSON string
    input_data = json.dumps(data)
    # Set the content type
    # If authentication is enabled, set the authorization header
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}
    # Make the request and display the response
    resp = requests.post(scoring_uri, input_data, headers=headers)
    #print(type(resp))   <class 'requests.models.Response'>
    #converts response object  to a JSON object of the result(which is a string)
    result=(resp.json())
    #print(result)     #{"result": [0]}
    #print(result["result"][0])
    ##print(type(result))   <type 'unicode'>
    # #  json. loads() takes in a string and returns a json object.
    result2=json.loads(result)
    #print(result2)
    #print(type(result2))   #<type 'dict'>
    #print(result2["result"][0])
    IsHealthy=result2["result"][0]
    return IsHealthy


INTERVAL = 1

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client


def device_method_listener(device_client):
    global INTERVAL
    while True:
        method_request = device_client.receive_method_request()
        print (
            "\nMethod callback called with:\nmethodName = {method_name}\npayload = {payload}".format(
                method_name=method_request.name,
                payload=method_request.payload
            )
        )
        if method_request.name == "SetTelemetryInterval":
            try:
                INTERVAL = int(method_request.payload)
            except ValueError:
                response_payload = {"Response": "Invalid parameter"}
                response_status = 400
            else:
                response_payload = {"Response": "Executed direct method {}".format(method_request.name)}
                response_status = 200
        else:
            response_payload = {"Response": "Direct method {} not defined".format(method_request.name)}
            response_status = 404

        method_response = MethodResponse(method_request.request_id, response_status, payload=response_payload)
        device_client.send_method_response(method_response)


MSG_TXT = '{{"temperature(C)": {temperature},"humidity(%)": {humidity},"pH Level":{ph},"sunlight(lux)":{sunlight},"soil_moisture(%)":{moisture},"HasWeed":{HasWeed},"IsHealhty":{IsHealthy}}}'

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        # Start a thread to listen 
        device_method_thread = threading.Thread(target=device_method_listener, args=(client,))
        device_method_thread.daemon = True
        device_method_thread.start()

        while True:
            # Build the message with simulated telemetry values.
            temperature = random.randint(23,36) + random.random()
            humidity = random.randint(40,85) + random.random()
            ph= random.randint(4,7) + random.random()
            sunlight = random.randint(15000,49999) + random.random()
            moisture = random.randint(35,99) + random.random()
            image_url=image_urls[random.randint(0,1)]
            HasWeed=PostCVPrediction(image_url)
            data_input={'pH Level':ph,'Temperature(C)':temperature,
                'Soil Moisture(%)':moisture,'Humidity(%)':humidity,'Sunlight(lux)':sunlight,'HasWeed':HasWeed}
            IsHealthy=PostMLPrediction(data_input)
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity,ph=ph,sunlight=sunlight, moisture=moisture,HasWeed=HasWeed,IsHealthy=IsHealthy)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print( "Message sent" )
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #2 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()