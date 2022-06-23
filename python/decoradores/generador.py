"""   generador  yield consumir"""                              

def generador():
    yield 1
    print("se reanuda la ejecucion ")
    yield 2
    yield 3
# consumimos el generador a demanda
gen=generador()
print(next(gen))
print(next(gen))
print(next(gen))

# recorrido por ciclo for  
for x in generador():
    print(f'este es u unciclo forx {x}')



def desgene():
    yield 1
    yield 2
    yield 3

for x in desgene():
    print(x)
z=desgene()
print(next(z))
print(next(z))
print(next(z))