""" no e psosible asignar una funcion a una variale """
"""  
mi_fun= def sumar(a,b):
            return a+b """

# con una funcion lambda en una sola linea de codigo
# no se necesita usar parentisis para los paramtros
funcio=lambda a,b:a+b
print(funcio(2,3))


# funcion qu no recibe parametros
hg=lambda:f'funcion llamada sinn argunmentos'
print(hg())

# funcon lambda con parametros por defaul
labdefa=lambda a=2,b=3:a/b
print(labdefa())
# funcion lambda con argumentos cariasbles *arg y *kargs


mifun= lambda *args, **kwargs: len(args)+len(kwargs)
print(f'resultado argumentos variables: {mifun(1,2,3,4, a=1, b=2)}')

# funciones lambda cona argumento sy vvaribles y valore por 

mifu= lambda a,b,c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'resultado argumentos variables: {mifu(1,2,3,4,5,6, e=1, f=2)}')
practicalam=lambda a,b:a+b
print(practicalam(100,90))