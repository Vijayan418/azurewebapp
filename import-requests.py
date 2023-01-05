import requests

url1 = 'https://vjwebapp1234.azurewebsites.net/api/calculator'

data = {
    "num1": 45,
    "num2": 1455,
    "operation": "multiply"
}

params1= {
    "num1": 45,
    "num2": 1455,
    "operation": "multiply"
}

response = requests.post(url=url1, json=data)
#response = requests.post(url=url1, params=params1)

print(response.json())
#print(response.url)
