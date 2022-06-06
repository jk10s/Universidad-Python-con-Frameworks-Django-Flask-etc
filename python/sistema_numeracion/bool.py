""" false= 0 vacio vacio dicionarios listas etc
y true= todo lo demas """

sentencia=True
while sentencia:
    print("ejecucion ciclo while")
    break
else:
    print("fin de ciclo")

texto='guzman'
texto2= texto.capitalize()
print(texto.capitalize())
print(f"texto {id(texto)}")
print(texto2)
numero='2'
j=int(numero)
print(type(j))
jk=['1','2','3','4']
print(('-').join(jk))

""" diccionarios con join """
dicionario={'julio':'1','carmen':'2'}
print(('*').join(dicionario.values()))

""" metodo split en str """

curso='java excel python'
print(curso.split(' '))

curso2='frontend,backend,fullstack'
print(curso2.split(','))


curso4='qqqqqqqqqqqqq,www,wwwqw,5656,5732'
print(len(curso4))
""" seperdor de mas split es el varible.spli(',',2) que significa qeu lo separe apartir de la coma solo los dos primeros """
curso3='java.excel.python.web3.solyity'
print(curso3.split('.',2))

lascosas="**lo, discutimós,nos,peliamos**"
print(lascosas.split(','))
print(lascosas.upper())
print(lascosas.lower())
print(lascosas.encode('utf8'))
print(lascosas.strip('*'))
jk=['1','2','3','4']
print(('-').join(jk))
kk='soñe,er,rt'
print(('*').join(kk))