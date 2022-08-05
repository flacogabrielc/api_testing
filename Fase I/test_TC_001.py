import pytest
import json
import requests
import random
import psycopg2

# BD ! conexion para posterior validacion para:
# Tabla OPERATION - STATUS FINISHED
# los casos que tendríamos que validar si o si con la
# BD es:
# - recargas, ?
# - pago con tarjeta,???
# - retiro, ?
# - extracash, - operaciones . pomelo
# - extracción por cajero,

# - depósito, 47 -> 50
# - retiro por transferencia, 18
# - envío de dinero, 015
# - pago de servicios, 21 -> 26

# REVERSAS (extracash, compras, extracción por cajero)
# digamos todo lo que genere una operación en Pluma
# hay que validar contra el campo status de la tabla operation de Pluma

# LUEGO :
# 36 y 37 - faltan terminar pausar y habilitar tarjeta
# ejecutar con infomre
# ui!
# Ver mails qa

# ver como agregar una validacion que cuando el assert no es correcto imprima lo que devuelve
# execute like pytest -s -v test_TC_Pruebas.py
# with marks pytest -s -v -m Smoke test_TC_Pruebas.py
# tener en cuenta que el externalID tiene que estar dado de alta en el -  idm para poder ejecutar este caso create_user(idm)
# agregar los nuevos casos para el alta completa

userID = '19fc2657-85f4-c3fa-f74d-cf37e12e5db9'
cardid = ''
gateway = 'gateway'
pomelo = 'pomelo'
bindadapter = 'bindadapter'
pluma = 'pluma'


def db_connection(db):

    try:
        connection = psycopg2.connect(
            host='db-aurora-postgres-shared-rw.qa.clave.cloud',
            user='gabriel.carballo',
            password='3ThzAThEwZsdw678',
            database=db
        )
        print("Conexion exitosa")
        cursor = connection.cursor()
        cursor.execute("SELECT version()")
        row = cursor.fetchone()
        print(row)

        # for row in rows:
        #     print(row)
    except Exception as ex:
        print(ex)
    finally:
        return cursor


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

#@pytest.mark.Gabo no se tiene en cuenta por el momento porque hay que ddar de alta por otros endpoints tamvbien
def test_tc_001_alta_cliente():
    headersdata = {'Content-Type': 'application/json', 'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE'}

    # data is the body
    data = {"externalId": "544c866c-4f36-44c2-aece-b8faafe470eb"

            }

    url = "https://api.qa.clave.cloud/gateway/customers"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()
    print(response_json)

#@pytest.mark.Gabo , no se tiene en cuenta por el momento porque hay que ddar de alta por otros endpoints tamvbien
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

@pytest.mark.Gabo
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
    response_json = response.json()
    #print(response.status_code)
    aidi = response_json['id']
    print(aidi)
    #print(aidi)
    recursor = db_connection(gateway)
    recursor.execute("select id from voucher order by id desc limit 1")
    #recursor.execute("select currency_id from voucher order by id desc limit 1")
    voucherid = recursor.fetchone()
    vou = voucherid[0]
    #print(vou)
    assert aidi == vou
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

#agregar 041, 042 para uso del voucher que no se repita continuamente

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
@pytest.mark.Smoke
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

@pytest.mark.Smoke
def test_tc_018_ret_por_trans():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {"sourceCustomerExternalId": userID,
            "destinationCustomerExternalId": userID,
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
    assert response.status_code == 202

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

@pytest.mark.Smoke
#tener en cuenta que para python null = None
def test_tc_024_pago_serv_s_fac():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "sourceCustomerExternalId": userID,
        "destinationCustomerExternalId": userID,
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
            "expirationDate": None,
            "reference": None,
            "hash": "1O3x_f-Qbeh4xH8moc1vO58ES0zJs5cLFyDq9kXx9kY",
            "type": "fetchedBill"
        }

    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

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

@pytest.mark.Smoke
def test_tc_026_serv_pay_bar_cod():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "sourceCustomerExternalId": userID,
        "destinationCustomerExternalId": userID,
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
            "expirationDate": None,
            "reference": None,
            "hash": "8bbUMR9SprDIEg5jGyM3ZByHb8Hl7QouPK9SXxlpqU8",
            "type": "barcode"
        }
    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

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

@pytest.mark.Smoke
def test_tc_028_pay_rec_phone():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "sourceCustomerExternalId": userID,
        "destinationCustomerExternalId": userID,
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

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

@pytest.mark.Smoke
def test_tc_029_pay_rec_cable():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "sourceCustomerExternalId": userID,
        "destinationCustomerExternalId": userID,
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

    response = requests.post(url, headers=headersdata, json=data)
    assert  response.status_code == 202

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

#No vigente por el momento el endpoint
# def test_tc_031_alta_cred():
#     jotaw = obtener_jwt()
#     headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
#                    'jwt': jotaw,
#                    'customerExternalId': userID, 'Content-Type': 'application/json'}
#
#     data = {
#         "customerExternalId": userID,
#         "productId": "patriot",
#         "vendorId": 896522
#     }
#
#     url = "https://api.qa.clave.cloud/credit/requests"
#
#     response = requests.post(url, headers=headersdata, json=data)
#     assert response.status_code == 202

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

@pytest.mark.Smoke
def test_tc_034_alta_tar_fis():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "customerExternalId": userID,
        "street": "Sergio Dembis",
        "streetNumber": "345",
        "floor": "4",
        "apartment": "D",
        "city": "Ciudad de Buenos Aires",
        "state": "CABA",
        "neighborhood": "Mataderos",
        "zipCode": "1440"
    }

    url = "https://cards-api.qa.clave.cloud/cards"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()
    global cardid
    cardid = response_json['cardId']
    #global
    print(cardid)
    #print(response_json)
    #return cardid
    #cardid == cardidi
    assert response.status_code == 201

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

#tendria que recorrer la lista de tarjetas y agarrarar la que este en status = Active
#y de esa sacar los parametros necesarios para pausarla cardid, last four
#en realidad ya tengo el card id, capturado tengo que agarrar
#todo el registro de la tarjeta que tengao que ver

#@pytest.mark.Gabo
def test_tc_036_pausar_tarjeta():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "cardId": cardid,
        "lastFour": "2740",
        "status": "PAUSED",
        "cardType": "PHYSICAL",
        "startDate": "2022-01-21"
    }

    url = f'https://api.qa.clave.cloud/cards/{cardid}/pause'

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

    response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_038_baj_tarj():
    jotaw = obtener_jwt()
    #cardid = test_tc_034_alta_tar_fis()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "reason": "LOST"
    }

    url = f'https://cards-api.qa.clave.cloud/cards/{cardid}/disable'

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

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

@pytest.mark.Smoke
def test_tc_041_cod_val_send_email():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "to": "gcarballo@clave.com",
        "type": "EMAIL",
        "client": "CLAVE"

    }

    url = "https://api.qa.clave.cloud/validation/send"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

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

#@pytest.mark.Gabo se desprecia porque se debe tener el valor para ingresarlo a mano del codigo
# def test_tc_043_cod_val_validate():
#     jotaw = obtener_jwt()
#     headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
#                    'jwt': jotaw,
#                    'customerExternalId':userID, 'Content-Type': 'application/json'}
#
#     data = {
#         "traceId": "0b6fbf0d-ac0f-4f3b-9c9c-d1678d236c49",
#         "code": "884698"
#
#     }
#
#     url = "https://api.qa.clave.cloud/validation/validate"
#
#     response = requests.post(url, headers=headersdata, json=data)

@pytest.mark.Smoke
def test_tc_044_enr_dat():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE'}

    url = "https://api.qa.clave.cloud/identity-service/v2/person/6503558/N"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200

@pytest.mark.Smoke
def test_tc_046_val_extid():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'jwt': jotaw,
                   'customerExternalId': userID, 'Content-Type': 'application/json'}

    data = {
        "externalId": userID,
        "jwt": jotaw
    }

    url = "https://api.qa.clave.cloud/client/jwt/validate"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

#@pytest.mark.Gabo
#Ref Zephyr CORE-352 op_type1
def test_tc_047_deposito():
    jotaw = obtener_jwt()
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE',
                   'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
                   'jwt': jotaw,
                   'customerExternalId': userID,
                   'Content-Type': 'application/json'}

    data = {
      "sourceCustomerExternalId": userID,
      "destinationCustomerExternalId": userID,
      "operationTypeId": 1,
      "performerUser": "marceu",
      "sourceAmount": 10000,
      "sourceCurrencyId": "ARS",
      "destinationAmount": None,
      "destinationCurrencyTypeId": None,
      "transactionChannelTypeId": 1,
      "params": {

        }
    }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202


#@pytest.mark.Gabo
#Ref Zephyr CORE-351 Deposito por transferencia
def test_tc_048_deposito_por_transf():
    jotaw = obtener_jwt()
    headersdata = {'apikey': '0F5I6IhzXnZ6Qm5giwQ0IWiw94m2UsnK',
                   'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
                   'jwt': jotaw,
                   'customerExternalId': userID,
                   'Content-Type': 'application/json'}

    data = {
    "sourceCustomerExternalId": "19fc2657-85f4-c3fa-f74d-cf37e12e5db9",
    "destinationCustomerExternalId": "19fc2657-85f4-c3fa-f74d-cf37e12e5db9",
    "operationTypeId": 3,
    "performerUser": "Gabriel",
    "sourceAmount": 1500,
    "sourceCurrencyId": "ARS",
    "destinationAmount": None,
    "destinationCurrencyTypeId": None,
    "transactionChannelTypeId": 4,
    "params": {
    }

}
    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

#@pytest.mark.Gabo
#Ref Zephyr CORE-354 Envio de Dinero
def test_tc_049_envio_dinero():
    jotaw = obtener_jwt()
    headersdata = {'apikey': '0F5I6IhzXnZ6Qm5giwQ0IWiw94m2UsnK',
                   'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
                   'jwt': jotaw,
                   'customerExternalId': userID,
                   'Content-Type': 'application/json'}
    data = {
            "sourceCustomerExternalId": "69bf92ce-8619-dccd-1c83-66d49d04faee",
            "destinationCustomerExternalId": userID,
            "operationTypeId": 5,
            "performerUser": "marina",
            "sourceAmount" : 100,
            "destinationAmount": 100,
            "sourceCurrencyId": "ARS",
            "destinationCurrencyId": "ARS",
            "transactionChannelTypeId": 1,
            "params": {
            "sourceClient": "Marina Ledesma",
            "destinationClient": "Gabriel Carballo"
            }
            }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202

#tener en cuenta que debe obtener el operation id de una transaccion previa
#@pytest.mark.Gabo
#Ref Zephyr CORE-353 Envio de Dinero
def test_tc_050_reversa_operacion():
    jotaw = obtener_jwt()
    headersdata = {'apikey': '0F5I6IhzXnZ6Qm5giwQ0IWiw94m2UsnK',
                   'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
                   'jwt': jotaw,
                   'customerExternalId': userID,
                   'Content-Type': 'application/json'}

    data = {
            "sourceCustomerExternalId": userID,
            "destinationCustomerExternalId": userID,
            "operationTypeId": 6,
            "performerUser": "mariL",
            "sourceAmount": None,
            "sourceCurrencyId": None,
            "transactionChannelTypeId": 4,
            "params": {
                "operationId": 3001,
                "comments": "la reverso"
            }

        }

    url = "https://api.qa.clave.cloud/core/operation"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 202


#    -H "Content-Type:application/json" \
#    -H "x-apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-60" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444966" \

#@pytest.mark.Gabo
def test_tc_053_pago_con_tarjeta():
    headersdata = {'Content-Type': 'application/json',
                   'x-apikey': 'ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=',
                   'x-endpoint': '/pomelo-adapter/transactions/authorizations',
                   'x-idempotency-key': 'test-idempotency-key-01',
                   'x-signature': 'hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=',
                   'x-timestamp': '1649444966'}

    data = {
              "transaction": {
                "id": "ctx-27WnxhnJ8787hV1XvLib327",
                "country_code": "ARG",
                "type": "PURCHASE",
                "point_type": "ECOMMERCE",
                "entry_mode": "MANUAL",
                "origin": "DOMESTIC",
                "local_date_time" : "2022-04-08T19:09:16",
                "original_transaction_id": None
              },
              "merchant": {
                "id": "111111111111111",
                "mcc": "5045",
                "address": None,
                "name": "Computer Software"
              },
              "card": {
                "id": "crd-2Bl8c6cgJcqRsElCdIXgOQgj2G4",
                "product_type": "PREPAID",
                "provider": "MASTERCARD",
                "last_four": "5437"
              },
              "user": {
                "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
              },
              "amount": {
                "local": {
                  "total": 10.0,
                  "currency": "ARS"
                },
                "transaction": {
                  "total": 990.0,
                  "currency": "ARS"
                },
                "settlement": {
                  "total": 11.0,
                  "currency": "USD"
                },
                "details": [
                  {
                    "type": "BASE",
                    "currency": "ARS",
                    "amount": 990.0,
                    "name": "BASE"
                  }
                ]
              }
            }

    url = "https://pomelo-adapter.qa.clave.cloud/transactions/authorizations"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

#@pytest.mark.Gabo
def test_tc_054_extraccion_por_cajero():
    headersdata = {'Content-Type': 'application/json',
                   'x-apikey': 'ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=',
                   'x-endpoint': '/pomelo-adapter/transactions/authorizations',
                   'x-idempotency-key': 'test-idempotency-key-101',
                   'x-signature': 'hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=',
                   'x-timestamp': '1649444965'}

    data = {
              "transaction": {
                "id": "ctx-test-withdrawal-123",
                "country_code": "ARG",
                "type": "WITHDRAWAL",
                "point_type": "POS",
                "entry_mode": "MAG_STRIPE",
                "origin": "DOMESTIC",
                "local_date_time" : "2022-07-07T12:45:00",
                "original_transaction_id": None
              },
              "merchant": {
                "id": "ID-Code06",
                "mcc": "6011",
                "address": None,
                "name": "Automated Cash Disb"
              },
              "card": {
                "id": "crd-2BjHfef1FQ2ilvvBky3cxgyc8jk",
                "product_type": "PREPAID",
                "provider": "MASTERCARD",
                "last_four": "8912"
              },
              "user": {
                "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
              },
              "amount": {
                "local": {
                  "total": 200.0,
                  "currency": "ARS"
                },
                "transaction": {
                  "total": 10000.0,
                  "currency": "ARS"
                },
                "settlement": {
                  "total": 8.0,
                  "currency": "USD"
                },
                "details": [
                  {
                    "type": "BASE",
                    "currency": "ARS",
                    "amount": 1000000000.0,
                    "name": "BASE"
                  }
                ]
              }
            }

    url = "https://pomelo-adapter.qa.clave.cloud/transactions/authorizations"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

@pytest.mark.Gabo
def test_tc_055_extracash():
    headersdata = {'Content-Type': 'application/json',
                   'x-apikey': 'ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=',
                   'x-endpoint': '/pomelo-adapter/transactions/authorizations',
                   'x-idempotency-key': 'test-idempotency-key-17',
                   'x-signature': 'hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=',
                   'x-timestamp': '1649444963'}

    data = {
              "transaction": {
                "id": "ctx-200kXoaEJLNzcsvNxY1pmBO9GHU",
                "country_code": "ARG",
                "type": "EXTRACASH",
                "point_type": "POS",
                "entry_mode": "MAG_STRIPE",
                "origin": "DOMESTIC",
                "local_date_time": "2022-07-07T12:45:00",
                "original_transaction_id": None
              },
              "merchant": {
                "id": "ABC123TESTMTF19",
                "mcc": "5999",
                "address": None,
                "name": "Misc Retail"
              },
              "card": {
                "id": "crd-2BjHfef1FQ2ilvvBky3cxgyc8jk",
                "product_type": "PREPAID",
                "provider": "MASTERCARD",
                "last_four": "8912"
              },
              "user": {
                "id": "usr-25QOzhZMAHVnN5FyvJTyxAKhsWU"
              },
              "amount": {
                "local": {
                  "total": 1350.0,
                  "currency": "ARS"
                },
                "transaction": {
                  "total": 135000000.0,
                  "currency": "ARS"
                },
                "settlement": {
                  "total": 150.0,
                  "currency": "USD"
                },
                "details": [
                  {
                    "type": "EXTRACASH",
                    "currency": "ARS",
                    "amount": 500.0,
                    "name": "EXTRACASH"
                  },
                  {
                    "type": "BASE",
                    "currency": "ARS",
                    "amount": 13000.0,
                    "name": "BASE"
                  }
                ]
              }
            }

    url = "https://pomelo-adapter.qa.clave.cloud/transactions/authorizations"

    response = requests.post(url, headers=headersdata, json=data)
    assert response.status_code == 200

db_connection(gateway)

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

# ago para sumar al mostro
#
# curl -i -X GET \
#    -H "apikey:ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE" \
#    -H "jwt:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTk0Mzk5MDksImlhdCI6MTY1OTQzODEwOSwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiMmRlOTdkZmMtMTk1NC0xNGI0LTk0MDktZTcwZjk2MTUzYWUyfEFSRyJ9.K8mf6Rgd6gtUGLxiz5aDZj2RRwSCLs8OCJiDvAKFfcggNEMMZSufwkNCLdIFQE7sEaYq3sbr-TKXyHZds6Wn7dohrHQnFp1AgV40mfAspupTeESiTQq8E00wBS_XBL0A6ECBK8yjwI0wLMrd7e-FS7U7TvVV_j_RLuDW3wFz_AxzwoZ_BeLjfBADMLiR3dIH45_RwWQ4J2BgssHbtLO6RZ1YJsHp6DKKKvoaFgHJfwUmHwVXahlq_1qua9uxcXBUU_YNmcdzyvFu9g6kn15PtXE89eaJOqpt2UBeYC9JZrtE8rPiXL82TnYK5zMXtZRHdwBP-lTqJgkdEV6PsxFGvHn9niipQdDiGTrfXGLz5Vhaldfxnk-pJbsvRkGURW7KqNmZi3yXwKiMjuI3qAz_GxQCnN5N9hQFILn3o4ZkybRu4DC4SEFXEmqmQx8H4QSZ1_Nxqwr9Aplx_P3AVapbOGJrQRSlXWDXiusbFIfCBhQwBJBEEyeJ_bZU8AbAnmqwaknCygxlOTCCT-HcAP8e3wDCGG_tyoY1GmwsjJrcZae7nzNYjdpH7i6B0_tYSNaWO53TFuEe8eWv82ogiLYDAioNTVeQYR3N5QlOzYBbxvhuwExFXIoDGqUAT1I3bputpobCWRbt8GD1hUsNe3tclj0cA0NQpkD8cxNLQ5FDDiw" \
#    -H "customerExternalId:2de97dfc-1954-14b4-9409-e70f96153ae2" \
#  'https://api.qa.clave.cloud/voucher/104'
# capaz lo podemos sumar al monstruo


# URGENTE TO ADD.
#
# Pago con tarjeta:

# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "x-apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-60" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444966" \

#    -d \
# '{
# "transaction": {
# "id": "ctx-27WnxhnJ8787hV1XvLib322",
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
# "id": "crd-2Bl8c6cgJcqRsElCdIXgOQgj2G4",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "5437"
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
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'



# extracción por cajero
# curl -i -X POST \
#    -H "Content-Type:application/json" \
#    -H "x-apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
#    -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
#    -H "x-idempotency-key:test-idempotency-key-70" \
#    -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
#    -H "x-timestamp:1649444965" \
#    -d \
# '{
# "transaction": {
# "id": "ctx-test-withdrawal-120",
# "country_code": "ARG",
# "type": "WITHDRAWAL",
# "point_type": "POS",
# "entry_mode": "MAG_STRIPE",
# "origin": "DOMESTIC",
# "local_date_time" : "2022-07-07T12:45:00",
# "original_transaction_id": null
# },
# "merchant": {
# "id": "ID-Code06      ",
# "mcc": "6011",
# "address": null,
# "name": "Automated Cash Disb"
# },
# "card": {
# "id": "crd-2BjHfef1FQ2ilvvBky3cxgyc8jk",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "8912"
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
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'

# Extracash
# curl -i -X POST \
# -H "Content-Type:application/json" \
# -H "apikey:ohbH43UkLG9QHBVv8gKvbp03aTU3fvi+faikEqwIHL8=" \
# -H "x-endpoint:/pomelo-adapter/transactions/authorizations" \
# -H "x-idempotency-key:test-idempotency-key-15" \
# -H "x-signature:hmac-sha256 JfUl0Hfp12n9U/cnBIYMXx0WEZbi3LT06OlQAGqat8g=" \
# -H "x-timestamp:1649444963" \
# -d \
# '{
# "transaction": {
# "id": "ctx-200kXoaEJLNzcsvNxY1pmBO7GHH",
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
# "id": "crd-2BjHfef1FQ2ilvvBky3cxgyc8jk",
# "product_type": "PREPAID",
# "provider": "MASTERCARD",
# "last_four": "8912"
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
#  'https://pomelo-adapter.qa.clave.cloud/transactions/authorizations'



# retiro cual?


# ahí te paso por si no lo tenés a ese endpoint
# curl -i -X POST \
# H "Content-Type:application/json" \
# H "jwt:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQwMjQ4NzYsImlhdCI6MTY1NDAyMzA3NiwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiZjI4NzlkZmQtY2UwYy1hZDg1LWIzYjgtN2M4NGI4NmEwY2JkfEFSRyJ9.em03muc9yNedZlrmsPKQVKI4dBQCo7rYXL5o_ELmIj523a1VMgjHeWPGpxJfBgTQisa8DuJ3fUs39HpVO_-XVFvQ0gngbPuFUFWaC-MGOVVs1mhwAGcFjEyfpuufQ7HgGtMn4QSGH_fMdKmmlXea1TbQUBmIwQIevq4vuyvZkJ7KapadVK1J8_opi3CdvYP82wUNi3nH3_IdOu8cPfTA8lf-a0vPDfHkoO90xM4JWicq3h4qbhiGHcLcUuCaRZc69kVWq4nZ4TYliI01ODsXCVhneNZHVPH-zOvrUgeninaDTs87MR8d7SGZ1tSIyeNXDIP9UtVU-WlWUhRAJv3XK-N8F48qSKJ0qFZ6uviZP6_EjjOy6gKTpZOWdTEqfSbR8xN0a2IHpMSlN9j_sOipoaJk12MM88ZR1418g5XRvEF0ebX_DQf99IcSKtAy0k11W-su6-QHMJkQMkHuJYe1fLcuDUz3zJawHn9InJIDmk7QdH78Uoq06MHNijH-L4ip3-AJ9HLkPoDThCdTFKclIYTCc3Em0meLWJu_O9O9-jyklo6_rrIQJX6qQXHcW38qaotd76ijfuoZYTUEBlhbYXlzamhdzgxiqoirSLp8rN7ake6dzBSqWTYpYADLrAjov6XeMx3LcuF0_A3ZOIr8VHypI7UD6bslY229kQp56cA" \
# H "apikey:47leXLWBdQEyViVMrqXrk7ORFIJWWFaP" \
# H "customerExternalId:f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd" \
# H "Authorization:Basic YWRtaW46cGFzc3dvcmQ=" \

# \
# '{
#  "customerExternalId": "fe96d723-e386-502a-26b8-6d6539cfe2bc",
# "type": "WITHDRAWAL",
# "transactionChannelTypeId": 2,
# "currencyCode": "ARS"
# }' \
#'https://gateway.qa.clave.cloud/vouchers'
# Frances0170117920000000889685CBU