from capadedatospersona import log
from usuario import Usuario
from conexion import *
from cursorpool import Cursorpool


class Usuariodao:
    '''
    dao
    crud
    '''
    _select= 'select * from usuario order by id_usuario'
    _insert='insert into usuario(username,password)values(%s,%s)'
    _actualizar='update usuario set username=%s, password=%s where id_usuario=%s'
    _delete='delete from usuario where id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with Cursorpool() as cursor:
            log.debug(f"selcionando usurios ")
            cursor.execute(cls._select)
            registros= cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario=Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
    @classmethod
    def insertar(cls, usuario):
        with Cursorpool() as cursor:
            log.debug(f"usurio a insertar ")
            valores=(usuario.username, usuario.password)
            cursor.execute(cls._insert,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls, usuario):
        with Cursorpool() as cursor:
            log.debug(f"usurio a actualizar ")
            valores=(usuario.username, usuario.password,usuario.id_usuario)
            cursor.execute(cls._actualizar,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls, usuario):
        with Cursorpool() as cursor:
            log.debug(f"usurio a eliminar ")
            valores=(usuario.id_usuario,)
            cursor.execute(cls._delete, valores)
            return cursor.rowcount
    
if __name__=='__main__':

    # usuario1=Usuariodao.seleccionar()
    # for usuario in usuario1:
    #     log.debug(usuario)
    
    persona1= Usuario(2, username='pedro',password='wer')
    peronasinsertadas=Usuariodao.actualizar(persona1)
    log.debug(f"perosnas actualizadas {peronasinsertadas}")

    # persona1= Usuario(username='juako',password=109)
    # peronasinsertadas=Usuariodao.insertar(persona1)
    # log.debug(f"perosnas actualizadas {peronasinsertadas}")