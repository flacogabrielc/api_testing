#from urllib import request, response
import json
import requests
import jsonpath

#import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request 
response = requests.get(url)
# # print(response)
#
# # Validate Status Code
# assert response.status_code == 200
#
# # display response content
# print(response.content)
# print(response.headers)

# # Fetch response Header
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))

# # Fetch Cookies
# print(response.cookies)
#
# # Fetch Encoding
# print(response.encoding)
# print(response.elapsed)

json_response = json.loads(response.text)
#print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response,'total_pages')
# data = jsonpath.jsonpath(json_response,'data')
# print(data[0])

for i in range(0,3):
    # data[0].first_name
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))


# first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
# f_name = jsonpath.jsonpath(json_response, 'data[2].first_name')
#
# print((first_name[0]))
# print((f_name[0]))

# tiene que definirse antes para que tome el valor, ejemplo data / total_pages


