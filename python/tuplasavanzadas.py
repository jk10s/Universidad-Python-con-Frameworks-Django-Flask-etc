""" declaracion de variables """
a,b='hola','adios'
print(a,b)
a,b=b,a
print(a,b)
def minmax(elementos):
    return min(elementos), max(elementos)

min,max=minmax([1,2,3,4,5,6])
print(min,max)