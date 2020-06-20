import requests
import json

# URL for the web service
scoring_uri = 'http://2e9d90fc-4fa6-4788-9343-8f589bb9b28a.southeastasia.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'PYEtDWhPY5qYhHsBAKY04ls5kUasdLeU'

# 1 set of data to score, so we get 1 result back
# data = {"data":
#             [
# [50.0,40000.0,9,25.0,50.00,0]
# ]
#         }


#another method
data = {"data":[
            
                {'pH':4.113643355,'Temperature':26.45361526,
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
# #  json. loads() takes in a string and returns a json object.
result2=json.loads(result)
print(result2["result"][0])

#print(input_data)


