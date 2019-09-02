import requests
import json

url = 'http://localhost:5000/predict'


data = {'features': [[25,1,0,2 ]]} #Femme de 25 ans en seconde classe

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text) 