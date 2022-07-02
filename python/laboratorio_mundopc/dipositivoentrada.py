class Dispositivo:
    
    def __init__(self,tipoentrada,marca) -> None:
        self._marca= marca
        self._tipoentrada=tipoentrada
    
    def __str__(self) -> str:
        return f'la marca es {self._marca} y la entrada es {self._tipoentrada}'

