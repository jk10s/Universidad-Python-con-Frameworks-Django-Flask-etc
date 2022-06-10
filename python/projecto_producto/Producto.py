class Producto:
    contador_producto=0
    def __init__(self, nombre, precio) -> None:
        Producto.contador_producto += 1
        self._idproducto=Producto.contador_producto
        self._nombre=nombre
        self._precio=precio
    
    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'producto N°{self._idproducto} nombre: {self._nombre} precio: {self._precio}'
    
if __name__== '__main__':
    prodcuto1=Producto("camisa",100.00)
    print(prodcuto1)
    prodcuto2=Producto("pantalon",300.00)
    print(prodcuto2)
