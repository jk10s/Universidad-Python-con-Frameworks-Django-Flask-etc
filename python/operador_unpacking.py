
numeros=[1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep='*')

def sumar(a,b,c):
    print(a+b+c)


sumar(2,3,4)
sumar(*numeros)

""" extraer elgunas partes de un objeto iterrable """
milista=[1,2,3,4,5,6]



a, *b, c, d=milista
print(a,b,c,d)
listuno=[1,2,3]
listdos=[4,5,6]
listtres=listuno+listdos
print(listtres)
listcuatro=[listuno,listdos] #listas de listas
print(listcuatro)
listcinco=[*listuno, *listdos]
print(listcinco)


""" unpacking in dicionarios """
diccio={1:'juan',2:'pedro',3:'hector'}
dicdos={4:'rafa',5:'nata'}
listavacia=[]
for x in diccio.values():
    listavacia.append(x)
print(listavacia)
print([diccio.values()])

dicotres={**diccio, **dicdos}
print(dicotres)

""" contruir u alista apartir de un str """
# se empaque la lista por medio de la funion * o ** y se empaqueña con la funcion sep=''
lista=[*'hola mundo']
print(*lista, sep='')
hl='hola como andas'

jl=input("ingresa un nmero")
x=jl[0]+jl[4]
print(x)





""" espar=int(input('escriba el numero '))
if espar%2==0:
    if espar>0:
        print('es par positivo')
    else:
        print('es par negativo')
elif espar%2 ==1:
    if espar>0:
        print('es impar postivo')
    else:
        print('es impar negativo') """