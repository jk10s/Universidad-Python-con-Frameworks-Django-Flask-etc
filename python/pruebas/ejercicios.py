""" elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10. """
from numpy import not_equal


# numero=int(input("por favor ingrese un numero"))

# for x in range(2,numero+1,2):
#     print(x)
#     if x == 10:
#         break

""" Genera un código que, dado un número, calcule la suma de los números pares menores al valor hasta el 0. El número se incluye en la suma sea o no par.
Ejemplo: Si el usuario ingresa 21 21+20+18+16+14+12+10+8+6+4+2 = 131
Si el usuario ingresa 6 6+4+2 = 12 """

numero=int(input("por favor ingrese un numero"))
suma=0
for x in range(numero,0,-2):
    suma=suma+x
print(suma)

""" Crear una solución informática que determine el valor a pagar por cada cliente de una empresa que factura servicio acorde a la siguiente tabla """