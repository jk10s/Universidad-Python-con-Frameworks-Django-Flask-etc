from teclado import Teclado
from raton import Raton
from monitor import Monitor
class Computadoras:
    contador_computadora=0
    def __init__(self,nombre,monitor,teclado,raton) -> None:
        Computadoras.contador_computadora += 1
        self._idordencompu=Computadoras.contador_computadora
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton    
    
    def __str__(self) -> str:
        return f'''
        {self._nombre}
        id {self._idordencompu}
        monitor {self._monitor}
        teclado {self._teclado}
        raton {self._raton}
        
        '''

if __name__=='__main__': 
    teclado1=Teclado("hp","usb")
    raton1=Raton("entradacinco","usbmause")
    monitor1=Monitor("lg",15)
    compu=Computadoras("sony", monitor1, teclado1, raton1)
    print(compu)