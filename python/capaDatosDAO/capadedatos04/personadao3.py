from capadedatospersona import log
from persona import Persona
from conexion import Conexion 
class Personadao:
    _select='select * from persona'

    @classmethod
    def selecionar(cls):
        with Conexion.obtenercursor() as cursor:
            cursor.execute(cls._select)
            registros=cursor.fetchall()
            personas=[]
            for x in  registros:
                persona= Persona(x[0],x[1])
                personas.append(persona)
            return personas
if __name__=='__main__':
    d = Personadao.selecionar()
    for x in d:
        log.debug(x)