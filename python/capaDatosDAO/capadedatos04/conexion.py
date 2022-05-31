import psycopg2 as bd
import sys
from capadedatospersona import log
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
                    host=cls._host,
                    database=cls._database,
                    port=cls._port
                )
                log.debug(f" venga tio te has conectado coreectamnete")
                return cls._conexion
            except Exception as e:
                log.debug(f"error en la conexion{e}")
                sys.exit()
        else:
            return cls._conexion        
    @classmethod
    def obtenercursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor= cls.obtenerconexion().cursor()
                log.debug(f" venga tio has bierto bien el cursor")
                return cls._cursor
            except Exception as e:
                log.debug(f"error de apertura cursor{e}")
                sys.exit()
        else:
            return cls._cursor        
if __name__=='__main__':
    Conexion.obtenerconexion()
    Conexion.obtenercursor()