import math
from tokenize import maybe
from decimal import Decimal
# a=10 #sistema decimal
# b= 0b1010 #sistema binario
# c=0o13
# d= 0x1223a
# e=0
# print(d)    
# j=int('10111',2)
# print(j)
# k=0b10111
# print(k)

# infini=float('inf')
# print(type(infini))
# print(infini)

# infini=float('-inf')
# print(type(infini))
# print(infini)

# infiniposi=math.inf
# print(infiniposi)
# print({math.isinf(infiniposi)})
# """ infinito negativo con math """
# infininega=-math.inf
# print(infiniposi)
# print({math.isinf(infininega)})
""" modulo decimal infinito """
decimalpositivo=Decimal('infinity')
print(decimalpositivo)
print({math.isinf(decimalpositivo)})

""" modulo decimal infinito negativo"""
decimalpositivo=Decimal('-infinity')
print(decimalpositivo)
print({math.isinf(decimalpositivo)})
