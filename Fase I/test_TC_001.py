import pytest
import json
import requests

#tener en cuenta que el externalID tiene que estar dado de alta en el idm para poder ejecutar este caso create_user(idm)
#agregar los nuevos casos para el alta completa

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
    response = response.post(url, headers=headersdata, json=data)


def test_tc_019_valid_account():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}


    url = "https://api.qa.clave.cloud/gateway/transfers/accounts?searchString=3220001823000055910025"
    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_020_rank_empr():
    headersdata ={'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url ="https://api.qa.clave.cloud/asset/core/companies-rankings"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_021_pago_serv_s_fac_cc():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}


    url = "https://api.qa.clave.cloud/payment/companies?searchString=Gobierno"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_022_pago_serv_s_fac_mp():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/payment/companies/482/payment-modes"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_023_pago_serv_s_fac_cf():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/payment/bills?companyCode=482&paymentModeId=39030785707000000527&C11=27249286090"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_024_pago_serv_s_fac():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "destinationCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "operationTypeId": 7,
    "performerUser": "marceu",
    "sourceAmount": 77.67,
    "sourceCurrencyId": "ARS",
    "transactionChannelTypeId": "2",
    "params": {
        "companyCode": "482",
        "companyName": "GOBIERNO DE MENDOZA - RENTAS",
        "clientId": "007401180041464561",
        "paymentModeId": "39030785707000000527",
        "barcode": "007401180041464561000000007767265DLC053818020000000000776718117000417",
        "amountType": "ESC",
        "expirationDate": null,
        "reference": null,
        "hash": "1O3x_f-Qbeh4xH8moc1vO58ES0zJs5cLFyDq9kXx9kY",
        "type": "fetchedBill"
        }

    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)
    #response_json = response.json()


def test_tc_025_bar_cod_read():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/payment/bills?barcode=057913405880003353280451910090000017025005"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_026_serv_pay_bar_cod():
    headersdata ={'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
   "sourceCustomerExternalId":"c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
   "destinationCustomerExternalId":"c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
   "operationTypeId":7,
   "performerUser":"marceu",
   "sourceAmount":1702.5,
   "sourceCurrencyId":"ARS",
   "transactionChannelTypeId":"2",
   "params":{
      "companyCode":"3145",
      "companyName":"CRENAC.",
      "clientId":"057913405880003353280451910090000017025005",
      "paymentModeId":"48526074106900000351",
      "barcode":"057913405880003353280451910090000017025005",
      "amountType":"ABI",
      "expirationDate":null,
      "reference":null,
      "hash":"8bbUMR9SprDIEg5jGyM3ZByHb8Hl7QouPK9SXxlpqU8",
      "type":"barcode"
        }
    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_027_comp_rec():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/payment/prepaid/companies"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_028_pay_rec_phone():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "destinationCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "operationTypeId": 10,
    "performerUser": "marceu",
    "sourceAmount": 400.00,
    "sourceCurrencyId": "ARS",
    "transactionChannelTypeId": "2",
    "params": {
        "companyCode": "1488",
        "companyName": "MOVISTAR - RECARGAS DE CELULAR",
        "paymentModeId": "29453037476400000114",
        "form": {
            "IDC": "1156674543",
            "IV1": "400"

        }
    }
}

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)


def test_tc_029_pay_rec_cable():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA','customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7','Content-Type': 'application/json'}

    data = {
    "sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "destinationCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "operationTypeId": 10,
    "performerUser": "marceu",
    "sourceAmount": 500.00,
    "sourceCurrencyId": "ARS",
    "transactionChannelTypeId": "2",
    "params": {
        "companyCode": "1379",
        "companyName": "DIRECTV PREPAGO - RECUPERO DE EQUIPOS 23/07",
        "paymentModeId": "62117071765400000242",
        "form": {
            "BA1": "057000687043877042",
            "IV1": "500"

            }
        }
    }

    url ="https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_030_get_voucher():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/payment/vouchers/111"

    response = response.get(url, headers=headersdata)
    response_json = response.json()


def test_tc_031_alta_cred():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
   "customerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
   "productId": "patriot",
   "vendorId": 896522
    }

    url = "https://api.qa.clave.cloud/credit/requests"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_032_cons_est_cred():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/credit/banners/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_033_cons_card_fis():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/physical_card_ready_by_customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_034_alta_tar_fis():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
   "customerExternalId":"c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
   "street":"Sergio Dembis",
   "streetNumber":"345",
   "floor":"4",
   "apartment":"D",
   "city":"Ciudad de Buenos Aires",
   "neighborhood":"Mataderos",
   "zipCode":"1440"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_035_consulta_tarjeta():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/cards_by_customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_036_pausar_tarjeta():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "cardId": "be8d9a60-0f2b-4ff4-960c-bbe19a77af3f",
    "lastFour": "2740",
    "status": "PAUSED",
    "cardType": "PHYSICAL",
    "startDate": "2022-01-21"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/pause"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_037_act_hab_tar():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA','customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
   "cardId":"be8d9a60-0f2b-4ff4-960c-bbe19a77af3f",
   "lastFour":"4740",
   "status":"ACTIVE",
   "cardType":"PHYSICAL",
   "startDate":"2022-01-21"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/activate"

    response = response.post(url, headers=headersdata, json=data)


def test_tc_038_baj_tarj():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "reason":"LOST"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/disable"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_039_get_sens_data():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/sensitive_data_frame"

    response = response.get(url, headers=headersdata)
    response_json = response.json()

def test_tc_040_get_act_form():
    headersdata = {'apikey:ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/enable_card_frame"

    response = response.get(url, headers=headersdata)
    response_json = response.json()



def test_tc_041_cod_val_send_email():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "to": "marcela@clave.com",
    "type": "EMAIL",
    "client": "CLAVE"

    }

    url = "https://api.qa.clave.cloud/validation/send"

    response = response.post(url, headers=headersdata, json=data)


def test_tc_042_cod_val_send_sms():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "to": "+541154651174",
    "type": "SMS",
    "client": "CLAVE"

    }

    url = "https://api.qa.clave.cloud/validation/send"

    responser = response.post(url, headers=headersdata, json=data)


def test_tc_043_cod_val_validate():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "traceId": "0b6fbf0d-ac0f-4f3b-9c9c-d1678d236c49",
    "code": "884698"

    }

    url = "https://api.qa.clave.cloud/validation/validate"

    response = response.post(url, headers=headersdata, json=data)


def test_tc_044_enr_dat():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7'}

    url = "https://api.qa.clave.cloud/identity-service/v2/person/6503558/N"

    response = response.get(url, headers=headersdata)
    response_json = response.json()



def test_tc_045_get_jwt_token():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': '544c866c-4f36-44c2-aece-b8faafe470eb', 'Content-Type': 'application/json'}

    data = {
    "customerExternalId": "544c866c-4f36-44c2-aece-b8faafe470eb",
    "ip": "127.0.0.1",
    "hash": "e0d123e5f316bef78bfdf5a008837578",
    "deviceData": "Motorola V3 Black"

    }

    url = "https://api.qa.clave.cloud/client/jwt/"

    response = response.post(url, headers=headersdata, json=data)

def test_tc_046_val_extid():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA', 'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
    "externalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
    "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgzMzQ1MzEsImlhdCI6MTY0NzcyOTczMSwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LAHjSzCBrDHPOa30UjOtE6c34o8cmyzVvMj7mlKbSNQ7DxwvohioJeerw0KN0IXRUXl4L1vUgoMz8BlOwI4GKOSBKdCh3SQr8sIFF6scdoEQscQP1uvDAw2Jhi8gIEzKeQPwNrdLeDbPpQ9-oZa2YD33tRsL5uXdZytefYrtGMyp5n5GoN552nRClOR6BhQ4vvqraiyqEpqmWQ3Qm09aJ9W3COArLP86_rM6njhyEshj-HLFNhJCtRhUUeCK5uTFm5xrUv45m-uARQrPSi3P0HXYtnRHHuDpopDCFSosXM5y0g4iaukDsz6LoIB_u7R2atNWF-EBCP_Bgy77-Zpn78KAq0YmL-IHW1oLeaaDB4wTJ8p18mwduACPNpAgIIBk0NsWoYX9YGJyX8cWExQuchRMJGknkFJkJFwgQ_I2e5CA3iPa--3cpkpwT2Mn62c9BStKEd7faw52WO7ghGDIMSbAkYrAmJswmyAp_Kb0LlrqlhoX6xBChQN3OgVYa3YvAePC1mPCp7Tf4vfeKPWdgJ6btJ0kSP5iNzaiug_C8TAXo7-BIBM64Sjojo4yVqR0ZftVIbBksJFIOrQRV9Bwg23ohvEyJui2H5MvW_2FoJy1FLiPWDwrqv4ckM8DgE0UGOJUojELKEuxXrlY_gh4ad5gGPxxz2IRQNOpTMNd6Yc"
    }

    url = "https://api.qa.clave.cloud/client/jwt/validate"

    response = response.post(url, headers=headersdata, json=data)