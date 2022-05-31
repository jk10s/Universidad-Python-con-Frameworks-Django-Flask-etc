from capadedatospersona import log

class Persona:
    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'''
            Nombre: {self._nombre},
            edad: {self._edad}
        '''
  
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return  self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    
if __name__== '__main__':
    persona1= Persona('juliokilo',12)
    log.debug(persona1)
    #simulacion de insert sin varios parametros
    persona1= Persona(nombre='juliok',edad=32)
    log.debug(persona1)
    #simulacionde eliminacion
    persona1= Persona(nombre='natalia')
    log.debug(persona1)
    
    
