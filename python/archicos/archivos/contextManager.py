class Manejofiles:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
    
    def __enter__(self):
        print('obtenr recurso'.center(50,'-'))
        self.nombre=open(self.nombre,'r')
        return self.nombre
    
    def __exit__(self,tipo_excepcion, valor_excepcion,traza_error):
        print('cerrams el recurso'.center('50,-'))
        if self.nombre:
            self.nombre.close()
