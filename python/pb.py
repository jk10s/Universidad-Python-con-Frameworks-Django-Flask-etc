class carro():
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad

    @property
    def nombre(self):
        return self.nombre
        
    @nombre.setter
    def nombre(self,nombre):
        self.nombre=nombre

    def mostrar(self):
        return "mi nombre es {} y mi edad es {}".format(self.nombre,self.edad)
    
objeto1=carro("juan",12)

print(objeto1.mostrar())