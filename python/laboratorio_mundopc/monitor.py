class Monitor:
    contador_monitor=0
    def __init__(self,marca,tamano) -> None:
      Monitor.contador_monitor += 1
      self.idMonitor=Monitor.contador_monitor
      self._marca=marca
      self._tamano=tamano
    
    @property
    def marca(self):
       return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self,tamano):
        self._tamano=tamano


    def __str__(self) -> str:
        return f'el id es {self.idMonitor} la markka {self.marca} y tamaño {self.tamano}'

if __name__=='__main__': 
    objeto1=Monitor("mdls",12)
    print(objeto1)