from capadedatospersona import log
from conexion import Conexion
class Cursorpool:
    def __init__(self) -> None:
        self._conexion=None
        self._cursor=None
    
    def __enter__(self):
        log.debug(f"inicio del metodo with")
        self._conexion= Conexion.obtenrconexion()
        self._cursor= self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
            log.debug('Se ejecuta método __exit__')
            if valor_excepcion:
                self._conexion.rollback()
                log.error(f'Ocurrió una excepción, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
            else:
                self._conexion.commit()
                log.debug('Commit de la transacción')
            self._cursor.close()
            Conexion.liberarconexion(self._conexion)

if __name__=='__main__':
    with Cursorpool() as cursor:
        log.debug(f"dentro del bloque with")
        cursor.execute('select * from persona')
        log.debug(cursor.fetchall())