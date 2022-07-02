from orden import Orden
from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadoras import Computadoras

teclado1=Teclado("hp","usb")
raton1=Raton("entradacinco","usbmause")
monitor1=Monitor("lg",15)
compu=Computadoras("sony", monitor1, teclado1, raton1)

teclado2=Teclado("haap","uaaasb")
raton2=Raton("entraaaadacinco","usbmaaaaause")
monitor2=Monitor("laaag",13335)
compu2=Computadoras("VAIO", monitor2, teclado2, raton2)

teclado3=Teclado("genuis","frusb")
raton3=Raton("marter","lopson")
monitor3=Monitor("huawei",89)
compu3=Computadoras("toshiba", monitor3, teclado3, raton3)

objetoitera=[compu, compu2]
orden1=Orden(objetoitera)

print(orden1)
orden1.agregar_computadora(compu3)
print(orden1)
