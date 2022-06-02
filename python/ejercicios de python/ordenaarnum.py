""" listauno=[12,45,567,34]
print(max(listauno))
numerosorden= sorted(listauno,key=lambda n: n % 5,reverse=True)

print(numerosorden) """
lista1=['red','blue','yellow']
lista2=['white', 'blank', 'narange', 'red','blue']
 
""" for i in lista1:
    for x in lista2:
        if i==x:
            print(i) 

conju2= set(lista1)
conju= set(lista2)
resul= conju.difference(conju2)
print(resul)"""