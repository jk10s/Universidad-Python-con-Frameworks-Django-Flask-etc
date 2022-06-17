import psycopg2

conexion=psycopg2.connect(
    user= 'admini',
    password='1234',
    host='localhost',
    port='5432',
    database='abril'
    
    )
try:
    with conexion:
        with  conexion.cursor() as cursor:
            sentencia = "select edad from persona where nombre='pedro'"
            cursor.execute(sentencia)
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'ocurrio un eror de tipo: {e}')

finally:
    conexion.close()
