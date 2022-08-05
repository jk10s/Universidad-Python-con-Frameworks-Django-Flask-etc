# decoradire de clase
# permiten transformar de un amanera programda nuestra clase
# es sunulas alis decireaderes de funciones 

def decorador_repr(cls):
    print(f"recibimos el objeto de clase {cls}")

class Persona:
    def __init__(self,nombre,edad) -> None:
        self._nombre=nombre
        self._edad=edad
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    
    def __repr__(self) -> str:
        return f' Persona({self._nombre} {self._edad}) '