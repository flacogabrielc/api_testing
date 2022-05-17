import requests
import json
import jsonpath

# API URl
url = "https://reqres.in/api/users/2"

# Read Input Json File
file = open('CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request with Json Input body
response = requests.put(url, request_json)

# response = requests.post(url, request_json)

# Validating Response Code
assert response.status_code == 200

# Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
