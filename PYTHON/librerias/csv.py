import csv
# Importa el módulo csv para leer y escribir archivos CSV

# Leer un archivo CSV línea por línea
with open('archivo.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Resultado (si el archivo contiene):
# nombre,edad
# Juan,30
# Ana,25
# ['nombre', 'edad']
# ['Juan', '30']
# ['Ana', '25']

# Leer CSV omitiendo el encabezado
with open('archivo.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # salta la primera fila
    for row in reader:
        print(row)
# Muestra solo los datos, sin el encabezado

# Escribir un archivo CSV
with open('salida.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nombre', 'edad'])
    writer.writerow(['Luis', 28])
# Crea un archivo CSV con encabezado y una fila

# Escribir varias filas a la vez
datos = [['nombre', 'edad'], ['Carlos', 35], ['Laura', 22]]
with open('salida.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(datos)
# Escribe todas las filas de una lista de listas

# Leer archivo CSV como diccionario
with open('archivo.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['nombre'], row['edad'])
# Resultado:
# Juan 30
# Ana 25

# Escribir CSV como diccionario
with open('salida.csv', mode='w', newline='') as f:
    campos = ['nombre', 'edad']
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerow({'nombre': 'Pedro', 'edad': 40})
# Crea un CSV con encabezado y una fila usando diccionarios

# Leer CSV con delimitador personalizado
with open('archivo_puntoycoma.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)
# Lee archivos donde los campos están separados por punto y coma (;)

# Limpiar espacios en blanco
with open('archivo.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        row = [campo.strip() for campo in row]
        print(row)
# Quita espacios extra al inicio y final de cada campo

# Detectar archivo CSV vacío
with open('archivo.csv', newline='') as f:
    reader = csv.reader(f)
    try:
        primera = next(reader)
        print('El archivo no está vacío.')
    except StopIteration:
        print('El archivo está vacío.')
# Detecta si el archivo tiene datos








