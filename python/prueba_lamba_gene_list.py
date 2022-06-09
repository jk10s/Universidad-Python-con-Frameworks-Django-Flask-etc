# ejejmplo lambda
lambaa=lambda a,b :a+b
print(lambaa(1,1))
# ahora ejemplo de generadores

jk=(valor for valor in range(1,50))
print(next(jk))

numeros=range(10)
# listcomprehesion
listaco=[]
listaco=[numero*numero for numero in numeros if numero %2 == 0]
print(listaco)

gh=lambda a,b:a+b
print(gh(12,56))

d=(valor for valor in range(1,10))
print(next(d))
print(next(d))
print(next(d))

b=[1,2,3,4,5,6]

m=[valor for valor in b if valor%2==0 ]
print(type(m))