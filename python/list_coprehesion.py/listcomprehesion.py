from cgi import print_arguments


numeros=range(10)
listapres=[]
for numero in numeros:
    if numero %2==0:
        listapres.append(numero*numero)


print(listapres)
""" hacemos lo mismo pero con list compresefuin """
listaco=[]
listaco=[numero*numero for numero in numeros if numero %2 == 0]
print(listaco)

pares =[numero for numero in range(1,51) if numero%2==0 if numero%6==0]
print(pares)


# lo mismo utlizando else

listaelse=[]
listaimpa=[]
for x in range(40):
    if x%2==0:
        listaelse.append(x)
    else:
        listaimpa.append(x)
print(f'lista par es {listaelse} y lista impar es {listaimpa}')

# la mismoa proconn lista de comprehesion

listaparrrr=[]
listaimparrr=[]

[listaparrrr.append(numero) if numero%2==0 else listaimparrr.append(numero) for numero in range(50)]
print(f'lista par es {listaparrrr} y lista impar es {listaimparrr}')

listasdelista=[[1,2,3],[4,5,6],[7,8,9,10]]
# convertimos la lista de listas en una misma

# listasimple=[valor for sublis in listasdelista for valor in sublis] 
# print(listasimple)

print([valor for sublis in listasdelista for valor in sublis] )


lista_pares=[]
for sublista in listasdelista:
    for valor in sublista:
        if valor %2==0:
            lista_pares.append(valor)

print(lista_pares)

lista_pares=[]
lista_pares=[valor for sub in listasdelista for valor in sub if valor%2==0]
print(lista_pares)