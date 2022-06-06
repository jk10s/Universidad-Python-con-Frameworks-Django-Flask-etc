
listaEstudiantes = []


class Hola():
    def __init__(self,nombre,edad,tipo,cedula):
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
        self.cedula=cedula
    def entrega(self):
        print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.nombre, self.edad, self.tipo, self.cedula))

def registrarEstudiante():
    nombree = float(input("Ingrese nota 3: "))
    edade = float(input("Ingrese nota 3: "))
    tipoe = float(input("Ingrese nota 3: "))
    cedulae = float(input("Ingrese nota 3: "))

    objAlumno = Hola(nombree,edade,tipoe,cedulae)
    listaEstudiantes.append(objAlumno)

def listadoEstudiantes():
    
    print("Listado de Estudiantes\n")
    for objAlumno in listaEstudiantes:
        objAlumno.entrega()
   
def main():
        
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar Estudiante")
        print("2.- Mostrar Estudiantes")
        print("3.- Buscar Estudiante")
        print("4.- Modificar notas")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
     

if __name__== '__main__':
     main()
