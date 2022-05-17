import jsonpath
import requests
import json
#import assert

# API url
url = "https://reqres.in/api/users"

# Read Imput Json file
file = open('CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# print(request_json)
# Make POST request with Json Input body

response = requests.post(url, request_json)
# print(response.content)

# Validating response code
assert response.status_code ==201, "Es una locura"
#assert False, "es imposible"

print(response.headers.get('Content-Length'))
#print(response.headers)
response_json = json.loads(response.text)

# Pick Id using Jsan Path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
