from dominio.Pelicula import Pelicula
import os

class CataloPelicula:
    ruta_archivo='/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/catalogo_peliculas/peliculas.txt'

    @classmethod    
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo,'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    @classmethod    
    def listar_pelicula(cls):
        with open(cls.ruta_archivo, 'r') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())
    
    @classmethod    
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'eliminado correctamente {cls.ruta_archivo}')

    def __str__(self) -> str:
        return f''

if __name__=='__main__':
    pass