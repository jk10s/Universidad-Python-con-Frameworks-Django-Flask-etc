from multiprocessing.spawn import import_main_path
from empleado import Empleado

class Gerente(Empleado):

    def __init__(self, nombre,sueldo, departamento) -> None:
        super().__init__(nombre,sueldo)
        self.departamento=departamento

    def __str__(self) -> str:
        return f'gerente y departamento {self.departamento} {super().__str__()}'