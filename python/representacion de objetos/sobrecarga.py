
# from haversine import haversine, Unit

# lyon = (45.7597, 4.8422) # (lat, lon)
# paris = (48.8567, 2.3508)

# haversine(lyon, paris)

# convertidosr de temperarueas

# simulacion de sobrecarga de constructores de python
# otras forms de crear objetos
class Persona:
    def __init__(self,nombre,apellido) -> None:
        self.nombre=nombre
        self.apellido=apellido

    @classmethod
    def crear_persona(cls):
        return cls(None, 'None')
    @classmethod
    def crear_persona_valores(cls,nombre,apellido):
        return cls(nombre, apellido)

    def __str__(self) -> str:
        return f'nombre {self.nombre} apellido {self.apellido}'



persona1=Persona('juan','carlos')
print(persona1)
persona_vacio=Persona.crear_persona()
print(persona_vacio)
persona_valor=Persona.crear_persona_valores('juacarlos','aria')
print(persona_valor)
