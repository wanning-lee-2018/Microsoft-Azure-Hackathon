import requests
import os
#==ORIGINAL ONE I DID IN VSC DIRECTLY BUT IT DIDNT WORK OUT==#

# url="https://potted-cv-1.cognitiveservices.azure.com/customvision/v3.0/Prediction/7308f98a-e5c4-4d9d-9f3e-7be4cc604a0b/classify/iterations/Potted-CV%20model/url"

# headers={
#     "Content-Type":"application/json",
#     "Prediction-Key":"d11988b68aff44689442d2995dd4912f"
#     }
# image_url="https://vision.eng.au.dk/wp-content/uploads/2017/11/47-150x150.png"
# body={"Url":image_url}
# response=requests.post(url,data=body,headers=headers)
# result=response.json()
# print(result)
#--------------------------------------------------------------------------------------------
#==UPDATED ONE THAT I ORIGINALLY DID ON POSTMAN AND I COPIED AND PASTED THE CODE INTO VSC,made some minor changes  AND IT WORK==#

# url = "https://potted-cv-1.cognitiveservices.azure.com/customvision/v3.0/Prediction/7308f98a-e5c4-4d9d-9f3e-7be4cc604a0b/classify/iterations/Potted-CV%20model/url"

# payload = "{\n    \"Url\": \"https://vision.eng.au.dk/wp-content/uploads/2017/11/47-150x150.png\"\n}"
# headers = {
# 	'Content-Type': 'application/json',
# 	'Prediction-Key': 'd11988b68aff44689442d2995dd4912f'
#     #,'Content-Type': 'text/plain'   ==REMOVED THIS LINE CUZ THIS THROWS OUT ERROR==
# }

# response = requests.request("POST", url, headers=headers, data = payload)
# #results=response.text.encode('utf8')  ====REMOVED THIS LINE CUZ IT WONT WORK===
# results=response.json()
# probs={}
# for pred in results['predictions']:
#     probs[pred["tagName"]]=pred["probability"]
# print(max(probs,key=probs.get))

#------------------------------------------------------------------------------------------------------
#==trying withlocal image file, it works in postman but doesnt work here.... still trying to figure out why#==

# # #imagepath="D:\Microsoft Azure Hackathon\potted-iot\iot-hub\Quickstarts\simulated-device-2\undp_seedlings_dataset\testing_data\Maize\184.png"
# # #data= open(imagepath,'rb').read()
url = "https://potted-cv-1.cognitiveservices.azure.com/customvision/v3.0/Prediction/7308f98a-e5c4-4d9d-9f3e-7be4cc604a0b/classify/iterations/Potted-CV%20model/image"

#payload = {}
files =[
	({'' :open('undp_seedlings_dataset/testing_data/Maize/184.png','rb')}, 'multipart/form-data')
]

headers = {
	'Content-Type': 'application/octet-stream',
	'Prediction-Key': 'd11988b68aff44689442d2995dd4912f'
}
response = requests.request("POST", url,headers=headers, files = files)

#print(response.text.encode('utf8'))   #====REMOVED THIS LINE CUZ IT WONT WORK===

results=response.json()
print(results)
#probs={}
# for pred in results['predictions']:
#     probs[pred["tagName"]]=pred["probability"]
# print(max(probs,key=probs.get))






