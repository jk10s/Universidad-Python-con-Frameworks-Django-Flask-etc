from capadedatospersona import log
import sys
import psycopg2

class Conexion:
    _user='admini'
    _password='1234'
    _host='localhost'
    _port='5432'
    _database='abril'
    _conexion=None

    @classmethod
    def obtenerconexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion= psycopg2.connect(
                    user=cls._user,
                    password=cls._password,
                    host=cls._host,
                    database=cls._database,
                    port=cls._port)
                log.debug(f' se ha conectado correctamente {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f' error de conexion {e}')
                sys.exit()
        else:
            return cls._conexion


if __name__=='__main__':
    Conexion.obtenerconexion()



""" 
abajo de esta de la vida por tres cadenas de caracteres de  la vida e 'oer;:;:;;;;;:
hola: 
como andas:
de la vida de los prestasiones de la vida q'

 """






















""" from capadedatospersona import log
import psycopg2 as bd
import sys

class Conexion:
    _user='admini'
    _password='1234'
    _database='abril'
    _port='5432'
    _host='localhost'
    _conexion= None

    @classmethod
    def obtenerconexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion= bd.connect(
                    user=cls._user,
                    password=cls._password,
                    host=cls._host,
                    port=cls._port,
                    database=cls._database)
                log.debug(f"conectado correctamente")
                return cls._conexion                
            except Exception as e:
                log.error(f"error durante la conexion {e}")
                sys.exit()
            
        else:
            cls._conexion

if __name__=='__main__':
    Conexion.obtenerconexion()         """