class Producto:
    def __init__(self,codigo,nombre,precio):
        self._codigo= codigo
        self._nombre= nombre
        self._precio=precio

    @property
    def codigo(self):
        return self._codigo    
    
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        self._precio=valor

    def __str__(self):
        return 'Codigo:' + str(self._codigo) +',nombre'+self._nombre +',precio'+str(self._precio)

p1=Producto(1,"jkjkjkj",8)


print(p1)
p1.nombre="mundillocruel"

