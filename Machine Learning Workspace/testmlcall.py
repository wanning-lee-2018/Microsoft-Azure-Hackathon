import requests
import json

# URL for the web service
scoring_uri = 'http://b620d5b4-8c60-4f5f-adaf-701e32b1e093.southeastasia.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'I9ehNbxEK7Z1lsKv6S7dcSG7FP6FY1i3'

# 1 set of data to score, so we get 1 result back
# data = {"data":
#             [
# [50.0,40000.0,9,25.0,50.00,0]
# ]
#         }


#another method
data = {"data":[
            
                {'pH Level':4.113643355,'Temperature(C)':26.45361526,
                'Soil Moisture(%)':46.99867094,'Humidity(%)':47.81398495,'Sunlight(lux)':45977.40904,'HasWeed':1.0}
            ]
        }

# Convert to JSON string
input_data = json.dumps(data)

# Set the content type
#headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
#headers['Authorization'] = f'Bearer {key}'
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
print(result2["result"][0])

#print(input_data)



