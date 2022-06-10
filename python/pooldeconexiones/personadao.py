from capadedatospersona import *
from persona import *
from conexion import *
from cursorpool import Cursorpool

class Personadao:
    _select='select * from persona'
    _insertar='INSERT INTO persona(nombre,edad) VALUES(%s,%s)'
    _actualizar='UPDATE persona SET edad=%s WHERE nombre=%s'
    _elimiinar='delete from persona where nombre=%s'

    @classmethod
    def selecionar(cls):
        with Cursorpool() as cursor:
            cursor.execute(cls._select)
            registros= cursor.fetchall()
            personas=[]
            for x in registros:
                persona=Persona(x[0],x[1])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls, persona):
        with Cursorpool() as cursor:
            valores=(persona.nombre,persona.edad)
            cursor.execute(cls._insertar, valores)
            log.debug(f'Persona  insertada: {persona}')
            return cursor.rowcount
    @classmethod
    def actualizar(cls, persona):
        with Cursorpool() as cursor:
            valores=(persona.edad,persona.nombre)
            cursor.execute(cls._actualizar, valores)
            log.debug(f'Persona  actualizada: {persona}')
            return cursor.rowcount
    @classmethod
    def eliminar(cls, persona):
        with Cursorpool() as cursor:
            valores=(persona.nombre,)
            cursor.execute(cls._elimiinar, valores)
            log.debug(f'Persona  eliminada: {persona}')
            return cursor.rowcount

if __name__=='__main__':

    persona1=Personadao.selecionar()
    for persona in persona1:
        log.debug(persona)

    # persona1= Persona(nombre='albina',edad=12)
    # peronasinsertadas=Personadao.insertar(persona1)
    # log.debug(f"perosnas insertadas{peronasinsertadas}")

    # persona1= Persona('victor',edad=1)
    # peronasinsertadas=Personadao.actualizar(persona1)
    # log.debug(f"perosnas actualizadas {peronasinsertadas}")
    
    # persona1= Persona(nombre='albina')
    # peronasinsertadas=Personadao.eliminar(persona1)
    # log.debug(f"perosnas eliminadas {peronasinsertadas}")



   

