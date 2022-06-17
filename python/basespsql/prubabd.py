import re
import psycopg2
conexion= psycopg2.connect(
    user='admini',
    password='1234',
    host='localhost',
    database='abril',
    port='5432'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            setencia="select * from persona where nombre in ('carmen','diego')"
            #nombre=input("ingrese el nombre a buscar ")
            cursor.execute(setencia)
            registro= cursor.fetchall()
            print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()