def funcion1(funciona):
    def funcionc():
        print("hola")
        funciona()
    return funcionc

@funcion1
def cocaina():
    print("esto ea coco")

cocaina()

multi=(valor*valor for valor in range(1,6))
print(multi)
# genera=multi()
# print(next(multi))
# print(next(multi))
# print(next(multi))
# print(next(multi))

sumas=sum(x+1 for x in range(1,5))
print(sumas)

# podemi utlizar un lista o cualquier otro iterador

lista=['juan','carlos']
generador=(valor for valor in lista)
print(next(generador))
print(next(generador))

for x in lista:
    print(x)

# crear u strinf apartir de un generador creada a apratir de una lista

listas=['karla','oscar']
contador=0
def incrementar():
    global contador
    contador +=1
    return contador

generad=(f'{incrementar()}.{nombre}' for nombre in listas)

lt=list(generad)
print(lt)

hu=(',').join(lt)
print(hu)