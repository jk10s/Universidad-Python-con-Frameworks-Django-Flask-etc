from color import Color
from poligono import Poligono

class Hija(Poligono,Color):
    def __init__(self, lado, color,puerta) -> None:
        Poligono.__init__(self, lado,lado)
        Color.__init__(self, color)
        self.puerta=puerta
    def mostrar(self):
        return f'area es {self.alto*self.ancho} con el color {self.color}'
    
    def __str__(self) -> str:
        return f'{Poligono.__str__(self)}, {Color.__str__(self)} y puertas {self.puerta}'
        pass
objeto1=Hija(5,"rojo","cuatro")
objeto1.alto=9
print(objeto1.mostrar())
print(objeto1)
