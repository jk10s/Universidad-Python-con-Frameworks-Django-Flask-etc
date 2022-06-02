from dominio.pelicula import Pelicula
import os

class Catalogo:
    ruta='/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/segundaprueba/te.txt'
    @classmethod
    def agregar(cls,peliculas):
        with open(cls.ruta,'a') as archivo:
            archivo.write(peliculas.nombre)
    @classmethod       
    def listar(cls):
        with open(cls.ruta,'r') as archivo:
            print(archivo.read())
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta)
        print('eliminacion correcta')


