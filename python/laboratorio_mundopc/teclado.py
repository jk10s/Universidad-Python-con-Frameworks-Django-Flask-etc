from dipositivoentrada import Dispositivo

class Teclado(Dispositivo):
    contador_tecaldo=0
    def __init__(self,tipoentrada, marca) -> None:
        Teclado.contador_tecaldo += 1
        self.idraton= Teclado.contador_tecaldo
        super().__init__(tipoentrada, marca)
    def __str__(self) -> str:
        return f'el id es {self.idraton} {super().__str__()}'

if __name__=='__main__':        
    objeto3= Teclado("entradatres","lamboryiny")
    objeto4= Teclado("entradacuatro","maclarends")
    print(objeto3)
    print(objeto4)