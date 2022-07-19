# import boto3
# import sqlalchemy as db
import psycopg2
# from sqlalchemy.sql import select
# import sqlite3
#import requests
#import random
import pytest
# prueba con psycopg2

def db_gateway():

    try:
        connection = psycopg2.connect(
            host='db-aurora-postgres-shared-rw.qa.clave.cloud',
            user='gabriel.carballo',
            password='3ThzAThEwZsdw678',
            database='gateway'
        )
        #query = gateway
        print("Conexion exitosa")
        cursor = connection.cursor()
        cursor.execute("SELECT version()")
        row = cursor.fetchone()
        print(row)
        # cursor.execute("SELECT * FROM country WHERE id = 11")
        # rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as ex:
        print(ex)
    finally:
        # connection.close()
        # print("se finalizo la conexion")
        return cursor

        # Equivalent to 'SELECT * FROM census'
        #query = db.select([census])

#prueba_db()

def prueba_con():
    recursor = db_gateway()
    recursor.execute("SELECT * FROM country WHERE id = 11")
    rows = recursor.fetchall()
    for row in rows:
        print(row)

prueba_con()





# ver como conectarse con sqlite
#prueba con sqlite3
#def preba_db1():
    #connection = sqlite3.connect('db-aurora-postgres-shared-rw.qa.clave.cloud', 'gabriel.carballo'

#             user='gabriel.carballo',
#             password='3ThzAThEwZsdw678',
#             database='gateway')


# userID = '19fc2657-85f4-c3fa-f74d-cf37e12e5db9'
# cardid = ''
#
# def db_gateway():
#
#     try:
#         connection = psycopg2.connect(
#             host='db-aurora-postgres-shared-rw.qa.clave.cloud',
#             user='gabriel.carballo',
#             password='3ThzAThEwZsdw678',
#             database='gateway'
#         )
#         print("Conexion exitosa")
#         cursor = connection.cursor()
#         cursor.execute("SELECT version()")
#         row = cursor.fetchone()
#         print(row)
#
#         for row in rows:
#             print(row)
#     except Exception as ex:
#         print(ex)
#     finally:
#         return cursor

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
    print(response.json)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
