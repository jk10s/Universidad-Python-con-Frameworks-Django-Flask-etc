from statistics import multimode

from attr import asdict


multicacion=(valor*valor+3 for valor in range(1,4))
print(multicacion)
print(next(multicacion))
print(next(multicacion))
print(next(multicacion))
# print(next(multicacion))
multi=sum(valor*valor for valor in range(4))
print(f'valor es {multi}')