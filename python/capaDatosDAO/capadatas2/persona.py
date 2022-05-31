from capadedatospersona import log
class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad= edad
    def __str__(self) -> str:
        return (f"""nombre del sujet0 {self.nombre} y la edad del sijeto es {self.edad}""")
