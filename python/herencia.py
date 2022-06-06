

from mailbox import NoSuchMailboxError


class Persona(object):
    def __init__(self, nombre, edad) :
        self.nombre= nombre
        self.edad=edad
    def __str__(self) -> str:
        return f'persona es {self.nombre} edad {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad,suelo):
        super().__init__(nombre, edad)
        self.suelo=suelo
    def __str__(self) -> str:
        return f'{super().__str__()} y suelo {self.suelo}'
""" objeto1= Empleado("juan",200,"as")
print(objeto1.nombre,objeto1.edad, objeto1.suelo) """