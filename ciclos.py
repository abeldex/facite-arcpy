# _*_ coding: utf-8 _*_
from random import randint

lista_aleatorios = []
#generar una lista con 100 numeros aleatorios
for i in range(1, 101, 1):
    aleatorio = randint(0, 1000)   #genera un numero aleatorio entre 0 y 1000
    lista_aleatorios.append(aleatorio)  #agregamos a la lista el aleatorio

#imprimir la lista de numeros generados
print lista_aleatorios

#buscar si existe el numero 100 en la lista
if lista_aleatorios.count(100) > 0:
    print "Si se encontro el 100 en la lista 👌"
else:
    print "No tuvimos suerte señor stark 🤦‍♂️"