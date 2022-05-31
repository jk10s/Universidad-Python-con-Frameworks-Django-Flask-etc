
import psycopg2 as bd
from capadedatospersona import log
import sys

class Conexion:
    _user='admini'
    _password='1234'
    _host='localhost'
    _port='5432'
    _database='abril'
    _conexion=None
    _cursor=None

    @classmethod
    def obtenerconexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion= bd.connect(
                    user=cls._user,
                    password=cls._password,
                    port=cls._port,
                    host=cls._host,
                    database=cls._database
                )

                log.error(f"conectado exitosa {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.debug(f"este es un error de conexion {e}")
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def obtenercursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor= cls.obtenerconexion().cursor()                     

                log.error(f"conectado al cursor exitosa {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.debug(f"este es un error de apetura cursor {e}")
        else:
            return cls._cursor
    
if __name__=='__main__':
    Conexion.obtenerconexion()
    Conexion.obtenercursor()
