class Person:
    def __init__(self, nombre) -> None:
        self.nombre= nombre
    def __add__(self,othero):
        #return self.nombre + othero.nombre
        return f'{self.nombre} {othero.nombre}'
obje=Person("juan")
obje2=Person("carlos")
print(obje+obje2)