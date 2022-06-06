# contadorpositivos=0
# contadornegativos=0
# numero=None
# while numero != 0:
#     numero=int(input("ingrese numero"))
#     if numero <0:
#         contadornegativos+=1
#     elif numero>0:
#         contadorpositivos+=1
    
# print(contadornegativos)
# print(contadorpositivos)


# numero=int(input("digite el numero a multiplicar"))
# LIMITE = 12
# contador = 1
# while contador <= LIMITE:
#     resultado = contador * numero
#     print("{} x {} = {}".format(numero, contador, resultado))
#     contador = contador + 1


""" Dado un numero de N Números (Diferentes a Cero), realice un algoritmo que permita determinar
y dar como salida lo siguiente:
• # Mayor y # Menor encontrado en el numero
• Cantidad de Números Mayores a 50
• Cantidad de Números Negativos Encontrados
• Promedio de los Positivos Encontrados """
numero=1
mayor50=[]
negativos=[]
positivos=[]
total=[]
while numero != 0:
    numero=int(input("ingrese el numero "))
    total.append(numero)
    if numero>50:
        mayor50.append(numero)
    elif numero <0:
        negativos.append(numero)
    elif numero >0:
        positivos.append(numero)
    
print(f' el maximo es {max(total)} los mayores de 50 son {len(mayor50)} negativos{len(negativos)} promedio positivos {sum(positivos)/len(positivos)} ')

