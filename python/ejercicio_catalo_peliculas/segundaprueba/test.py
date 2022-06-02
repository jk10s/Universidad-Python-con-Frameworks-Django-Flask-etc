from dominio.pelicula import Pelicula
from servicio.catalogo import Catalogo as jc

opcion=None
while opcion != 4:
    print(f'Menu'.center(50,'-'))
    print(f'1. para agregar peliculas')
    print(f'2. para listar peliculas')
    print(f'3. para eliminar catalogos')
    print(f'4. para borrar catalogos')

    opcion=int(input('elija una opcion (1-4) '))
    if opcion==1:
        peli=input('escriba una pelicula  ')
        pelicul=Pelicula(peli)
        jc.agregar(pelicul)
        
    if opcion==2:
        jc.listar()

    if opcion==3:
        jc.eliminar()

else:
    print(f'error asasas')