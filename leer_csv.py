# _*_ coding: utf-8 _*_
import csv
ubicacion_archivo = 'csv/data_estados.csv'
datos = {}
total_localidades = 0
with open(ubicacion_archivo, mode='r') as archivo:
    datos = csv.DictReader(archivo)

    # imprimir el diccionario de datos
    for estado in datos:
        if estado['CVE_ENT'] == "25" and estado['CVE_MUN'] == '005':
            print estado['NOM_ENT'] + " " + estado["NOM_MUN"] + " 🛣️ " + estado['NOM_LOC'] + " 📍 Coordenadas: (" + estado['LAT_DEC'] + "," + estado['LON_DEC'] + ")"
            total_localidades += 1

print "Total de Localidades del csv ƪ(˘⌣˘)ʃ: " + str(total_localidades)

