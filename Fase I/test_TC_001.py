import pytest
import json
import requests
import random


# ver como agregar una validacion que cuando el assert no es correcto imprima lo que devuelve
# execute like pytest -s -v test_TC_Pruebas.py
# with marks pytest -s -v -m Smoke test_TC_Pruebas.py
# asserts
# marks
# ejecucion agrupacion
# tener en cuenta que el externalID tiene que estar dado de alta en el -  idm para poder ejecutar este caso create_user(idm)
# agregar los nuevos casos para el alta completa


userID = '19fc2657-85f4-c3fa-f74d-cf37e12e5db9'


def obtener_jwt():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": userID,
        "ip": "127.0.0.1",
        "hash": "e0d123e5f316bef78bfdf5a008837578",
        "deviceData": "Iphone"

    }

    url = "https://api.qa.clave.cloud/client/jwt/"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()
    return response_json['jwt']

#@pytest.mark.Gabo
def test_tc_001_alta_cliente():
    headersdata = {'Content-Type': 'application/json', 'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE'}

    # data is the body
    data = {"externalId": "544c866c-4f36-44c2-aece-b8faafe470eb"

            }

    url = "https://api.qa.clave.cloud/gateway/customers"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()
    print(response_json)

#@pytest.mark.Gabo
def test_tc_002_cons_pro_alta():
    # tener en cuenta que lo que se envia luego del processes es el encode ky
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'customerExternalId': '544c866c-4f36-44c2-aece-b8faafe470eu'}

    url = "https://api.qa.clave.cloud/gateway/processes/57795e69-5369-404c-90d9-669475928e65"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

@pytest.mark.Smoke
def test_tc_003_cons_cliente():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/core/customer?externalId=19fc2657-85f4-c3fa-f74d-cf37e12e5db9"
    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

@pytest.mark.Smoke
def test_tc_004_gen_cupon_dep():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": userID,
        "type": "DEPOSIT",
        "transactionChannelTypeId": 2,
        "currencyCode": "ARS"}

    url = "https://api.qa.clave.cloud/gateway/vouchers"
    response = requests.post(url, headers=headersdata, json=data)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

@pytest.mark.Smoke
def test_tc_005_gen_cupon_ret():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": userID,
        "type": "WITHDRAWAL",
        "transactionChannelTypeId": 2,
        "currencyCode": "ARS"
    }

    url = "https://api.qa.clave.cloud/gateway/vouchers"
    response = requests.post(url, headers=headersdata, json=data)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


@pytest.mark.Smoke
def test_tc_006_consultar_saldos():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    # url = "https://api.qa.clave.cloud/core/customer/'userID'/balances"
    url = f'https://api.qa.clave.cloud/core/customer/{userID}/balances'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

@pytest.mark.Smoke
def test_tc_007_consultar_sdo_token():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/investors/v1/balance/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

    assert response.status_code == 200
    # assert response.headers["Content-Type"] == "application/json"

@pytest.mark.Smoke
def test_tc_008_cons_op_enr_customer():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/core/operation/enrichment_by_customer/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_009_cons_op_por_op():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/core/operation/18"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200
    # buscar por id de operacion "operation" se puede validar por varias.

@pytest.mark.Smoke
def test_tc_010_cons_por_cust():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/core/operation/find_by_customer/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_011_cons_op_frec():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/core/operation/frequent_by_customer/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_012_cons_cont_frec():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/asset/customer/{userID}/frequent_addresses'

    # url = f'https://api.qa.clave.cloud/core/operation/frequent_by_customer/{userID}'
    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_013_cons_bancos():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/asset/banks"
    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_014_cons_suc():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/asset/branches?latitude=-34.601786078086576&longitude=-58.4095409673291"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_015_env_din():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {"sourceCustomerExternalId": userID,
            "destinationCustomerExternalId": '69bf92ce-8619-dccd-1c83-66d49d04faee',
            "operationTypeId": 5,
            "performerUser": "marceu",
            "sourceAmount": 200,
            "sourceCurrencyId": "ARS",
            "destinationAmount": 200,
            "destinationCurrencyId": "ARS",
            "transactionChannelTypeId": 1,
            "params": {

            }
            }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

    # response_json = requests.json()


# tener en cuenta que el cbu debe cambiar en cada corrida
@pytest.mark.Gabo
def test_tc_016_agendar_cuent_to_trans():
    jotaw = obtener_jwt()
    cebeu = random.randint(1000000000000000000001, 9999999999999999999999)

    # agregar un random al cbu
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "owner": "69bf92ce-8619-dccd-1c83-66d49d04faee",
        "accountType": "Caja de ahorro en pesos",
        "accountNumber": "8393/37",
        "cbu": cebeu,
        "alias": "evampiros.vilma.palma.",
        "bankName": "Galicia",
        "remitter": "Juan Martin",
        "referenceCode": "AB8965"

    }

    url = "https://api.qa.clave.cloud/asset/banksbook"

    response = requests.post(url, headers=headersdata, json=data)
    # response_json = requests.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_017_cons_ag_cuen_transf():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f"https://api.qa.clave.cloud/asset/banksbook?externalId={userID}"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_018_ret_por_trans():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

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
    response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_019_valid_account():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/gateway/transfers/accounts?searchString=3220001823000055910025"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_020_rank_empr():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/asset/core/companies-rankings"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_021_pago_serv_s_fac_cc():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/companies?searchString=Gobierno"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200
    #por ahora usamos este porque no tiene referencia alguna

@pytest.mark.Smoke
def test_tc_022_pago_serv_s_fac_mp():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/companies/482/payment-modes"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_023_pago_serv_s_fac_cf():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/bills?companyCode=482&paymentModeId=39030785707000000527&C11=27249286090"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_024_pago_serv_s_fac():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

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
    # response_json = response.json()

@pytest.mark.Smoke
def test_tc_025_bar_cod_read():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/bills?barcode=057913405880003353280451910090000017025005"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_026_serv_pay_bar_cod():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "sourceCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
        "destinationCustomerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
        "operationTypeId": 7,
        "performerUser": "marceu",
        "sourceAmount": 1702.5,
        "sourceCurrencyId": "ARS",
        "transactionChannelTypeId": "2",
        "params": {
            "companyCode": "3145",
            "companyName": "CRENAC.",
            "clientId": "057913405880003353280451910090000017025005",
            "paymentModeId": "48526074106900000351",
            "barcode": "057913405880003353280451910090000017025005",
            "amountType": "ABI",
            "expirationDate": null,
            "reference": null,
            "hash": "8bbUMR9SprDIEg5jGyM3ZByHb8Hl7QouPK9SXxlpqU8",
            "type": "barcode"
        }
    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_027_comp_rec():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/prepaid/companies"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_028_pay_rec_phone():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

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

#@pytest.mark.Gabo
def test_tc_029_pay_rec_cable():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

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

    url = "https://api.qa.clave.cloud/core/operation"

    response = response.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_030_get_voucher():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/payment/vouchers/111"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_031_alta_cred():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
        "productId": "patriot",
        "vendorId": 896522
    }

    url = "https://api.qa.clave.cloud/credit/requests"

    response = response.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_032_cons_est_cred():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/credit/banners/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_033_cons_card_fis():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/cards/physical_card_ready_by_customer/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_034_alta_tar_fis():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
        "street": "Sergio Dembis",
        "streetNumber": "345",
        "floor": "4",
        "apartment": "D",
        "city": "Ciudad de Buenos Aires",
        "neighborhood": "Mataderos",
        "zipCode": "1440"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards"

    response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_035_consulta_tarjeta():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://api.qa.clave.cloud/cards/cards_by_customer/{userID}'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_036_pausar_tarjeta():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "cardId": "be8d9a60-0f2b-4ff4-960c-bbe19a77af3f",
        "lastFour": "2740",
        "status": "PAUSED",
        "cardType": "PHYSICAL",
        "startDate": "2022-01-21"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/pause"

    response = response.post(url, headers=headersdata, json=data)

#@pytest.mark.Gabo
def test_tc_037_act_hab_tar():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "cardId": "be8d9a60-0f2b-4ff4-960c-bbe19a77af3f",
        "lastFour": "4740",
        "status": "ACTIVE",
        "cardType": "PHYSICAL",
        "startDate": "2022-01-21"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/activate"

    response = response.post(url, headers=headersdata, json=data)

#@pytest.mark.Gabo
def test_tc_038_baj_tarj():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "reason": "LOST"
    }

    url = "https://api.qa.clave.cloud/gateway/mocks/cards/be8d9a60-0f2b-4ff4-960c-bbe19a77af3f/disable"

    response = response.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_039_get_sens_data():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = f'https://cards-api.qa.clave.cloud/cards/crd-27WRwapwZmGtohmNSTx9X0lOpcS/sensitive_data_frame'

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_040_get_act_form():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/cards/crd-27WRwapwZmGtohmNSTx9X0lOpcS/enable_card_frame"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 400

#@pytest.mark.Gabo
def test_tc_041_cod_val_send_email():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "to": "marcela@clave.com",
        "type": "EMAIL",
        "client": "CLAVE"

    }

    url = "https://api.qa.clave.cloud/validation/send"

    response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_042_cod_val_send_sms():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "to": "+541131099717",
        "type": "SMS",
        "client": "CLAVE"

    }

    url = "https://api.qa.clave.cloud/validation/send"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_043_cod_val_validate():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "traceId": "0b6fbf0d-ac0f-4f3b-9c9c-d1678d236c49",
        "code": "884698"

    }

    url = "https://api.qa.clave.cloud/validation/validate"

    response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_044_enr_dat():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE'}

    url = "https://api.qa.clave.cloud/identity-service/v2/person/6503558/N"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_045_get_jwt_token():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': '544c866c-4f36-44c2-aece-b8faafe470eb', 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": "544c866c-4f36-44c2-aece-b8faafe470eb",
        "ip": "127.0.0.1",
        "hash": "e0d123e5f316bef78bfdf5a008837578",
        "deviceData": "Motorola V3 Black"

    }

    url = "https://api.qa.clave.cloud/client/jwt/"

    response = requests.post(url, headers=headersdata, json=data)

#@pytest.mark.Gabo
def test_tc_046_val_extid():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgyMzU5NTIsImlhdCI6MTY0NzYzMTE1MiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LgSn30QPhkPhUjMSGLPYr8sksbM7QcGuyAe-egsqLdFuj32rd_BIJbsLlW8zaP8XEpmsaAu2_gc-vVjIQf5CgOvI8DnpUY_-q17gfBYONy0RJmiGIMIUgqjOjhEMLN75MDc-ETziCIEpn9D8YjkDl9J5DX5KHYWNbeSbvURhvAGADl8aWvvunHgVjOYeWd7luyYbjZQ7I_K2_V0UwLv45MScWHG-dIzYnUJDdNXtvkjgpZEnq9iwzkmb1Lb886FTpqA9jSQyKE4QO-LBvvDf121yhhPrj9ualBU8pd0tMBpp4IcvG0So312HWnUpyFW9tFFZ_kFdTX76JTQBPkph6UT81k1kJ6jFutMmJDJ7A5aITTFpxK8yi8-8_95tGOS2HxXRwa36A6bm-lZlx1vTEgFTaqd9RJcD3Bbori1TN1-d3R-Q2HcILLYHULQVVG2A0-oGP5X3042Dqta0Zk_2RauCNZ8aEfzo5HLvfSSjQgqiO4cSJpb0UXTfACWSD7-6zAJD-C249YEdteKrtytDItHwzQelNZAjmutaNjbKkAiHjEjkjghLSt8_PJWOJoM5NWVv_lt0JG_rYuKAF2wKNSm54bDCMO6GrCiMrbozqaTHA7JvUCzylNEjTBbXxzOoiQlQ0h7zyMJjkl6LPHtZGxqPnDETCNjL39poaCm35tA',
                   'customerExternalId': 'c27ed8c7-ed0e-4c7e-826e-a8e345190aa7', 'Content-Type': 'application/json'}

    data = {
        "externalId": "c27ed8c7-ed0e-4c7e-826e-a8e345190aa7",
        "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDgzMzQ1MzEsImlhdCI6MTY0NzcyOTczMSwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiYzI3ZWQ4YzctZWQwZS00YzdlLTgyNmUtYThlMzQ1MTkwYWE3fEFSRyJ9.LAHjSzCBrDHPOa30UjOtE6c34o8cmyzVvMj7mlKbSNQ7DxwvohioJeerw0KN0IXRUXl4L1vUgoMz8BlOwI4GKOSBKdCh3SQr8sIFF6scdoEQscQP1uvDAw2Jhi8gIEzKeQPwNrdLeDbPpQ9-oZa2YD33tRsL5uXdZytefYrtGMyp5n5GoN552nRClOR6BhQ4vvqraiyqEpqmWQ3Qm09aJ9W3COArLP86_rM6njhyEshj-HLFNhJCtRhUUeCK5uTFm5xrUv45m-uARQrPSi3P0HXYtnRHHuDpopDCFSosXM5y0g4iaukDsz6LoIB_u7R2atNWF-EBCP_Bgy77-Zpn78KAq0YmL-IHW1oLeaaDB4wTJ8p18mwduACPNpAgIIBk0NsWoYX9YGJyX8cWExQuchRMJGknkFJkJFwgQ_I2e5CA3iPa--3cpkpwT2Mn62c9BStKEd7faw52WO7ghGDIMSbAkYrAmJswmyAp_Kb0LlrqlhoX6xBChQN3OgVYa3YvAePC1mPCp7Tf4vfeKPWdgJ6btJ0kSP5iNzaiug_C8TAXo7-BIBM64Sjojo4yVqR0ZftVIbBksJFIOrQRV9Bwg23ohvEyJui2H5MvW_2FoJy1FLiPWDwrqv4ckM8DgE0UGOJUojELKEuxXrlY_gh4ad5gGPxxz2IRQNOpTMNd6Yc"
    }

    url = "https://api.qa.clave.cloud/client/jwt/validate"

    response = requests.post(url, headers=headersdata, json=data)


#reversas
#card 104 105 106 107 108 112

#104 reversa extracash
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-11" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444959" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-200kXoaEJLNzcsvNxY1pmBO7GGJ",
# "country_code": "ARG",
# "type": "EXTRACASH",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time": "2022-07-07T12:45:00",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "ABC123TESTMTF19",
# "mcc": "5999",
# "address": null,
# "name": "Misc Retail"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 1350.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 135000000.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 150.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "EXTRACASH",
# "currency": "ARS",
# "amount": 500.0,
# "name": "EXTRACASH"
# },
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 13000.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'

#105 Reversa compras
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "x-apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-53" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444959" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-27WnxhnJ8787hV1XvLib316",
# "country_code": "ARG",
# "type": "PURCHASE",
# "point_type": "ECOMMERCE",
# "entry_mode": "MANUAL",
# "origin": "DOMESTIC",
# "local_date_time" : "2022-04-08T19:09:16",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "111111111111111",
# "mcc": "5045",
# "address": null,
# "name": "Computer Software"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 10.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 990.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 11.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 990.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'

#106 reversa extraccion
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "x-apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-66" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444961" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-test-withdrawal-017",
# "country_code": "ARG",
# "type": "WITHDRAWAL",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time" : "2022-07-07T12:45:00",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "ID-Code06      ",
# "mcc": "6011",
# "address": null,
# "name": "Automated Cash Disb"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 200.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 10000.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 8.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 1000000000.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'

#107 REversa refound
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:https://pomelo-adapter.qa.clave.cloud/transactions/adjustments/debit" \
#    -H "x-idempotency-key:test-idempotency-key-13" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444963" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-200kXoaEJLNzcsvNxY1pmBO7136",
# "country_code": "ARG",
# "type": "REVERSAL_REFUND",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time": "2022-04-05T12:45:00",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "ABC123TESTMTF19",
# "mcc": "5999",
# "address": null,
# "name": "Misc Retail"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 1000.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 135000000.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 150.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "REVERSAL_REFUND",
# "currency": "ARS",
# "amount": 500.0,
# "name": "REVERSAL_REFUND"
# },
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 13000.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/adjustments/debit'

#108 reversa de payment
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:https://pomelo-adapter.qa.clave.cloud/transactions/adjustments/debit" \
#    -H "x-idempotency-key:test-idempotency-key-11" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444960" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-200kXoaEJLNzcsvNxY1pmBO7141",
# "country_code": "ARG",
# "type": "REVERSAL_PAYMENT",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time": "2022-04-05T12:45:00",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "ABC123TESTMTF19",
# "mcc": "5999",
# "address": null,
# "name": "Misc Retail"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 1000.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 135000000.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 150.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "REVERSAL_PAYMENT",
# "currency": "ARS",
# "amount": 500.0,
# "name": "REVERSAL_PAYMENT"
# },
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 13000.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/adjustments/debit'

#112 transaccion inexistente
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:https://pomelo-adapter.qa.clave.cloud/cards//transactions/adjustments/credit" \
#    -H "x-idempotency-key:1234514" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444961" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-200kXoaEJLNzcsvNxY1pmBO7128",
# "country_code": "ARG",
# "type": "REVERSAL_EXTRACASH",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time": "2022-07-07T12:45:00",
# "original_transaction_id": "dtx-200kXoaEJLNzcsvNxY1pmBO7GGI"
# },
# "merchant": {
# "id": "ABC123TESTMTF19",
# "mcc": "5999",
# "address": null,
# "name": "Misc Retail"
# },
# "card": {
# "id": "crd-2B2I6c1m9wf9io7l4mASxdkAodJ",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "6997"
# },
# "user": {
# "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
# },
# "amount": {
# "local": {
# "total": 1000.0,
# "currency": "ARS"
# },
# "transaction": {
# "total": 135000000.0,
# "currency": "ARS"
# },
# "settlement": {
# "total": 150.0,
# "currency": "USD"
# },
# "details": [
# {
# "type": "EXTRACASH",
# "currency": "ARS",
# "amount": 500.0,
# "name": "EXTRACASH"
# },
# {
# "type": "BASE",
# "currency": "ARS",
# "amount": 13000.0,
# "name": "BASE"
# }
# ]
# }
# }' \
#  'https://pomelo-adapter.qa.clave.cloud/transactions/adjustments/credit'