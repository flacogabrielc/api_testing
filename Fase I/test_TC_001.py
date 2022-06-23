import pytest
import json
import requests

#tener en cuenta que el externalID tiene que estar dado de alta en el idm para poder ejecutar este caso create_user(idm)
def test_tc_001_alta_cliente():
    headersdata = {'Content-Type': 'application/json', 'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE'}

    # data is the body
    data = {"externalId": "544c866c-4f36-44c2-aece-b8faafe470eb"

    }

    url = "https://api.qa.clave.cloud/gateway/customers"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()
    print(response_json)

def test_tc_002_cons_pro_alta():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'customerExternalId': '544c866c-4f36-44c2-aece-b8faafe470eu'}


    url = "https://api.qa.clave.cloud/gateway/processes/57795e69-5369-404c-90d9-669475928e65"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

#def test_tc_003_cons_cliente():
