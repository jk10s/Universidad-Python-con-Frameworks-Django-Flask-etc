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
    conexion.autocommit=False   
    cursor= conexion.cursor() 
    sentencia="update persona set nombre=%s, edad=%s where nombre=%s"
    valores=('guzman',20,'natalia')
    cursor.execute(sentencia,valores)
    regitrosinsertados= cursor.rowcount
    conexion.commit()
    print(f'registros actualizados: {regitrosinsertados}')
           
except Exception as e:
    print(e)
finally:
    conexion.close()

