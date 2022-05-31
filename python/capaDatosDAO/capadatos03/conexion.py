from distutils.log import debug
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
    def obtenerconexioon(cls):
        if cls._conexion is None:
            try:
                cls._conexion=bd.connect(
                    user=cls._user,
                    password=cls._password,
                    host=cls._host,
                    database=cls._database,
                    port=cls._port)
                log.debug(f"conexion satisfactoria {cls._conexion}")
                return cls._conexion
            except Exception as e:

                log.debug(f"error en la conexion {cls._conexion}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenercursor(cls):
        if cls._cursor is None:
            try:

                cls._cursor= cls.obtenerconexioon().cursor() 
                log.debug(f"se abrio el cursor {cls._cursor}")
                return cls._cursor
            except Exception as e:

                log.debug(f"error del cursor{e}")
                sys.exit()
            
        else:
            return cls._cursor

if __name__=='__main__':
    Conexion.obtenerconexioon()
    Conexion.obtenercursor()