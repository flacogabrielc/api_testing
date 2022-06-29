import json
import requests
import pytest

#prueba obtener el jwt y usarlo en un test

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
    #print(response_json)

    #print(response.json())
    #return response_json
    #print(response_json)
#
# jotaw = test_obtener_jwt()
# print(jotaw)

def test_tc_006_consultar_saldos():
    jotaw = obtener_jwt()

    headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': jotaw, 'customerExternalId': userID}

    url = "https://api.qa.clave.cloud/core/customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7/balances"

    response = requests.get(url, headers=headersdata)
    response_json = response.json()

# def test_tc_006_consultar_saldos():
#
#     headersdata = {'apikey': 'ltYkkzeoPZLhYtXjNpYpTt9cEFb9elNE', 'jwt': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTY1MzI5NjMsImlhdCI6MTY1NjUzMTE2MywiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiMTlmYzI2NTctODVmNC1jM2ZhLWY3NGQtY2YzN2UxMmU1ZGI5fEFSRyJ9.mtYzP2sBwuq-Rvk0EivjoKQsY5PMS9Qin3KSblVdhVWL4whPMy3F4KImR_dwRbv3OUjOGcfcgWpbXfok6ysSDTQKJfjPSXoml9vz-2KETGkRvmRmzp9M7ZslPv5vc1giwUsDkRei7Fo0b_jJVEXnNtbvTEa-4mfS3B6tfwvObBcVmzZP2EJFDuRXPgHe7IRA_4DexCNEDfqKp8bQKcocDIIFsrbN13aLRePfbbaV4P1edA_SLjTFEGK5OAP_J_55Hrf__dABe9bW7vFrqa_BKvM933d_DFZDOv-XwMI1cXzeWcMsktIdKnOD8OHlp5nEL8LQ32v4sAG8hoRhXJZFGpTmY4zNvsDPn0bI7TeUM4FoojOdMDdQxjnuuyzbDqf0WJdsR_g0jeUUlJmV5EW2WvKczoNjJ8PWH7nK9SkLs9kygpV5VRi9pAq-ZybuJ01bp_rvz2Dn2PEwO3jnFd0UAADjS5NcGxfPSvv-X5aZaSpx2-IdbQwfF_jg5EL3Lt51Axh1CXkyPiiVvpEXD7dcUtU1mjJOq9RQXe29BzY1OrLCRclRcE9Re7Grg7OY6_OYnwRyjhOZLriE-kSVIfU47ds3Eb2a3UtERd_GmI9dHByHLBHbjkvsFoD0lYROE8_cnaTTpl_bQIHk-AEJH7hPIYuLeE6yO7NZBzLVG3P8RyU', 'customerExternalId': '19fc2657-85f4-c3fa-f74d-cf37e12e5db9' }
#
#     url = "https://api.qa.clave.cloud/core/customer/c27ed8c7-ed0e-4c7e-826e-a8e345190aa7/balances"
#
#     response = requests.get(url, headers=headersdata)
#     response_json = response.json()