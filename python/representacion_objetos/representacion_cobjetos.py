# print(dir(object))

class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} persona( nombre:{self.nombre},edad:{self.edad})'
    
    # la implementacion esta orientado para usurios finales
    def __str__(self) -> str:   
        return f'{self.__class__.__name__ }: metodo str  nombre es {self.nombre}  y edad {self.edad}'
    def __format__(self, __format_spec: str) -> str:
        return f'{self.__class__.__name__} con el nombre  {self.nombre} y la edad {self.edad}'
persona1=Persona('juan',12)
print(f'el objeto personal {persona1}')
print(f'el objeto personal {persona1!r}')
print(persona1.__str__())
# que es iguak
print(persona1)
print(f'{persona1}')