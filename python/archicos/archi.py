try:
    archivo = open('/home/jk10s/Vídeos/ciclo 3 pCS/parque/python/archicos/hola.txt','a')
    archivo.write("hola como andas")
except Exception as e:
    print("error")
finally:
    archivo.close()