from itertools import count


try:
    archivo = open('/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/archivos/texto.txt','r')
    archivo2 = open('/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/archivos/prueba.txt','a')
    archivo2.write(archivo.read())
    
    """ contador=0
    for linea in archivo:
        contador += 1
        print(contador) """
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
    print("se cerro el archivo conrrectate")