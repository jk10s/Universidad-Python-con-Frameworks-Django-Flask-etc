from manejodearchivos import Manejode
with Manejode('python/archicos/archivolectura.txt') as archivos:
    print(archivos.read())