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
            sentencia="delete from persona where nombre in %s"
            cama=input("propociona los nombres e eliminar ")
            valores=(tuple(cama.split(',')),)
            cursor.execute(sentencia,valores)
            regitrosinsertados= cursor.rowcount
            print(f'registros eliminados: {regitrosinsertados}')
           
except Exception as e:
    print(e)
finally:
    conexion.close()