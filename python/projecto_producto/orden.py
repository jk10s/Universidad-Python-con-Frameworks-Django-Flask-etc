from Producto import *

class Orden:
    contador_orden=0

    def __init__(self,productos) -> None:
        Orden.contador_orden += 1
        self._idorden=Orden.contador_orden
        self._productos= list(productos)

    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total=0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '
        return f'Orden {self._idorden} \nproductos: {productos_str}'

if __name__== '__main__':
    prodcuto1=Producto("camisa",100.00)
    #print(prodcuto1)
    prodcuto2=Producto("pantalon",300.00)
    #print(prodcuto2)
    productos1=[prodcuto1, prodcuto2]
    orden1= Orden(productos1)
    print(orden1)