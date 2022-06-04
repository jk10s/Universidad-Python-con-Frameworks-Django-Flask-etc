class Cubo:
    def __init__(self,alto,ancho,pro) -> None:
        self.alto=alto
        self.ancho=ancho
        self.pro=pro

    def area(self):
        return self.alto*self.ancho * self.pro

ancho=int(input("escriba ancho del cubo "))
alto=int(input("escriba alto del cubo "))
pro=int(input("escriba la profuncidad del cubo "))

objeto1=Cubo(ancho,alto,pro)

print(f'el are del cubo es {objeto1.area()}')