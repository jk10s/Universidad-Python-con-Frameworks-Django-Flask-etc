""" print(dir(__builtins__))#ver todas las funcones qeu tiene incorporado python
help(zip) """

numero=[1,2,3]
letras=['a','b','c']
mezcla=zip(numero,letras)
identificadores=321,322,323,324,325
conjunto={6,4,0,9,8,15,10}
print(mezcla)
print(list(mezcla))
print(tuple(mezcla))
print(tuple(zip(numero,letras,identificadores,conjunto)))

""" iterar en pararelo """


""" crear un dicionario con zip y dos iterables """
llaves = ['nombre','apellido', 'edad']
valores=['juan,','perez',23]
dicionarios=dict(zip(llaves,valores))
print(dicionarios)
""" actualizar un elemento de un diccionario """

llav=['edad']
nuevaedad=[29]
dicionarios.update(zip(llav,nuevaedad))
print(dicionarios)
