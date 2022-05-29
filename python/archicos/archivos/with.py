from contextManager import Manejofiles


with Manejofiles('/home/jk10s/Vídeos/ciclo 3 pCS/parque/frontend/archivos/prueba.txt') as archivo:
    print(archivo.read())


