matriz=[[10,20],[36,98,78],[1,2,3,4]]

""" funcion de  matriz listas en listas """

print(matriz[1][0])
print(matriz[2][0])

lista_lista=[[3004,2005,30003,4004],[8,9,10,11,12,13],[0,1,2]]
lista_lista.sort(key=len)
print(lista_lista)
""" ordenar listas co la funcion  sorted """
nombre1=['andresogomezcru','xiomara','karla','pedro', 'zperanza']
nombre1=sorted(nombre1,reverse=True) #orden decendennte
print(nombre1)
nombre1=sorted(nombre1) #orden acendente
print(nombre1)

nombre1=sorted(nombre1,key=len)
print(nombre1)
nombre1=reversed(nombre1)
print(list(nombre1))

