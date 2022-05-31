from capadedatospersona import log

from conexion import *
from persona import *
class PersonaDAO:
    _seleccionar='select * from persona'
    _insertar="INSERT INTO persona(nombre,edad) VALUES('ingrid',77)"
    _actualizar="UPDATE SET persona nombre=%s edad) VALUES('ingrid',77)"
    _eliinar='DELETE from persona where nombre=%s'
    
    @classmethod
    def seleccionar(cls):
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._seleccionar)
                registros = cursor.fetchall()
                
                for registro in registros:
                    print(registro)
                    
                

if __name__ == '__main__':
    PersonaDAO.seleccionar()
