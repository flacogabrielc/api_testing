import json
import requests
import pytest

# prueba obtener el jwt y usarlo en un test - done
# usar marquers grouping ver video 91 en adelante #tags and execution with tAGS - done
# choose 10!
# reporting + screenshots
#execute code before and after pytest Fixtures
# agregar assertions
# ver modos de ejecucion con mas impresion por pantalla
# una variable global de tipo environment tambien viendo a futuro donde este -> https://api.qa.clave.cloud/, y
# las otras refes a Qa o el ambiente que tenga que ser
# nomenclatura de los casos asociados a historias


userID = '19fc2657-85f4-c3fa-f74d-cf37e12e5db9'

def obtener_jwt():
    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'Content-Type': 'application/json'}

    data = {
    "customerExternalId" : userID,
    "ip" : "127.0.0.1",
    "hash" : "e0d123e5f316bef78bfdf5a008837578",
    "deviceData" : "Iphone"

    }

    url = "https://api.qa.clave.cloud/client/jwt/"

    response = requests.post(url, headers=headersdata, json=data)
    response_json = response.json()

    return response_json['jwt']
#
# jotaw = test_obtener_jwt()
# print(jotaw)

def test_tc_006_consultar_saldos():
    jotaw = obtener_jwt()

    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': jotaw, 'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/core/customer/19fc2657-85f4-c3fa-f74d-cf37e12e5db9/balances"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
