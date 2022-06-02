from dominio.pelicula import Pelicula
from servicio.catalogo import Catalogo as jc

opcion=None
while opcion != 4:
    print('Menu'.center(50,'-'))
    print('1. agregar peliculas')
    print('2. listar peliculas')
    print('3. eliminar catalogo')
    print('4. salir')

    opcion= int(input('elija la opcion del (1-4)'))

    if opcion== 1:
        pe=input('ingrese una pelicula  ')
        pelicu=Pelicula(pe)
        jc.agregar(pelicu)
    if opcion== 2:
        
        jc.listar()
    if opcion== 3:
        
        jc.eliminar()
else:
    print('saliendo del menu')