import requests

url="https://potted-cv-1.cognitiveservices.azure.com/customvision/v3.0/Prediction/7308f98a-e5c4-4d9d-9f3e-7be4cc604a0b/classify/iterations/Potted-CV%20model/url"

headers={
    "Prediction-Key":"d11988b68aff44689442d2995dd4912f",
    "Content-Type":"application/json"}



#imagepath="D:/potted-iot/iot-hub/Quickstarts/simulated-device-2/undp_seedlings_dataset/testing_data/Fat Hen/382.png"
#data= open(imagepath,'rb').read()
imageurl="https://static.backyardfruit.com/images/products/key-lime-tree-2.jpg"
data={"Url":imageurl}
response=requests.post(url,headers=headers,data=data)
response=response.json()
print(response)



