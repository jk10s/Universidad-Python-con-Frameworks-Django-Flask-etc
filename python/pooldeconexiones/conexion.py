from psycopg2 import pool
from capadedatospersona import log
import sys
class Conexion:
    _user='admini'
    _pass='1234'
    _database='abril'
    _port='5432'
    _localhost='localhost'
    _min=1
    _max=5
    _pool=None

    @classmethod
    def obtenerpoll(cls):
        if cls._pool is None:
            try:
                cls._pool= pool.SimpleConnectionPool(cls._min, cls._max,
                                                        user=cls._user,
                                                        password=cls._pass,
                                                        port=cls._port,
                                                        host=cls._localhost,
                                                        database=cls._database)
                log.debug(f"creacion del pool exitoso {cls._pool}")
                return cls._pool
            except Exception as e:
                log.debug(f"ocurrio un error de obtencion de pool {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenrconexion(cls):
        conexion=cls.obtenerpoll().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    @classmethod
    def liberarconexion(cls,conexion):
        cls.obtenerpoll().putconn(conexion)
        log.debug(f'Conexion liberada del pool: {conexion}')
    @classmethod
    def cerrarconexion(cls):
        cls.obtenerpoll().closeall()
        

if __name__=='__main__':
   conexion1= Conexion.obtenrconexion()
   Conexion.liberarconexion(conexion1)
   conexion2= Conexion.obtenrconexion()
#    conexion3= Conexion.obtenrconexion()
#    conexion4= Conexion.obtenrconexion()
#    conexion5= Conexion.obtenrconexion()