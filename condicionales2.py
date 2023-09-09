# _*_ coding: utf-8 _*_
#solicitar una calificacion de un alumno entre el 0 y el 10
#y vamos a imprimir si aprobo o reprobo
try:
    calificacion = int( input('Ingrese una calificacion entre 0 y 10: ') )

    #si la calificacion se encuentra en los valores de 6 y 10 decimos que esta aprobado
    if calificacion >= 6 and calificacion <= 10 :
        print "Aprobado 😁👍"
    elif calificacion >= 0 and calificacion <= 5 :
        print "Reprobado 😢😖"
    else :
        print "la calificacion no esta entre calificacion entre 0 y 10 😒"
except Exception as error:
    print "Oh oh creo que ingresaste una letra 👀, te estoy pidiendo un numero"
    print "Problema: " + error.message
