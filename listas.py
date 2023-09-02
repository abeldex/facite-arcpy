# _*_ coding: utf-8 _*_

#definir una lista con los dias de la semana
dias_semana = ['martes', 'miercoles', 'jueves', 'viernes', 'sabado']
print dias_semana

#agregarle un nuevo elemento a la lista al final
dias_semana.append('domingo')
#agregar un nuevo elemento a la lista al inicio
dias_semana.insert(0, 'lunes')

print dias_semana

#agregar una tupla a nuestra lista
dias_semana.append( (1,2,3,4,5,6,7) )
print dias_semana

#borramos la tupla o el ultimo elemento de la lista
dias_semana.pop(-1)
#borramos el elemento con valor jueves de la lista
dias_semana.remove('jueves')

#ordenar la lista de manera ascendente
dias_semana.sort()
print dias_semana
#ordenar la lista de forma descendiente
dias_semana.sort(reverse=True)
print dias_semana
#cuenta cuantos elementos encontro en la lista con el valor proporcionado
total_lista = dias_semana.count('sabado')
print "El sabado se encontro " + str(total_lista) + " veces"
#nos dice el tamaño de la lista o el total de elementos de la lista
total = len(dias_semana)
print "La lista de semanas tiene " + str(total) + " elementos"
