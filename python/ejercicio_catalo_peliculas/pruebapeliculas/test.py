from domino.peliculas import Peliculas
from servicio.archivos import Archivo as cp

opcion=None
while opcion != 4:
    print("Menu".center(50,'-'))
    print('escoja las opcions acontinuacion(1-4')
    print('1.para agregar peliculas')
    print('2.para  listar peliculas')
    print('3.para borrar catalogo')
    print('4.para salir del munu')
    opcion = int(input('eliga la opcion 1-4' ))
    if opcion== 1:
        peli= input('esciba el nombre de la pelicula')
        pelicul=Peliculas(peli)
        cp.agregar(pelicul)
    if opcion== 2:        
        cp.listar()
    if opcion== 3:        
        cp.eliminar()
else:
    print('saliendo del menu')