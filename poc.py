import requests

url = 'http://localhost:3000/index.php'
payload = {'username':'grape', 'password':'secret1234'}

response = requests.get(url, data=payload)

print(response.text)