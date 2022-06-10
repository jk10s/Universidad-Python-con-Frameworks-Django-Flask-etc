from empleado import Empleado
from gerente import Gerente

def imprimir(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

objempleado= Empleado("juan",1200)
imprimir(objempleado)
gerente=Gerente("carlosjulio",129,"sitemas")

imprimir(gerente)
