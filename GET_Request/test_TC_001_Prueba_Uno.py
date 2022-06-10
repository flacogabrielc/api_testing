import pytest
import requests
#import allure

# Test case code must be written inside a method
# method name must be started with test
# si los ejecuto con -v nos muestra el resultado de cada uno ex: pytest -v GET_Request/test_TC_001_Prueba_Uno.py
# ejecutar como ->  pytest -v GET_Request -mismo efecto que el file pero lo hace con todos los que estan dentro del folder
# -s print statement output en este caso "this is...."

#using decorator
@pytest.mark.skip('skipping as this functionality is not marking, developer will fix it new build')
def test_tc_001_get_users():
    #put test case code over there
    #method with test name
    print('This is out test case code')
    print('This is end of my test case')

def test_tc_003_deposit_account():
    print('prueba ejecucion test case')
    print('another test')

#@pytest.mark.skip
def test_tc_004_get_idm_users():
    headersdata = {'Authorization': 'Bearer CxYDpEomtDPYMfYk5ysVVDWRNkswip9Y', 'X-Caller-Id': 'CLAR',
                   'Content-Type': 'application/json'}
    # data is the body
    data = {
        "organization_id": "CLAVE_ARG",
        "page": 1,
    }

    # API URL
    url = "https://idm.qa.clave.cloud/api/get_users"

#    response = requests.post(url, headers=headersdata, json=data)
#    print(response.text)

# customerId = "19fc2657-85f4-c3fa-f74d-cf37e12e5db9"
# @pytest.

#def test_tc_005_obtener_token(customerId):
def test_tc_005_obtener_token():
    #customerId = "19fc2657-85f4-c3fa-f74d-cf37e12e5db9"
    headersdata = {'Content-Type': 'application/json'}

    data = {
        "customerExternalId": "19fc2657-85f4-c3fa-f74d-cf37e12e5db9",
        "ip": "127.0.0.1",
        "hash": "e0d123e5f316bef78bfdf5a008837578",
        "deviceData": "Iphone",
    }

    # API url
    url = "https://client.qa.clave.cloud/client/jwt"

    response = requests.post(url, headers=headersdata, json=data)

    # print(response.text)
    # print(response.json())
    response_json = response.json()
    # print(response_json)

    jwt_token = response_json['jwt']
    #
    print(jwt_token)
    return jwt_token

#test_tc_005_obtener_token("19fc2657-85f4-c3fa-f74d-cf37e12e5db9")
#test_tc_004_get_idm_users()


