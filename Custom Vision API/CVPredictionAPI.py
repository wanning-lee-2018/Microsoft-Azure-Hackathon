import requests
import os


url = "" # INSERT CUSTOM VISION PREDICTION API URL 

payload = "{\n    \"Url\": \"https://vision.eng.au.dk/wp-content/uploads/2017/11/47-150x150.png\"\n}"   
headers = {
	'Content-Type': 'application/json',
	'Prediction-Key': ''  #INSERT PREDICTION KEY
}

response = requests.request("POST", url, headers=headers, data = payload)
results=response.json()
probs={}
for pred in results['predictions']:
    probs[pred["tagName"]]=pred["probability"]
print(max(probs,key=probs.get)) #PRINT PREDICTED RESULT OF THE HIGHEST PROBABILITY







