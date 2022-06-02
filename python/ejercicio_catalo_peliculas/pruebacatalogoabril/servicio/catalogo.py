import os

class Catalogo:
    rutta='/home/jk10s/Vídeos/ciclo 3 pCS/parque/python/pruebacatalogoabril/tyt.txt'
    
    @classmethod
    def agregarpeli(cls, pelicula):
        with open (cls.rutta, 'a' ) as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    @classmethod
    def listarpeli(cls):
        with open(cls.rutta, 'r')as archivo:
            print(f'catalogo de peliculas'.center(50,'*'))
            print(archivo.read())
    @classmethod
    def eliminarpeli(cls):
        os.remove(cls.rutta)
        print(f'se ha elimindao el archivo {cls.rutta}')


