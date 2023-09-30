# _*_ coding: utf-8 _*_
import arcpy        #libreria de arcgis
import csv          #libreria para generar excel csv

#Permitir sobreescribir los archivos que ya existen (reemplazar)
arcpy.env.overwriteOutput = True

#archivos de entrada
parada_autobuses = r"C:\Users\dirinfo\PycharmProjects\facite-arcpy\recursos\Data\SanFrancisco.gdb\Bus_Stops"
censo = r"C:\Users\dirinfo\PycharmProjects\facite-arcpy\recursos\Data\SanFrancisco.gdb\CensusBlocks2010"
#archivos de salida (generados)
seleccion_paradas = r"C:\Users\dirinfo\PycharmProjects\facite-arcpy\recursos\Data\SanFrancisco.gdb\Seleccion"
buffer = r"C:\Users\dirinfo\PycharmProjects\facite-arcpy\recursos\Data\SanFrancisco.gdb\Buffer"
interseccion = r"C:\Users\dirinfo\PycharmProjects\facite-arcpy\recursos\Data\SanFrancisco.gdb\InterseccionCenso"

'''
#SELECCIONAR LAS PARADAS DE CAMION QUE COINCIDAN CON EL NAME 14 OB y el BUS_SIGNAG Lowell St.
arcpy.Select_analysis(parada_autobuses, seleccion_paradas,"NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
print "Seleccion Finalizada ✅"

#HACER BUFFER A LA SELECCION ANTERIOR DE 100 Metros
arcpy.Buffer_analysis(seleccion_paradas,buffer,"100 Meters")
print "Buffer Finalizado ✅"

#HACER LA INTERSECCION DE LA CAPA DE Census_Block con el resultado del Buffer
arcpy.Intersect_analysis([censo, buffer], interseccion)
print "Interseccion Finalizada ✅"
'''

interseccion_datos = {}    #diccionario en blanco para extraer la informacion

#Recorrer cada uno de los registros de la tabla de atributos de la capa de interseccion
#tomando unicamente los campos llamados POP10 (poblacion) y STOPID (codigo de parada camion)
with arcpy.da.SearchCursor(interseccion, ["POP10", "STOPID", "NAME"]) as cursor:
    #por cada fila en la tabla de atributos la agregamos al diccionario
    for fila in cursor:
        stop_id = fila[1]
        pop10 = fila[0]
        name = fila[2]
        #verificar si la parada de autobus ya existe en el diccionario
        if stop_id not in interseccion_datos.keys():
            #si no existe en el diccionario lo agregamos
            interseccion_datos[stop_id] = [pop10]
        else:
            #si ya estaba agregado en el diccionario entonces solo agregamos el pop10
            interseccion_datos[stop_id].append(pop10)

print "Informacion del Diccionario: "
print interseccion_datos








