file = open('python/archicos/archivolectura.txt', 'r')
""" file.write("/n esto  o es un abroma tio es \n")
file.write("esto deveria se otra linea")
 """
""" for x in file:
    print(x) """
print(file.readlines()[2])