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

# Funciones Anidadas
# -------------------------------------------
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
# print(f'Var local fuera función: {var_local}')

# Más de funciones anidadas y alcance de variables
def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'

    funcion_anidada()

    print(f'Valor variable local externa: {variable_local_externa}')
    # No es posible acceder a una variable local más interna
    # print(f'Valor variable local anidada: {variable_local_anidada}')

funcion_externa()

# Definimos variable global
contador = 0

def mostrar_contador():
    print(contador)


def modificar_contador(c):
    # Sin esta línea no se usa la variable global
    global contador
    contador = c

modificar_contador(5)
mostrar_contador()


# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la función
def sumar(a, b):
    return a + b

# 1. Asignar una función a una variable (no se usan paréntesis)
mi_funcion = sumar

# Verificar el tipo de variable
print(type(mi_funcion))

# Llamamos la función a través de la variable
resultado = mi_funcion(5, 8)
print(f'Resultado: {resultado}')

# Funciones lambda
# Son funciones anónimas, y son pequeñas (una línea de código)

# No es posible asignar una función a una variable
# mi_funcion = def sumar(a, b): return a + b

# Con una función lambda(anónima, sin nombre, y una sola línea de código)
# No se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero sí debe regresar una expresión
mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4,6)
print(f'Resultado sumar con función lambda: {resultado}')

# Función lambda que no recibe argumentos (debemos regresar una expresión válida)
mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'Llamar función lambda sin argumentos: {mi_funcion_lambda()}')

# Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}')

# Función lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}')

# Un closure es una función que defina a otra, y además la regresar
# la función anidada puede acceder a las variables locales definidas
# en la función principal o externa

# Función principal
# def operacion(a, b):
#     # 1. Definimos una función interna o anidada
#     def sumar():
#         return a + b
#
#     # 2. Retornar la función
#     return sumar

# Función principal
def operacion(a, b):
    # 1. Definimos una función lambda interna o anidada y la retornamos
    return lambda: a + b

mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')

# Llamar la función regresada al vuelo
print(f'Resultado de la función closure al vuelo: {operacion(2,3)()}')

# Decoradores con argumentos
# Un decorador es una función que recibe una función y regresa una función (al menos)
# Lo utilizamos para extender funcionalidad de una función
# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)
# a(b) -> c
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes desde la función_decorada_c')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después desde la función decorada_c')
        return resultado

    return funcion_decorada_c


@funcion_decorador_a
def sumar(a, b):
    # print(f'Resultado suma: {a + b}')
    return a + b

resultado = sumar(5, 6)
print(f'Resultado suma: {resultado}')

# GENERADORES 
# ----------------------------------------------------------------
# Generadores
# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función yield (producir) (no se usar return)
def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir más valores de los que produce el generador
# lanza un error de StopIteration
# print(next(gen))

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Número generado: {valor}')

# Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

# Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Número producido: {valor}')

# Consumir a demanda
generador = generador_numeros()
try:
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador {e}')

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresión valor generado: {valor}')
    except StopIteration as e:
        print('Se terminó de iterar el generador')
        break

# Expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función (sin paréntesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')


# Crear un string a partir de un generador creado a partir de una lista
lista = ['Karla','Gomez', 22]
contador = 0
# Definimos una función para incrementar el contador
def incremetar():
    global contador
    contador += 1
    return contador
# La primera para es el yield, la segunda es el for, entre paréntesis
generador = (f'{incremetar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista) # ['1. Karla','2. Gomez']
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')


# LIST COMPREHENSION
# ------------------------------
numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista Pares: {lista_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleción if condicion]
# La condición de if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista Pares con list comprehensions: {lista_pares}')


# Un ejemplo simila con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(f'Lista divisible entre 2 y 6: {pares}')

# Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# El mismo ejercicio usando list comprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero)
 for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor
                for sublista in lista_listas
                for valor in sublista]
print(f'lista simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor%2==0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

# Con list comprehensions, en una sola línea de código
# No es necesario separar las líneas, solo es para mejor lectura de código
lista_pares = []
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista
               if valor%2==0]
print(f'Lista pares: {lista_pares}')

# Palabras reservadas en Python (keywords)
import keyword

print('Palabras reservadas (keywords) en Python')
print(keyword.kwlist)

# Variable (no podemos utilizar keyword para el nombre de una variable)
# as = 'Hola'
# Función (no podemos utilizar keyword para el nombre de una función)
# def is():
#     pass

# Profundizando en programación orientada a objetos
# -------------------------------------------------------
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan','Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Atributo clase
print(persona1.contador_personas) # Atributo del objeto 1

# Un segundo objeto
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)

# Desde los objetos creados, accedemos al nuevo atributo de la clase
# Esto es posible por que los atributos de clase se comparten con todos los objetos
print(persona1.contador2)
print(persona2.contador2)

# Simulación de sobrecarga de constructores en python
# otras formas de crear objectos
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None) # llamar al método init

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(persona1)

persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)

persona_con_valores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(persona_con_valores)


class ConvertidorTemperatura:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alta: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alta: {fahrenheit}')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_f(15)
    print(f'15 C a F: {resultado:.2f}')
    resultado = ConvertidorTemperatura.f_c(10)
    print(f'10 F a C: {resultado:.2f}')

# Representación de objetos (str, repr, format)
# ----------------------------------------------
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'

    # str es más para el usuario final u otros sistemas
    # la implementación por default llama al método repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # format su implementación por default es str
    # se manda a llamar al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan','Perez')
# repr (!r)
print(f'Mi objeto persona1: {persona1!r}')
# str (de manera automática el método print llama al método str)
print(persona1)
# format
print(f'{persona1}')

# Ejemplo atributos publicos, protegidos, privados
class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('Valor público', 'Valor protegido', 'Valor privado')
# Acceso al valor publico
print(objeto.publico)
# Modificar el valor publico
objeto.publico = 'Modificando valor público'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clase hija
print(objeto._protegido)
# Modificando valor protegido (solo dentro misma clase o subclases)
objeto._protegido = 'Modificando valor protegido'
print(objeto._protegido)

# Accediendo al valor privado (solo dentro de la misma clase)
# Directamente no se puede acceder
#print(objeto.__privado)
# Pero, se convierte a objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# Incluso se puede modificar
objeto._MiClase__privado = 'Cambiando valor privado'
print(objeto._MiClase__privado)

# En conclusión, no se puede comparar con otros lenguajes
# como C++ o Java, ya que no es la misma funcionalidad
# ni las mismas limitantes
# Debemos ser programadores responsables y respetar las buenas prácticas
# Impuestas en Python
# En la mayoría de los casos es suficiente con usar un guión bajo
# para encapsular y ocultar el detalle de una clase si somos programadores responsables

# Orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Método padre')

class Hijo(Padre):
    # Se manda a llamar el método __init__ de la clase padre
    # siempre y cuando la clase hija no defina su propio metodo init

    # Definimos el metodo init
    def __init__(self):
        # De manera opcional podemos llamar al metodo __init__ de la clase padre (super)
        print('Inicializador hijo')
        super().__init__()

    # Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Método sobreescrito hijo')
        super().metodo()

# padre1 = Padre()
# padre1.metodo()
hijo1 = Hijo()
hijo1.metodo()

# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)


# Ejemplo de herencia simple
# ------------------------------------
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

# Lista sólo acepta números
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista de Enteros Ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

# Lista simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
#Lista enteros
lista_enteros = ListaEnteros([1, 3, 4, -15])
print(lista_enteros)
# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1, 10, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO (Method Resolution Order)
print(ListaEnterosOrdenada.__mro__)


# otro ejemplo:
class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Método clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')

    def metodo(self):
        print('Método clase2')

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')

    def metodo(self):
        print('Método clase3')

class Clase4(Clase2, Clase3):

    def metodo(self):
        print('Método clase4')

# Creamos objeto clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual método se ejecuta
clase4.metodo()

# isinstance
# ---------------------------------------------
print('Es entero?', isinstance(10, int))
print('Es cadena?', isinstance('hola', str))
print('Es lista ent ord?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista ent?', isinstance(lista_enteros_ordenada, ListaEnteros)) # true
print('Es lista ord?', isinstance(lista_enteros_ordenada, ListaOrdenada))   # true
print('Es lista simple?', isinstance(lista_enteros_ordenada, ListaSimple))  # true
print('Es object?', isinstance(lista_enteros_ordenada, object))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple)))

# Decoradores de Clase
# ----------------------------------------------------------
# Permiten transformar de manera programática nuestra clase
# Es similar a los decoradores de funciones (es metaprogramación)
import inspect


def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si
        # se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro: {parametro}')

    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresion Generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre, solo la firma
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls,'__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #     return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

persona1 = Persona('Juan','Perez', 28)
print(persona1)
pesona2 = Persona('Karla','Gomez', 30)
print(pesona2)
#Tiene los métodos de propiedad nombre, apellido, repr
print(dir(Persona))
# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)

# DATA CLASES: modulo q agrega cierta funcionalidad a clases
from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')

domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Juan','Perez', domicilio1)
print(f'{persona1!r}')
# Variable de clase
print(f'Variable clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variable con valores vacíos
persona_vacia = Persona('Karla','', None)
print(f'Persona vacía: {persona_vacia}')
# Revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan','Perez', Domicilio('Saturno', 15))
print(f'Objetos iguales?: {persona1 == persona2}')
# Agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion)
# Frozen = True
# coleccion[0].nombre='Juan Carlos'
# persona1.nombre = 'Juan Carlos'

# JSON
# ----------------------
# Leer archivo json
# json = JavaScript Object Notation
import urllib.request
import json

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)
# Imprimimos sólo los nombres de las personas
# json se convierte a listas y diccionarios de python
print('Nombres de las personas en el archivo json:')
for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])
# Accedemos al total de personas de archivo
print(f'Total de personas: {json_respuesta["total"]}')
# Accedemos al mensaje del archivo
print(f'Mensaje: {json_respuesta["mensaje"]}')

# OTRO EJEMPLO
import json
import urllib.request

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
# print(respuesta)
cuerpo_respuesta = respuesta.read()
#print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
# print(json_respuesta)
# Ejercicio 1. Acceder a la descripción del clima
# descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripción clima: {descripcion_clima}')
# Ejercicio 2. Mostrar la temperatura mínima y máxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura mínima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura máxima: {temp_max}')

# MENUS
# ---------------
from tkinter import ttk, Menu
# Configurar el menú principal

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()

def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    #tearoff = False para evitar que se separe el menú de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al menú de archivo
    submenu_archivo.add_command(label='Nuevo')
    # Agregar un separador
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al submenu
    submenu_ayuda.add_command(label='Acerca De')
    # Agregamos al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)

# hacer que no sea resizable la ventana
ventana.resizable(0,0)

# EJEMPLO LOGIN
# --------------------
import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)


    def _login(self):
        messagebox.showinfo('Datos Login',
            f'usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()

    