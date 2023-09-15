# _*_ coding: utf-8 _*_
#Como declarar una funcion (funcion que nos salude)
def saludar(): #funcion que no recibe ningun parametro (datos, informacion)
    print "Hola te saludo"
def pendiente():  #funcion que no hace nada
    pass          #sirve para que nuestra funcion no nos detecte error

#crear una funcion que adivine la edad en base a la fecha de nacimiento
def adivinar_edad( mes, anio, dia=5):
    #empezar a calcular cual es la edad
    actual = 2023
    mes_actual = 9 #septiembre
    edad = actual - anio
    #si el mes es mayor al mes actual entonces restamos uno a la edad
    if mes > mes_actual:
        edad = edad - 1

    print "La edad es : " + str(edad)


#crear una funcion que reciba parametros opcionales
def definir_sexualidad(genero="No binario"):
    print "Elejiste ser " + genero

#mandar llamar la funcion saludar
saludar()
pendiente()

#mandar llamar la funcion adivinar_edad
adivinar_edad( 4, 1988)

#mandar llamar la funcion definir_sexualidad con 2 valores diferentes y uno vacio
definir_sexualidad("Heterosexual")
definir_sexualidad("LGBQT+")
definir_sexualidad()


