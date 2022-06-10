class Empleado:
    def __init__(self,nombre, sueldo) -> None:
        self.nombre=nombre
        self.sueldo=sueldo 

    def __str__(self) -> str:
        return f'empleado {self.nombre} sueldo {self.sueldo}'

    def mostrar(self):
        return self.__str__()