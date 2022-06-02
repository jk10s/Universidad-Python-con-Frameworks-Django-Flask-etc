from domino.peliculas  import Peliculas
import os

class Archivo:
       
    ruta= '/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/pruebapeliculas/texto.txt'

    @classmethod
    def agregar(cls, peliculas):    
        with open(cls.ruta,'a') as archivo:
            archivo.write(f'{peliculas.nombre}\n')

    @classmethod
    def listar(cls):
        with open(cls.ruta,'r') as archivo:
            print(archivo.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta)
        print(f'archivo elimnado econ exito {cls.ruta}')
    
    