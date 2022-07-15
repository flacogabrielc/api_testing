import boto3
import sqlalchemy as db
import psycopg2
# from sqlalchemy.sql import select

try:
    connection=psycopg2.connect(
        host='db-aurora-postgres-shared-rw.qa.clave.cloud',
        user='gabriel.carballo',
        password='3ThzAThEwZsdw678',
        database='gateway'
    )
    #query = gateway
    print("Conexion exitosa")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM country")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("se finalizo la conexion")

    # Equivalent to 'SELECT * FROM census'
    #query = db.select([census])