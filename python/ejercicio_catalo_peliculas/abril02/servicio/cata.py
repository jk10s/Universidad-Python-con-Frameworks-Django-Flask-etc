class Catalogo:
    ruta='/home/jk10s/Vídeos/ciclo 3 pCS/parque/python/abril02/tres.txt'
    @classmethod
    def agregar(cls,pelicula):
        with open(cls.ruta,'a')as archivo:
            archivo.write(pelicula.nombre)
    @classmethod
    def listar(cls):
        with open(cls.ruta,'r')as archivo:
            print(archivo.read())
