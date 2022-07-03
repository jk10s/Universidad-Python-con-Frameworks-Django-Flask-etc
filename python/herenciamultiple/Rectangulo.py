from poligono import Poligono
from color import Color

class Rectangulo(Poligono,Color):
    def __init__(self, ancho, alto, color) -> None:
        Poligono.__init__(self,ancho,alto)
        Color.__init__(self,color)
    
    def calculararea(self):
        return f'el area del rectangulo es {self.ancho* self.alto}'

    def __str__(self) -> str:
        return f'{Poligono.__str__(self)}'

print('creacionde objeto rectangulo'.center(50,'-'))
objeto5=Rectangulo(8,4,"white")
objeto5.alto=-5
print(objeto5.calculararea())
print(objeto5)