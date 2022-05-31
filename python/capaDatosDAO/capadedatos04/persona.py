class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    def __str__(self) -> str:
        return f"el nobre del fulano es {self.nombre} y la edad es {self.edad}"
