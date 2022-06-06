nombre='juan'
edad=28
mensajeconformt='mi nombre es %s y edad %s'%(nombre,edad)
print(mensajeconformt)

persona=('karla','giraldo',500.00)
mensajeformateado='hola  %s %s, tu sueldo es %s'%persona
print(mensajeformateado)

mensajef='hola %s %s, tu sueldo es  %s'
print(mensajef%('karla','giraldo',500))

mensaje3='hola {} {} y tu sueldo es {}'.format(nombre,edad,500)
print(mensaje3)

mensaje4='nombre {0} tu edad es {1} el sueldo es {2}'.format(nombre,edad,900)
print(mensaje4)

mensaje5='nombre {1} tu edad es {0} el sueldo es {2}'.format(nombre,edad,900)
print(mensaje5)

mensaje6='mensaje 6 nombre {n} tu edad es {e} el sueldo es {s}'.format(n=nombre,e=edad,s=900)
print(mensaje6)

dici={'nombre':'ivan','edad':35,'sueldo':800}
mensaje7='mensajae 7 el nombre es {dico[nombre]} edad es {dico[edad]}'.format(dico=dici)
print(mensaje7)

""" formato recomendado """
mensaje8=f'mensaje 8 nombre {nombre} edad {edad}'
print(mensaje8)

""" multilicaion de str """

tupla=('valor', )
mensaje9=5*tupla
print(mensaje9)

print(4*[0])

"""  carateres de escape \ """
resulatado='hola \'  como andas'
print(resulatado)

resu='eliminacion del punto\\\\\\\b\b\b'
print(resu)

rs='c:\\nuevo\juan'
print(rs)

r=r'cadena con \n salto de linea'
print(r)
r=f'cadena con \n salto de linea'
print(r)

""" caracteres de unicode """
print('hola\u0020como andas')
print('Hola','\u2665')
""" juego de caracteres ascii """
print(chr(167))
""" manejo iteral b (bys)"""
mensa=b'Universidad python' 
print(mensa)
print(mensa[0]) # equivante en byts en decimal
print(chr(mensa[0])) #caracter respectivo

""" convertir de str a bys y biseverssa  el utf8 soporta  acentos"""
tring= 'programación en python '
print(f'string original {tring}')
print(tring.encode('UTF-8'))

""" convertir de string a bytes """
original='la cadena original progración'
print(original)
codificado=original.encode('UTF-8')
print(codificado)
#ahora de bytes a string
deco= codificado.decode('utf8')
print(deco)
print(  original==deco)
""" eliminar caracteres al inico de una  cadena  """
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:',titulo)

gt=' 1*** GlobalMentoring.com.mx *** '
print('cadena',gt,len(gt))
hj=gt.strip()
print(hj,len(hj))