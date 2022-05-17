import requests
import json

headersdata = {'Content-Type':'application/json', 'Authorization':'Basic YWRtaW46cGFzc3dvcmQ=', 'customerExternalId':'f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd', 'jwt':'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTEwODI2NjgsImlhdCI6MTY1MTA4MDg2OCwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiZjI4NzlkZmQtY2UwYy1hZDg1LWIzYjgtN2M4NGI4NmEwY2JkfEFSRyJ9.bIQwQO9D50WpXY1f3wciUGYi4Jq_Hi3wy4ZDlS9cqIU97-5qz9HAuCHjBNTVnAfigFvlvRgpqZikartn2r-9UOPDu8nTR4Xk9DUGItFf0Sbeit51bdfZy5cxTXxwa7_M6YaDt0wgTsZDiDDqgcObg4RUIK8ftYUGi3TScU28pKJGBQY8XzMdtRM1WS3Yxyo8hoSjEQhlJVncze0ggXFjHBIsBuIUMIDIlcBOA0VWA1errkOL5I5r7DWNifoGlTG2CFFCylMv1Ho-UMR7zhrWH7APVJ48v8BSFAKVu35uljR2MQkJ4YdNVTopKVgjPT5JAOv-V5aRMVTkMFUd5i7HAjrIM1Biv3qVyh-PcG-gJv4H09SjrwegZ27lQOtjDkPsrm_yYVxyTMOk667fn2W1sKNrXi12jB8kVqHQuuRI5QJEl80oYXHlukfrM-sUjvglMFhqcNJxy6F8nygv41D4lR17BIQsqERordbONSmffGmgH8xmE0gCUfNpbwlDkw2cXGc0p1yzrxJzd91kHsUopnz5oVd75H9p4klWT87-gU0DdyMKYArHrRQYWFLXArWr0LgY4J0zKbk2wf4McqVE-ziUQm0083iAmdJmo06Z9lo0q0GZvsCre-Rvq9vDaTIITr-58Xh0QRexIYrOdpSABzcDfyxNn4JrBdSWMfqbBoU','apikey':'6KzvGaDHWtoni1zExtBEqIaNUx49fA8h'}

data = {
    "sourceCustomerExternalId": "f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd",
    "destinationCustomerExternalId" : "f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd",
    "operationTypeId" : 4,
    "performerUser" : "marina",
    "sourceAmount" : 115.54,
    "sourceCurrencyId" : "ARS",
    "transactionChannelTypeId" : 4,
    "params" : {
        "destinationBankAccountAlias": "SODIO.NOVIO46.CLAVE",
         "concept":"MNTICQSLNVSASQ"
    }
}

url = "https://api.qa.clave.cloud/core/operation"

response = requests.post(url, headers=headersdata, json=data)
print(response.text)
print(response.status_code)

# "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTEwODI2NjgsImlhdCI6MTY1MTA4MDg2OCwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiZjI4NzlkZmQtY2UwYy1hZDg1LWIzYjgtN2M4NGI4NmEwY2JkfEFSRyJ9.bIQwQO9D50WpXY1f3wciUGYi4Jq_Hi3wy4ZDlS9cqIU97-5qz9HAuCHjBNTVnAfigFvlvRgpqZikartn2r-9UOPDu8nTR4Xk9DUGItFf0Sbeit51bdfZy5cxTXxwa7_M6YaDt0wgTsZDiDDqgcObg4RUIK8ftYUGi3TScU28pKJGBQY8XzMdtRM1WS3Yxyo8hoSjEQhlJVncze0ggXFjHBIsBuIUMIDIlcBOA0VWA1errkOL5I5r7DWNifoGlTG2CFFCylMv1Ho-UMR7zhrWH7APVJ48v8BSFAKVu35uljR2MQkJ4YdNVTopKVgjPT5JAOv-V5aRMVTkMFUd5i7HAjrIM1Biv3qVyh-PcG-gJv4H09SjrwegZ27lQOtjDkPsrm_yYVxyTMOk667fn2W1sKNrXi12jB8kVqHQuuRI5QJEl80oYXHlukfrM-sUjvglMFhqcNJxy6F8nygv41D4lR17BIQsqERordbONSmffGmgH8xmE0gCUfNpbwlDkw2cXGc0p1yzrxJzd91kHsUopnz5oVd75H9p4klWT87-gU0DdyMKYArHrRQYWFLXArWr0LgY4J0zKbk2wf4McqVE-ziUQm0083iAmdJmo06Z9lo0q0GZvsCre-Rvq9vDaTIITr-58Xh0QRexIYrOdpSABzcDfyxNn4JrBdSWMfqbBoU"


# ALQ - Alquiler - done
#
# CUO - Cuota - done
#
# EXP - Expensas - dobne
#
# FAC - Factura - done
#
# PRE - Préstamo - done
#
# SEG - Seguro - don
#
# HON - Honorarios - don
#
# HAB - Haberes - done
#
# VAR - Varios - done

