import requests

headersdata

data







# curl --location --request POST 'https://bindadapter.api.dev.clave.cloud/transaction-types/transfer-callback/transactions' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "id": "61944a28-445e-420e-877e-8666872ac17e",
#     "object": "ApiTransaction",
#     "created": "2022-04-12T13:06:44.748Z",
#     "data": {
#         "id": "DLMORZP908K3LO4NEGJ485",
#         "type": "TRANSFER",
#         "from": {
#             "bank_id": "322",
#             "account_id": "20-1-735016-1-0"
#         },
#         "counterparty": {
#             "id": "20177130811",
#             "name": "Roberto Leto",
#             "id_type": "CUIT_CUIL",
#             "bank_routing": {
#                 "scheme": "UNAVAILABLE",
#                 "address": ""
#             },
#             "account_routing": {
#                 "scheme": "CVU",
#                 "address": "0000451400272771308104"
#             }
#         },
#         "details": {
#             "origin_credit": {
#                 "cvu": "0000001700205097767427",
#                 "cuit": "20509776742"
#             }
#         },
#         "transaction_ids": [
#             "DLMORZP908K3LO4NEGJ480"
#         ],
#         "status": "COMPLETED",
#         "start_date": "",
#         "end_date": "2999-12-31T00:00:00.000Z",
#         "charge": {
#             "summary": "VAR COMPLETE_TRANS",
#             "value": {
#                 "amount": 300.45
#             }
#         },
#         "business_date": "2022-04-12T03:00:00.000Z"
#     },
#     "type": "transfer.cvu.received",
#     "redeliveries": 0
# }'