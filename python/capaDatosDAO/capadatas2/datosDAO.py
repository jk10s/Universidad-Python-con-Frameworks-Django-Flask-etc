from conwxion import *
from capadedatospersona import log
from persona import Persona

class Datosdao:
    _seleccionar='select * from persona'

    @classmethod
    def seleccionar(cls):
            with Conexion.obtenercursor() as cursor:
                cursor.execute(cls._seleccionar)
                registros =cursor.fetchall() 
                personas=[] 
                for x in registros:
                    persona=Persona(x[0],x[1]) 
                    personas.append(persona)          
                return personas

if __name__ == '__main__':
    personas=Datosdao.seleccionar()
    for persona in personas:
        log.debug(persona)
    
        