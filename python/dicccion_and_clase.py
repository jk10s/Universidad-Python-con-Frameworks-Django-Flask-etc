""" loster=[1,2,3,5]
for x in loster:
    print(x)
dicionarios={"julio":111,"hector":2222}

for i in dicionarios:
    print(dicionarios[i])

hola=list(dicionarios.items())
print(hola)

for clave,valor in dicionarios.items():
    print(clave,":   ",valor)

hj=loster.pop()
print(hj)
loster.insert(5,99)
print(loster)

 """
class hola:
    def __init__(self,nombre,edad) -> None:
        self.edad=edad
        self.nombre=nombre
    def ostrar(self):
        return (f'el nombre es {self.nombre}')
    def __str__(self) -> str:
        return f'hola ninño de la ostia{self.nombre}'

objeto=hola("juan",26)
print(objeto.edad)