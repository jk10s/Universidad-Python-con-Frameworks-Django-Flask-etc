print('hola\u0020como andas')
print('Hola','\u2665')
tring= 'programación en python '
print(f'string original {tring}')
print(tring.encode('UTF-8'))

original='la cadena original progración'
print(original)
codificado=original.encode('UTF-8')
print(codificado)

#ahora de bytes a string
deco= codificado.decode('utf8')
print(deco)
print(  original==deco)

cadenaori="por favor imprimir´"
enco=cadenaori.encode('utf8')
print(enco)

decorer=b'por favor imprimir\xc2\xb4'
dc=decorer.decode('utf8')
print(dc)

""" eliminar caracteres al inico de una  cadena  """
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena original:',titulo, len(titulo))
nombre='***juan carlos***'
print(nombre, len(nombre))
jk=nombre.strip('*')
print(jk)
print(jk, len(jk))
dicionarios={"julio":111,"hector":2222}

for i in dicionarios:
    print(dicionarios[i])
print(list(dicionarios.keys()))
b= 0b1010101011111 
print(b)
a=10 #sistema decimal
b= 0b1010 #sistema binario
c=0o13
d= 0x1223a
e=0
print(d)    
j=int('10111',2)
print(j)
k=0b10111
print(k)