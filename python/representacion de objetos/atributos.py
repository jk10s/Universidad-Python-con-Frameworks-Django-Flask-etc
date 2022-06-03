class Persona:
    contador_persona=0
    def __init__(self,nombre,apellido) -> None:
        self.nombre=nombre
        self.apellido=apellido


persona1=Persona('cantiflas','rojas')
print(persona1.__dict__)

# crrear objeto vuelo

print(persona1.contador_persona)
persona1.contador_persona=10
print(persona1.contador_persona)
print(persona1.__dict__)
print(Persona.contador_persona)

# segundo objeto

persona2=Persona('karla','arias')
persona2.contador_persona=15
print(persona2.contador_persona)
print(persona2.__dict__)
print(Persona.contador_persona)

# asociar un atriibuto de clase vuelo
Persona.contador2=20
print(Persona.contador2)