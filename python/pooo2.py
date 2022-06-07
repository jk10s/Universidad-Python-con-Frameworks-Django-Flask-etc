class Carro:
    def __init__(self,nombre,color,modelo):
        self._nombre=nombre
        self._color=color
        self._modelo=modelo
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre=valor

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,valor):
        self._modelo=valor       
    
    def __str__(self) -> str:
        return 'este es el nombre tio' +self._nombre+'y esl color es'+self._color
    

objeto1=Carro("jesus","negro","ksdf")

print(objeto1)

objeto1.nombre="carlos"

print(objeto1.nombre)