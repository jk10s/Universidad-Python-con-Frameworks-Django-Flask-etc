class Manejode:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
    def __enter__(self):
        print('obtener el recurso'.center(50,'*'))
        self.nombre = open(self.nombre,'r')
        return self.nombre
    def __exit__(self, tipo_excepcion, valor_excepcion, trazo_error):
        print("ceramos el recurso")
        if self.nombre:
           self.nombre.close()