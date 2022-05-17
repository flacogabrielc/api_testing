import requests
import json

headersdata = {'Content-Type':'application/json', 'apikey':'0F5I6IhzXnZ6Qm5giwQ0IWiw94m2UsnK', 'jwt':'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTA5OTEyNTgsImlhdCI6MTY1MDk4OTQ1OCwiaXNzIjoiY2xhdmUuY29tIiwic3ViIjoiZjI4NzlkZmQtY2UwYy1hZDg1LWIzYjgtN2M4NGI4NmEwY2JkfEFSRyJ9.KP44cMUyJpkSKbqF1P1G5Xf-o9ZSzL2h8tpG1WvvlAC0VXVW6kFKHTGJmKnVdc_Lj4JPFxiL2mWhiGqY3KlOgo8w_Hzd4DZ96ajFVTOVzg0Ygp4wOTewlkA7To23Y6f10Qu5XWRpNtG9vNGTFLO-Iap6FotKpkrKtnQPaZSYTxCgi_k3W9f7gtAw-GKnC5rvCUxCjGzFwyUZrJrEOPRdMvq0ViWJl-xpIaqoXs27OaIGacsNYE_XSLecJ08NMT3mZezKokCTHxCqIlHkYdlhbTMXSNmp0YjLhjdLmX7uDpFy5KdH5WsjH7wE2aAPfHQzCeEN6n0hgSRq0k4_x3A8KjgTe2hg_i_moaxno2BCBcps5DZs1aBl1p6VsVNfIZW7sVnfxTBtTWZHS9EIm0iruYg7d5DIiQNhWj-m9Rlm127rfJx4XRxnQKofIrEOU8Vi-5rymbARcYo6o0iVsDXxPIGsPkdHNkDeJIS7qY4pvwASy5g6VQQoF_YeG1wWJmofL-dz5toNeRgHQ0Q_fmgaJDl4u2uWKHSU1_rIOixy2aIq1tmJiJ_XDt5TSITqJX76R2fD1gkz84GXiXB9JwjRnUI_P-10y0VfuH5F9-CSTfLJshFVYCnTjfHTch46RcHKutDVIt6FDsGfY4PkBy3vq-yTMw_3R2YU_b09yFHGQq8','customerExternalId':'f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd'}

data = {
  "sourceCustomerExternalId":"f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd",
  "destinationCustomerExternalId":"f2879dfd-ce0c-ad85-b3b8-7c84b86a0cbd",
  "operationTypeId": 3,
  "performerUser":"marina",
  "sourceAmount": 2000,
  "sourceCurrencyId":"ARS",
  "destinationAmount": None,
  "destinationCurrencyTypeId": None,
  "transactionChannelTypeId": 4,
  "params": {
  }

}

url = "https://api.qa.clave.cloud/core/operation"

response = requests.post(url, headers=headersdata, json=data)
print(response.text)
