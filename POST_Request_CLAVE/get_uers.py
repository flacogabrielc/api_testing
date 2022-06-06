import requests

headersdata = {'Authorization':'Bearer CxYDpEomtDPYMfYk5ysVVDWRNkswip9Y','X-Caller-Id':'CLAR','Content-Type':'application/json'}
#data is the body
data = {
    "organization_id": "CLAVE_ARG",
    "page": 1,
}

# API URL
url = "https://idm.qa.clave.cloud/api/get_users"

response = requests.post(url, headers=headersdata, json = data  )
print(response.text)

# flacogabreielc
#git config --global user.name "flacogabrielc"
# #git config --global user.email "flacogabrielc@hotmail.com"
#ssh-keygen -t rsa -b 4096 -C "flacogabrielc@hotmail.com"
#git config --global user.email flacogabrielc@hotmail.com
