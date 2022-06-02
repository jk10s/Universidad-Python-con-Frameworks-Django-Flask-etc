


class Pelicula:

    def __init__(self,nombre) -> None:
        self._nombre=nombre

    def __str__(self) -> str:
        return f'el nombre de l apelucila es {self._nombre}'
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

if __name__=='__main__':
    objetoeli=Pelicula("los vengadores")
    print(objetoeli)