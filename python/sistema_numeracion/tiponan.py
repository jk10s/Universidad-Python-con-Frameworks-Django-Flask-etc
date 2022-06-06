""" no es un numero, no es sencible a mayusculas not a numeber se trabaja con float o con decimal un topo puede ser resultado de operacion similar el de valores infinitos

no es numerico
no es sencible a mayusculas
es un tipo de dato numerico indefinido
se comprueba si es nan con la funcion math.sinan(varible a comprobarar)
"""
import math
from decimal import Decimal
a= float('NaN')
b= float(2.0)
print(a)
print(b)

print(math.isnan(a))
print(math.isnan(b))

g= Decimal