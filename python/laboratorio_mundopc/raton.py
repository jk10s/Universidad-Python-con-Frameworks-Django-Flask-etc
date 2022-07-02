from dipositivoentrada import Dispositivo

class Raton(Dispositivo):
    contador_raton=0
    def __init__(self,tipoentrada, marca,) -> None:
        Raton.contador_raton += 1
        self.idraton= Raton.contador_raton
        super().__init__(tipoentrada, marca)

    def __str__(self) -> str:
        return f'el id es  {self.idraton}  {super().__str__()}'

if __name__=='__main__':    
    objetodispo=Dispositivo("entradauno","azus")
    print(objetodispo)

    objetoraton= Raton("entaradados","ferrari")
    print(objetoraton)