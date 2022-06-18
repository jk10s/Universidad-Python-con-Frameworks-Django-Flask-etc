estudiantes=[]

class EstudantesUni(object):
    def __init__(self,nombre,modelo,tipo) -> None:
        self.nombre=nombre
        self.modelo =modelo
        self.ipo =tipo

    def mostrar(self):
        print(f'este esun producto de respuesta{self.nombre}{self.modelo}')



def primero():
    print("este es el numero uno")
    nombreuno=input("escribe tu nombre")
    modelouno=int(input("escribe tu nombre"))
    tipouno=input("escribe tu nombre")
    objetoEstudianete = EstudantesUni(nombreuno,modelouno,tipouno)
    estudiantes.append(objetoEstudianete)


def segundo():
    print("este es el numero dos lista de estudiantes")
    for objetoEstudianete in estudiantes:
        objetoEstudianete.mostrar()

def main():
    while True:
        print("""programa para estudiantes
        escribe 1 para agregar un los dato de estudiante
        escribe 2 para listar todo los estudoantes
        escribe 3 para salir del programa
        
        """)
        numero=int(input("escribe el numero para escoger"))
        if numero == 1:
            primero()
        elif numero==2:
            segundo()


if __name__== '__main__':
    main()