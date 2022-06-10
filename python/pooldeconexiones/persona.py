class Persona:
    def __init__(self,nombre=None,edad=None):
        self.nombre=nombre
        self.edad=edad
    def __str__(self) -> str:
        return f"el nombre del tal y pacula es {self.nombre} y la edad es {self.edad}"
