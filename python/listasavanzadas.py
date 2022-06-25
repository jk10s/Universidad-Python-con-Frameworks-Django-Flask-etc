nombre = ['nombre', 'juan' 'pedro']
nombre2= 'laura maria gonzalo ernesto'.split()
# print(nombre+nombre2)


nombre.extend(nombre2)
print(nombre)
listadenun=[1,2,3,4,5,6,7,8,9]
""" obtener el primer elemento de la lista """
print(listadenun[6])
print(f'el cuarto elemeto de la lista es {listadenun.index(4)}')

""" inverti el orden de un alsita """
listaordenada=[10,20,30,40,50]
listaordenada.reverse()
print(listaordenada)
""" ordenar los elmentos de una lista """
listades=[7,8,5,45,344,23,12]
listades.sort()
print(listades)
""" ********lista ordenenada decendente********** """
listadescendente=[100,2,3,67,89,54]
listadescendente.sort(reverse=True)
print(listadescendente)
""" obtenr el valo maximo de un alista y el valor minimo """
print(max(listadescendente))
print(min(listadescendente))
""" ******* copia de una lista """
listanueva=listadescendente.copy()
print(listanueva)


""" lista en listas  de multiplicaion """
listamul=2*[[2,5]]
print(listamul)
""" matrice den listas lista en listas """

