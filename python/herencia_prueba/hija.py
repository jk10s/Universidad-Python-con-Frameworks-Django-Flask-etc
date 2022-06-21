from padre import Padre

class Hija(Padre):
    def __init__(self, nombreu, edadu) -> None:
        Padre.__init__(self, nombreu, edadu)

    def resta(self):
        return f'la resta de las edad son{self.edad-12}'

  
objetouno = Hija (1,23)
print(objetouno.resta())
#print(objetouno)