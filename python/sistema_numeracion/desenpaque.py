
from pickletools import read_int4


valores= 1,2,3
print(valores)
print(type(valores))
valor1, valor2, valor3=1,2,3
print(valor1,valor2,valor3)

valor4,_,valor6=1,22,3
print(valor4, _,valor6)

variable= None
if bool(variable):
    print(f'se considera veradera')
else:    
    print(f'se considera falsa')
