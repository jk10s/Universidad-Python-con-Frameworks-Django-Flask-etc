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
            sentencia="INSERT INTO persona(nombre,edad) VALUES(%s, %s)"
            valores=(
            ('juliana',9),
            ('camilo',28),
            ('pacho',8)
            )
            cursor.executemany(sentencia,valores)
            
            regitrosinsertados= cursor.rowcount
            print(f'registros insertados: {regitrosinsertados}')
           
except Exception as e:
    print(e)
finally:
    conexion.close()