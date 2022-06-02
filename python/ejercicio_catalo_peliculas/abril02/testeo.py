from domino.peli import Pelicula
from servicio.cata import Catalogo as jk

trueno=None
while trueno != 4:
    print(""" menu
    !)agraga
    2)lista
    3)elina
    4)salir
    
    """)
    trueno=int(input("escribe un aopcion de 1-4"))
    if trueno==1:
        pe=input("ingresa l apelicula")
        pelicu=Pelicula(pe)
        jk.agregar(pelicu)
    if trueno==2:
        jk.listar()
else:
    print("no valido")
