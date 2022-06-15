suma=lambda a,b:a+b
print(suma(3,4))

lista=[1,2,4,5]

jh=[valor+1 for valor in lista]
print(jh)

listasdelista=[[1,2,3],[4,5,6],[7,8,9,10]]

lista_pares=[]
lista_pares=[valor for sub in listasdelista for valor in sub if valor%2==0]
print(lista_pares)  


def deco1(deco2):
    def deco3():
        print("esta es una prueba de ddecoradores")
        deco2()
    return deco3

@deco1
def suma():
    print("esta es la suma tio")

suma()

j=(range(5))
print(j)

def Generador():
    yield 1
    yield 2
    yield 3

g=Generador()
print(next(g))
print(next(g))
print(next(g))

for x in Generador():
    print(f'generador numero {x}')

desge=(valor for valor in range(5))
print(next(desge))
print(next(desge))
print(next(desge))
print(next(desge))

ll=0b10000
l=0x100000
lll=0b1000000
llll=0b1000000

print(ll,l,llll)

textoo='le bendado dice holá'
print(textoo.encode())
eter=b'le bendado dice hol\xc3\xa1'
print(eter.decode())