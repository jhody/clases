# Profundizando en el tipo str

# Dar formato a un str
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
# print(mensaje)

# Método print
print(nombre, edad, sueldo, sep=', ') #separador
#-----------------------------------------------------
# multiplicación str
resultado = 3*'Hola'
print(f'Resultado: {resultado}')

# multiplicación tuplas
resultado = 5*('Hola',10) # ('Hola',10,'Hola',10,....)
print(f'Resultado: {resultado}')

# multiplicación listas
resultado = 10*[0] # [0,0,0,0,0,0,0,0,0,0]
print(f'Resultado: {resultado}, largo: {len(resultado)}')

#-----------------------------------------------------------
# caracteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b' # elimina los 3 ultimos caracteres
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\\juan'
print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de línea' # se procesa el \n como un caracter normal
print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
print(f'Resultado: {resultado}')

#------------------------------------------

# caracteres unicode
print('Hola\u0020Mundo')
print('Notación simple:', '\u0041')
print('Notación extendida:','\U00000041')
print('Notación hexadecimal','\x41')
print('Corazón:','\u2665')
print('Cara sonriendo:','\U0001f600')
print('Serpiente:','\U0001F40D')

# Caracteres ascii
caracter = chr(65)
print('A mayúscula:', caracter)
caracter = chr(64)
print('Símbolo @:', caracter)
caracter = chr(97)
print('a minúscula:', caracter)

# caracteres bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1]) # imprime el código
print(chr(mensaje[1])) # imprime la letra

lista_caracteres = mensaje.split() # [b'Universidad',b'Python']
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8') # convertir a bytes
print('bytes codificado:', bytes) # b'Programaci\xc3\xb3n con Python'
# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)

# Ejemplo: leer archivo
# ------------------------
# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    # contenido = mensaje.read()
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)

# Ejemplo2
# -------------------------------
# Leer contenido online
import urllib
from urllib.request import urlopen

palabras = []
# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)

# funciones con cadena:
# ---------------------------------
# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print('No. veces Universidad: ', contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte a minúsculas un str
print(contenido.lower())

# buscamos la cadena python en el contenido
print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe Python?: ','Python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con: ',contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con:', contenido.lower().endswith('globalmentoring.com.mx'.lower()))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# Alinear cadenas
# ---------------------------
# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(10,'*'))
# print(len(titulo.center(50,'*')))
print(titulo.center(len(titulo)+10,'-'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10,'-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+10,'-'))


# Reemplazar contenido en un str
print(contenido.replace(' ','-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:',titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:',titulo)

# ---------------------------
# Unpacking - desempaquetado
valores = 1,2,3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

# Profundizando listas
# Listas son mutables
nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura María Gonzalo Ernesto'.split()
# Sumar listas
print(f'Sumar listas {nombres1 + nombres2}')
# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1: {nombres1}')

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')
# obtener el índice del primer elemento encontrado en una lista
# help(list.index)
print(f'Índice 4: {numeros1.index(4)}')

# Invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos de una lista
numeros1.sort()
print(f'Lista ordenada (ascendente): {numeros1}')
# Ordenar de manera descendente una lista
numeros1.sort(reverse=True)
print(f'Lista ordenada (descendente): {numeros1}')

# Obtener el valor min y max de una lista
print(f'Valor mínimo: {min(numeros1)}')
print(f'Valor máximo: {max(numeros1)}')

# Copiar los elementos de una lista
numeros2 = numeros1.copy() #copia referencia
# help(list.copy)
print(f'Misma referencia? {numeros1 is numeros2}')  # false
print(f'Mismo contenido? {numeros1 == numeros2}')   # true

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')  # false
print(f'Mismo contenido? {numeros1 == numeros2}')   # true

# slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')  # false
print(f'Mismo contenido? {numeros1 == numeros2}')   # true

# Multiplicación listas
lista_multiplicacion = 5*[[2, 5]] # [[2,5],[2,5],[2,5],[2,5],[2,5]] - tienen la misma referencia cada uno
print(lista_multiplicacion)
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')    # true
print(f'Mismo contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}')     # true
lista_multiplicacion[2].append(7)  # [[2,5,7],[2,5,7],[2,5,7],[2,5,7],[2,5,7]]  # se modifica todos
print(lista_multiplicacion)

# Matrices en Python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglón 0, Columna 0: {matriz[0][0]}')
print(f'Renglón 2, Columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

# SORT modifica la lista original
lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)  # q ordene por el largo de elementos de cada sublista
print(f'Ordenar lista: {lista_listas}')

# sorted built-in NO MODIFICA LA LISTA ORIGINAL
# help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
# ordenar de manera descendente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
# Ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1,key=len)
print(nombres1)
# built-in reversed
nombres1 = reversed(nombres1) # devuelve un iterado, por loq hay q convertir a lista
print(list(nombres1))

# * desempaquetar
numeros = [1,2,3]
print(numeros)
print(*numeros) # 1,2,3 Desempaquetar elementos
print(*numeros, sep=' - ') # 1 - 2 - 3

# para desempaquetar diccionarios se usa **
# -------------------------
# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)
# ------------------------------
# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
print(a,b,c,d)  # 1 [2,3,4] 5 6


# Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}') # [[1,2,3],[4,5,6]]
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}') # [1,2,3,4,5,6]

# Unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}') # {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}

# Construir una lista a partir de un str
lista = [*'HolaMundo'] # desempaquetar cadena
print(lista) # ['H','o','l',...]
print(*lista, sep=' ') # H o l a M u n d o

# FUNCION ZIP: Mezclar elementos de iterable a la par, tomando como base la cantidad menor de un iterable
# print(dir(__builtins__)) # listar funciones en python
# help(zip)
numeros = (1,2,3)
letras = ['a','b','c']
mezcla = zip(numeros, letras)
print(mezcla)
print(list(mezcla)) # [(1,'a'),(2,'b'),(3,'c')] lista de tupla
print(tuple(zip(numeros, letras))) # convertir a tupla: ((1,'a'),(2,'b'),(3,'c'))

numeros = (1,2,3)
letras = ['a','b','c','d']
indentificadores = 321, 322, 323, 324, 325 # es una tupla, no es necesario poner ()
conjunto = {6,4,0,9,8,15,10} # es un set
mezcla = zip(numeros, letras, indentificadores, conjunto)
# print(mezcla)
print(list(mezcla)) # [(1,'a',321,6),(2,'b',322,4),(3,'c',323,0)]
# print(tuple(zip(numeros, letras)))
# print(type(mezcla))

# iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

# unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)
print(f'Números: {numeros}, Letras: {letras}')

# ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3,2,4,1,0]
mezcla = zip(letras, numeros)
# Sin orden
print(tuple(mezcla)) # [('c',3),('d',2),('a',4),('e',1),('b',0)]
# ordenar por letra (primer iterable)
print(sorted(zip(letras, numeros))) # [('a',4),('b',0),('c',3),('d',2),('e',1)]

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores)) # convetir a diccionario
print(diccionario) # {'Nombre':'Juan','Apellido':'Perez','Edad':18}


# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad)) # {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)

# Produndizando en tuplas
#-----------------------------.ñ
# Declarar variables
a, b = 'Hola', 'Adios'
print(a,b)
# swap (intercambio)
a, b = b, a
print(a, b)

# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'Valor min: {min}, Valor max: {max}')

# Regresa la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')

# PROFUNDIZAR EN SET
#-----------------------
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1,2],[3,4]} # Dará error
conjunto = {'Juan', True, 18.0}
print(conjunto)
# Set vacío
# conjunto = {} genera un dict vacío, no un set
# print(type(conjunto))
# set vacío correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4]) # elimina duplicados
print(conjunto) # {8,4,5,7}

# Podemos agregar más elementos on incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto) # {4,5,100,7,8,300,200}
conjunto.update([20,30,40,40])
print(conjunto) # {4,5,7,8,200,20,30,100,40,300}

# Copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}') # true
print(f'Es la misma referencia? {conjunto is conjunto_copia}') # false

# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan','Karla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','María'}
# Todos con ojos_cafe y pelo rubio (Union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio)) # {'Karla','Marc0','Laura','Lorenzo'}
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# (intersetion) Sólo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio)) # {'Laura'}

# (difference) Pelo negro sin ojos cafe (no es conmutativa)
# las personas que se encuentran en el primer set pero NO en el segundo
print(pelo_negro.difference(ojos_cafe))

# (diferencia simétrica) Pelo negro u ojos cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set está contenido en otro (subset)
# revismos si los elementos del primer set están contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set están contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))

# Produndizando en DICCIONARIOS
#-----------------------------------
# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)

# Los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor1'} # error
# diccionario = {(1,2):'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
# print(diccionario['nombre'])

# Método get recupera una llave, y si no existe NO lanza excepción
# además podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombres','No se encontró la llave'))
print(diccionario)

# setdefault sí modifica el diccionario, además se agregar un valor por default
nombre = diccionario.setdefault('Nombres','Valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint, muestra de forma ordenada
from pprint import pprint as pp
# help(pp)
pp(diccionario, sort_dicts=False)


# Funciones Anidadas
# -------------------------------
def calculadora(a, b, operacion='sumar'):
    # 1. Definir Función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # 2. Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(5, 6)
calculadora(4, 3, operacion='restar')
# Alcance de Variables (scope)

var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    print(f'Variable global desde función: {var_global}')
    # Definición de variable local
    var_local = 'Variables local'
    print(f'Variable local desde función: {var_local}')

    def funcion_anidada():
        print(f'Variable local dentro función anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Var global fuera función: {var_global}')
# No es posible acceder a variables locales fuera
# del bloque donde se definieron
# print(f'Var local fuera función: {var_local}') # error