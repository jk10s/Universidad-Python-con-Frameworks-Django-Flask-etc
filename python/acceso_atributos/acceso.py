
class Miclase:
    def __init__(self,publico,protegido,privado) -> None:
        self.publico=publico
        self._protegido=protegido
        self.__privado=privado

objetos=Miclase('valor publico', 'valor protegido','valor privado')
print(objetos.publico)
objetos.publico='nuevo valor de la variable publico'
print(objetos.publico)
# aceso al valro protegido 
print(objetos._protegido)
objetos._protegido='nuevo valor de la variable protegido'
print(objetos._protegido)
# no se debe y no lo deja privado
# print(objetos.___privado)
# objetos.__privado='nuevo valor de la variable pricado'
# print(objetos.__privado)

""" los objetos privado no los deja llamar solo si se llama con _Miclase__nombreatributo """
print(objetos._Miclase__privado)

