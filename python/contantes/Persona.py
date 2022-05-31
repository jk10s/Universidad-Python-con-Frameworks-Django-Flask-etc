from mailbox import NoSuchMailboxError


class Persona:
    contador_persona = 0

    @classmethod
    def generarsiguiente(cls):
        cls.contador_persona+= 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        #Persona.contador_persona += 1
        #self.id_persona = Persona.contador_persona
        self.id_persona = Persona.generarsiguiente()
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Persona {self.id_persona}{self.nombre}{self.edad}'

objetoo = Persona('pedro',21)
print(objetoo)
objetoo2 = Persona('karla',11)
print(objetoo2)