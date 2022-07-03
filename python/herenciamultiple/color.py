class Color:
    def __init__(self,color) -> None:
        self._color=color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    def __str__(self) -> str:
        return f'el color {self._color}'
objeto3=Color("yellow")
""" print(objeto3) """