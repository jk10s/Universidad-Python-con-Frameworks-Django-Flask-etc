from dominio.peli import Pelicula
from servicio.cata import Catalogo as jk

opcion= None
while opcion != 4:
    print("""*********menu**********
    1) agregar peliculas
    2) listar peliculas
    3) eliminar catalogo
    4) salir
    """)
    opcion=int(input('ingrese una opcion de 1 a 4 '))
    if opcion==1:
        pe=input('ingresa la pelicula ')
        pelicu=Pelicula(pe)
        jk.agregar(pelicu)
    if opcion==2:
        jk.listar()
else:
    print('Hasta pronto')