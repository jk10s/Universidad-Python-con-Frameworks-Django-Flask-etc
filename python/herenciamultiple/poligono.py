
class Poligono:
    def __init__(self,alto,ancho) -> None:
        if self._validarValor(ancho):
            self._ancho=ancho
        else:
            self._ancho=0
            print(f'el valor {ancho} no es valido')
        if self._validarValor(alto):
            self._alto=alto
        else:
            self._alto=0                   
            print(f'el valor {alto} no es valido')
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,alto):
        if self._validarValor(alto):
            self._alto=alto
        else:
            print(f'el valor es erroneo{alto}')
    @property
    def ancho (self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        if self._validarValor(ancho):
            self._ancho=ancho
        else:
            print(f'el valor es erroneo{ancho}')

    def __str__(self) -> str:
        return f'figura polino alto {self._alto} ancho {self._ancho}'   
         
    def _validarValor(self,valor):
        return True if 0<valor<10 else False

""" objeto2=Poligono(7,3)
print(objeto2) """