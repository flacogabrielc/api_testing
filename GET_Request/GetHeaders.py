import requests
headerdata={}
response = requests.get('https://httpbin.org/get')
print(response.text)
