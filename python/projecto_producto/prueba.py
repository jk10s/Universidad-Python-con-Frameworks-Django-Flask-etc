from orden import Orden
from Producto import Producto

producto1= Producto("camisa", 100.00)
producto2= Producto("falda", 300.00)
producto3= Producto("cachucha", 40.00)
producto4= Producto("short", 450.00)

productos1=[producto1, producto2]
productos2=[producto3, producto4]
orde1=Orden(productos1)
orde1.agregar_producto(producto3)
orde1.agregar_producto(producto4)
print(orde1)
print(orde1.calcular_total())
orden2=Orden(productos2)
print(orden2)
print(f'total orden2 {orden2.calcular_total()}')






""" 
class Prueba:
    def __init__(self,nombre) -> None:
        self.nombre=nombre

    def __str__(self) -> str:
        return {self.nombre}

objeto1=Prueba("hola")
print(objeto1.__str__()) """