from capadedatospersona import log
from usurio_dao import Usuariodao
from usuario import Usuario
opcion= None
while opcion != 5:
    print("""
    opcinoes
    1) listar usurios
    2) agregar usuarios
    3) actualizar usuarios
    4) eliminar usuarios
    5) salir
    """)
    opcion=int(input("ingres una opcin valida"))
    if opcion == 1:
        usuarios=Usuariodao.seleccionar()
        for usurio in usuarios:
            log.info(usurio)
            
    elif opcion == 2:
        username_var=input("ingre el username")
        paswwor_var=input("ingre el password")
        usuarios=Usuario(username=username_var,password=paswwor_var)
        usuariosinsertar=Usuariodao.insertar(usuarios)
        log.debug(f"usuarios insertados {usuariosinsertar}")

    elif opcion == 3:
        j= int(input("ingrese el id a modificae"))
        username_var=input("ingre el nuevo username")
        paswwor_var=input("ingre la nueva password")
        persona1= Usuario(j, username=username_var,password=paswwor_var)
        peronasinsertadas=Usuariodao.actualizar(persona1)
        log.debug(f"perosnas actualizadas {peronasinsertadas}")

    elif opcion == 4:
        id_var=int(input("ingre elid a elminar"))  
        usuarios=Usuario(id_usuario=id_var,)
        usuariosinsertar=Usuariodao.eliminar(usuarios)
        log.debug(f"usuarios eliminados {usuariosinsertar}")
        
    else:
        print(f"saliendo de la aplicacion")
