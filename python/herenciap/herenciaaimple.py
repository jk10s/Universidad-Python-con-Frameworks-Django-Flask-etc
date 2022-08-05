from mimetypes import init


class Listasimple:
    def __init__(self,elementos) -> None:
        self._elementos=elementos
    
    def agregar(self,elemento):
        self._elementos.append(elemento)
    
    def __getitem__(self,indice):
        return self._elementos[indice]
    def orden(self):
        return self._elementos.sort()
    def __len__(self):
        return len(self._elementos)
    def __repr__(self):
        return f'{self.__class__.__name__} xxxxxx {self._elementos!r}'

class ListaOrdenada(Listasimple):
    def __init__(self, elementos) -> None:
        super().__init__(elementos)
        # ordenamos los elemnetos
        self.orden()
    def agregar(self,elemento):
        super().agregar(elemento)
        self.orden()

class enteros(Listasimple):
    def __init__(self, elementos) -> None:
        super().__init__(elementos)

    

listasimple=Listasimple([5,2,6,9])
print(listasimple.orden())
listaordenada=ListaOrdenada([6,3,2,6,8,9,4])
print(listaordenada)
listaordenada.agregar(-12)
print(listaordenada)
print(len(listaordenada))