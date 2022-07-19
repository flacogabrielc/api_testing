import boto3
import sqlalchemy as db
import psycopg2
# from sqlalchemy.sql import select
import sqlite3

# prueba con psycopg2
def prueba_db():

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
    recursor = prueba_db()
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

