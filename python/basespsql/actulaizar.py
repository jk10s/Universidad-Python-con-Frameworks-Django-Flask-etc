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
            sentencia="update persona set nombre=%s, edad=%s where nombre=%s"
            valores=('natalia',20,'rodolfo')
            cursor.execute(sentencia,valores)
            regitrosinsertados= cursor.rowcount
            print(f'registros actualizados: {regitrosinsertados}')
           
except Exception as e:
    print(e)
finally:
    conexion.close()