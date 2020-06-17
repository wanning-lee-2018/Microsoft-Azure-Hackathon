import requests
import json

# URL for the web service
scoring_uri = 'http://2e9d90fc-4fa6-4788-9343-8f589bb9b28a.southeastasia.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'PYEtDWhPY5qYhHsBAKY04ls5kUasdLeU'

# Two sets of data to score, so we get two results back
data = {"data":
        [
            [50.0,40000.0,9,25.0,50.00,0],
            [6,25.0,50.0,50.0,40000.0,0]
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
print(resp.text)


 