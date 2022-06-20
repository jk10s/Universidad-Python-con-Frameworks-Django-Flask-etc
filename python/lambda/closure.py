""" closure es una funcion qeu define a otra y la puede regresar """

# funcion eterno

def Operacion(a,b):
    def sumar():
        return a+b
    return  sumar
mifuncio=Operacion(5,2)
print(mifuncio())

""" llamer la funcion """

lan=lambda  a,b:a+b
print(lan(2,1))