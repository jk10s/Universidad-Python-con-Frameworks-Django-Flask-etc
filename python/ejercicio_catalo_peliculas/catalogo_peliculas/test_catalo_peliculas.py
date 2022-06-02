from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CataloPelicula as cp

opcion=None
while opcion !=4:
    try:

        print('opciones: ')
        print('1.agregar peliculas')
        print('2.listar peliculas')
        print('3.eliminar catalogo de peliculas')
        print('4.salir')

        opcion=int(input('escribe tu opcion(1-4): '))
        if opcion==1:
            nombre_pelicula= input('proporiciona el nombre de la pelicula ')
            pelicula=Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion==2:            
            cp.listar_pelicula()

        elif opcion==3:            
            cp.eliminar_pelicula()
            

    except Exception as e:
        print(f'ocurrio un eroor {e}')
        opcion=None
else:
    print('salimos del programa')