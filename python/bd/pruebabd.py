""" from dbm import _Database
import psycopg2

conexion= psycopg2.connect(
    user='admini',
    password='1234',
    host='121.0.0.1',
    port='5432'
    database='datos'
)
    
   

print(conexion) """