class Padre:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
        
    def suma(self):
        return f'suma de edades es {self.edad+2}'
    
    def __str__(self) -> str:
        return f'{self.nombre}, {self.edad}'
        
objetu=Padre("carlos",12)
print(objetu.suma())