
class Orden:
    contador_orden=0

    def __init__(self,computadoras) -> None:
        Orden.contador_orden += 1
        self.idorden=Orden.contador_orden
        self.computadoras= list(computadoras)
   

    def agregar_computadora(self,computadora):
        self.computadoras.append(computadora)
    

    def __str__(self) -> str:
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()        
        
        return f'''Orden {self.idorden}
        computadpras: {computadoras_str}         
        '''

