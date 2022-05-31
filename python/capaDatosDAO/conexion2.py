import psycopg2 as bd
from capadedatospersona import log
import sys
class Conexion:
    _password='1234'
    _user='admini'
    _host='localhost'
    _port='5432'
    _database='abril'
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
                log.debug(f" la conexion ha sido satisfactoria")
                return cls._conexion
                
            except Exception as e:
                log.debug(f"error duranante la conexion {e}")
                sys.exit()
        else:
            return cls._conexion

if __name__=='__main__':
    Conexion.obtenerconexion()