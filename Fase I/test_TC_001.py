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
    #tener en cuenta que lo que se envia luego del processes es el encode ky
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'customerExternalId': '544c866c-4f36-44c2-aece-b8faafe470eu'}


    url = "https://api.qa.clave.cloud/gateway/processes/57795e69-5369-404c-90d9-669475928e65"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_003_cons_cliente():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/core/customer?externalId=c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"
    response = requests.get(url, headers=headersdata)
    response_json = response.json()


def test_tc_004_gen_cupon_dep():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "customerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "type": "DEPOSIT",
    "transactionChannelTypeId": 2,
    "currencyCode": "ARS"}

    url = "https://api.qa.clave.cloud/gateway/vouchers"
    response = requests.post(url, headers=headersdata, json=data)

def test_tc_005_gen_cupon_ret():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "customerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "type": "WITHDRAWAL",
    "transactionChannelTypeId": 2,
    "currencyCode": "ARS"
        }

    url = "https://api.qa.clave.cloud/gateway/vouchers"
    response = requests.post(url, headers=headersdata, json=data)

def test_tc_006_consultar_saldos():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7' }

    url = "https://api.qa.clave.cloud/core/customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7/balances"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_007_consultar_sdo_token():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url ="https://api.qa.clave.cloud/investors/v1/balance/3cc05f7a-9f19-11ec-b909-0242ac120002"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_008_cons_op_enr_customer():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/core/operation/enrichment_by_customer/3cc05f7a-9f19-11ec-b909-0242ac120002"


    response = requests.get(url, headers=headersdata)
    response_json = response.json()


def test_tc_009_cons_op_por_op():

    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url ="https://api.qa.clave.cloud/core/operation/118"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_010_cons_por_cust():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/core/operation/find_by_customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_011_cons_op_frec():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/core/operation/frequent_by_customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = response.get(url, headers=headersdata)
    response_json = requests.json()

def test_tc_012_cons_cont_frec():
    headearsdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7' }

    url = "https://api.qa.clave.cloud/asset/customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7/frequent_addresses"

    response = response.get(url, headers=headearsdata)
    response_json = requests.json()

def test_tc_013_cons_bancos():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/asset/banks"

    response = response.get(url, headers=headersdata)
    response_json = requests.json()

def test_tc_014_cons_suc():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https: // api.qa.clave.cloud / asset / branches?latitude = -34.601786078086576 & longitude = -58.4095409673291"

    response = response.get(url, headers=headersdata)
    response_json = requests.json()

def test_tc_015_env_din():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {"sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "destinationCustomerExternalId" : "97b71fc4-6214-e7a0-9921-b75da1e72574",
    "operationTypeId" : 5,
    "performerUser" : "marceu",
    "sourceAmount" : 2,
    "sourceCurrencyId" : "ARS",
    "destinationAmount" : 2,
    "destinationCurrencyId" : "ARS",
    "transactionChannelTypeId" : 1,
    "params" : {

    }
}

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)
    #response_json = requests.json()

def test_tc_016_agendar_cuent_to_trans():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "owner": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "accountType": "Caja de ahorro en pesos",
    "accountNumber": "8393/37",
    "cbu": "0000000000000000000001",
    "alias": "evampiros.vilma.palma.",
    "bankName": "Galicia",
    "remitter": "Juan Martin",
    "referenceCode": "AB8965"

    }

    url = "https://api.qa.clave.cloud/asset/banksbook"

    response = response.post(url, headers=headersdata, json=data)
    #response_json = requests.json()

def test_tc_017_cons_ag_cuen_transf():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', '"jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/asset/banksbook?externalId=c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = response.get(ur, headers=headersdata)
    response_json = response.json()

def test_tc_018_ret_por_trans():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type' :'application/json'}

    data = {"sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "destinationCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "operationTypeId": 4,
    "performerUser": "marceu",
    "sourceAmount": 5.12,
    "sourceCurrencyId": "ARS",
    "transactionChannelTypeId": 4,
    "params": {
        "destinationBankAccountAlias": "MITO.FILA.OJOTA"
        }

    }

    url = "https://api.qa.clave.cloud/core/operation"




