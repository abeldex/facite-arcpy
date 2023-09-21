#importar el archivo estados para poder utilizar la clase que se llama estados
#import clases.estados
from clases.estados import estados
import webbrowser

#vamos a crear nuestro primer estado, (ejemplo : sinaloa)
sinaloa = estados()
#vamos a asignarle valores a los atributos del estado de sinaloa
sinaloa.clave = 25
sinaloa.nombre = "SINALOA"
sinaloa.poblacion = 3027000

#ejecutar la funcion con la que obtenemos la poblacion del estado
sinaloa.obtener_poblacion()

#creamos otro estado pero ahora usando el contructor
durango = estados(34, 'DURANGO', 0, 0, 654876)
durango.obtener_poblacion()

#establecerle la ubucacion a sinaloa y durango y obtener el enlace de google maps
sinaloa.establecer_ubicacion('25.0', '-107.499998')
url = sinaloa.obtener_enlace_google_maps()
print url
#abrir el navegador automaticamente con el enlace
webbrowser.open(url)

durango.establecer_ubicacion("24.83333", "-104.83333")
webbrowser.open(durango.obtener_enlace_google_maps())
