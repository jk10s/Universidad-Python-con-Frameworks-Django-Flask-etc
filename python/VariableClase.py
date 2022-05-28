import statistics


class Miclase:
    varible_clase="esta es una varible de clase"
    def __init__(self,instancia) -> None:
        self.instancia=instancia
    
    def juan():
        print("hola animal")
        
    @staticmethod
    def metodoestatico():
        print(Miclase.varible_clase)
    @classmethod
    def metodo_clase(cls):
        print(cls.varible_clase)
    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodoestatico()


""" Miclase.metodoestatico()

print(Miclase.varible_clase)
objeto6=Miclase("el valor de la instancia")
print(objeto6.instancia)
print(objeto6.varible_clase) """

#Miclase.metodo_clase()
objeto1=Miclase("variable deinstacicciiia")
#objeto1.metodo_clase()
objeto1.metodo_instancia()