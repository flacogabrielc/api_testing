import requests
import json

def ob_token(customerId):

    headersdata = {'Content-Type':'application/json'}

    data = {
        "customerExternalId":customerId,
        "ip" : "127.0.0.1",
        "hash" : "e0d123e5f316bef78bfdf5a008837578",
        "deviceData" : "Iphone",
    }

    # API url
    url = "https://client.qa.clave.cloud/client/jwt"

    response = requests.post(url, headers = headersdata, json = data  )

    #print(response.text)
    #print(response.json())
    response_json = response.json()
    #print(response_json)

    jwt_token = response_json['jwt']
    #
    print(jwt_token)
    return jwt_token

#
# [6:08 PM, 4/22/2022] Cristian Arzuaga: enes que instalarte esta libreria
# [6:08 PM, 4/22/2022] Cristian Arzuaga: pip install psycopg2
# [6:08 PM, 4/22/2022] Cristian Arzuaga: y despues en python
# [6:08 PM, 4/22/2022] Cristian Arzuaga: import psycopg2
#
# #establishing the connection
# conn = psycopg2.connect(
#    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
#
# #Executing an MYSQL function using the execute() method
# cursor.execute("select version()")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)
#
# #Closing the connection
# conn.close()