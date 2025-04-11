```python
x = 10        # Entero (int)
y = 2.5       # Flotante (float)
nombre = "Ana" # Cadena de texto (str)
es_mayor = True # Booleano (bool)
print(type(x))       # <class 'int'>
print(type(nombre))  # <class 'str'>
a = 10
b = 3
print(a + b)  # 13
intentos += 1
print(a // b) # 3 (división entera)
print(a % b)  # 1 (módulo)
print(a ** b) # 1000 (potencia)
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")

contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1

for i in range(1, 6):
    print("Número:", i)

for num in range(1, 10):
    if num == 5:
        break  # Se detiene cuando num es 5
    print(num)

for num in range(1, 10):
    if num == 5:
        continue  # Salta la iteración cuando num es 5
    print(num)
```
#### For

```python
estudiantes = [
    {'nombre': 'Juan', 'edad': 20},
    {'nombre': 'Maria', 'edad': 22},
    {'nombre': 'JUAN', 'edad': 25},
    {'nombre': 'Carlos', 'edad': 23}
]

nombre = "juan"

encontrado = [est for est in estudiantes if est['nombre'].lower() == nombre.lower()]
print(encontrado)
```

#### Listas (list)
Las listas son estructuras mutables que almacenan múltiples valores.
```python
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # manzana
frutas.append("naranja")  # Agrega un elemento
print(frutas)
```
#### Tuplas (tuple)
Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
Las tuplas son mas rapidas para acceder a elementos individuales que las listas
```python
coordenadas = (10, 20)
print(coordenadas[0])  # 10
```
#### Diccionarios (dict)
```python
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"}
print(persona["nombre"])  # Juan
persona["edad"] = 31  # Modifica un valor
```
#### Funciones y excepciones
```python
def saludar(nombre):
    return "Hola, " + nombre

print(saludar("Carlos"))
```
#### Manejo de excepciones (try-except)
```python
try:
    x = int(input("Ingresa un número: "))
    print("El doble es:", x * 2)
except ValueError:
    print("Error: Ingresa un número válido.")
```
### Módulos y manejo de archivos
#### Importar módulos (import)
```python
import math
print(math.sqrt(16))  # 4.0
```
#### Manejo de archivos (open, read, write)
```python
# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!")

# Leer un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```
- os.path.exists
```python
es una función en Python que se usa para verificar si una ruta (archivo o directorio) existe en el sistema de archivos.
import os
os.path.exists(ruta)
os.path.isfile(ruta)
os.path.isdir(ruta)
```
##### strip()
eliminar los espacios en blanco u otros caracteres especificados al inicio y al final de una cadena
```python
texto = "   Hola mundo   "
print(texto.strip())  # "Hola mundo"

texto = "---Hola mundo---"
print(texto.strip("-"))  # "Hola mundo"

texto = "xxxyHola mundo yyyxx"
print(texto.strip("xy"))  # "Hola mundo "

```
Métodos relacionados:
- lstrip(): Elimina solo los caracteres del lado izquierdo (inicio).
- rstrip(): Elimina solo los caracteres del lado derecho (final).
```python
texto = "  Hola mundo  "
print(texto.lstrip())  # "Hola mundo  "
print(texto.rstrip())  # "  Hola mundo"

```
##### split()
divide una cadena en una lista de partes utilizando un separador especificado.
```python
texto = "Hola mundo Python"
partes = texto.split()  # Sin especificar separador, usa espacios
print(partes)  # ['Hola', 'mundo', 'Python']

texto = "manzana,naranja,plátano"
frutas = texto.split(",")
print(frutas)  # ['manzana', 'naranja', 'plátano']

texto = "uno-dos-tres-cuatro"
partes = texto.split("-", 2)
print(partes)  # ['uno', 'dos', 'tres-cuatro'] Aquí, maxsplit=2 hace solo dos divisiones.

texto = "Línea 1\nLínea 2\nLínea 3"
lineas = texto.split("\n")
print(lineas)  # ['Línea 1', 'Línea 2', 'Línea 3']

```
Método relacionado: rsplit()

 funciona igual que split(), pero empieza dividiendo desde la derecha.
```python
texto = "uno-dos-tres-cuatro"
partes = texto.rsplit("-", 2)
print(partes)  # ['uno-dos', 'tres', 'cuatro']

```
##### lower()
 convierte todos los caracteres de una cadena a minúsculas.
```python
texto = "Hola Mundo"
print(texto.lower())  # "hola mundo"

palabras = ["Hola", "MUNDO", "Python"]
palabras_min = [palabra.lower() for palabra in palabras]
print(palabras_min)  # ['hola', 'mundo', 'python']

```
Métodos relacionados:
- upper(): Convierte a mayúsculas.
- capitalize(): Convierte solo la primera letra en mayúscula.
- title(): Convierte la primera letra de cada palabra en mayúscula.
```python
texto = "bIENVENIDO a PYTHON"
print(texto.lower())      # "bienvenido a python"
print(texto.upper())      # "BIENVENIDO A PYTHON"
print(texto.capitalize()) # "Bienvenido a python"
print(texto.title())      # "Bienvenido A Python"
```
##### swapcase() → Invierte mayúsculas y minúsculas
```python
texto = "Hola Mundo"
print(texto.swapcase())  # "hOLA mUNDO"
```

##### random()
se usa para generar números aleatorios y seleccionar elementos al azar de secuencias como listas o cadenas
```python
import random
num = random.randint(1, 10)  # Número entero entre 1 y 10 (ambos incluidos)
print(num)

num = random.uniform(1, 10)  # Número decimal entre 1 y 10
print(num)

colores = ["rojo", "azul", "verde", "amarillo"]
color_aleatorio = random.choice(colores) #Seleccionar un elemento aleatorio de una lista
print(color_aleatorio)

numeros = [1, 2, 3, 4, 5]
seleccion = random.choices(numeros, k=3)  # Selecciona 3 números con repetición
print(seleccion)

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)  # Lista mezclada en un orden aleatorio

cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
mano = random.sample(cartas, 5)  # Selecciona 5 cartas sin repetición
print(mano)

```
##### str() → Convierte a cadena
```python
num = 123
cadena = str(num)
print(cadena)  # '123'
print(type(cadena))  # <class 'str'>
```
##### center(ancho, relleno) → Centra el texto
```python
texto = "Python"
print(texto.center(10, "-"))  # "--Python--"
```
##### ljust(ancho, relleno) → Alinea a la izquierda
```python
print(texto.ljust(10, "-"))  # "Python----"
```
##### rjust(ancho, relleno) → Alinea a la derecha
```python
print(texto.rjust(10, "-"))  # "----Python"
```
##### zfill(ancho) → Rellena con ceros a la izquierda
```python
numero = "42"
print(numero.zfill(5))  # "00042"
```
##### find
```python
texto = "Hola mundo"
print(texto.find("mundo"))  # 5
print(texto.find("Python"))  # -1 (No existe)
```
##### index(subcadena) → Igual que find(), pero lanza error si no encuentra
```python
print(texto.index("mundo"))  # 5
# print(texto.index("Python"))  # ❌ ValueError
```
##### count(subcadena) → Cuenta cuántas veces aparece
```python
print(texto.count("o"))  # 2
```
##### startswith(subcadena) → Verifica si inicia con una subcadena
```python
print(texto.startswith("Hola"))  # True
```
##### print(texto.endswith("mundo"))  # True
```python
print(texto.endswith("mundo"))  # True
```
##### replace(viejo, nuevo, cantidad)
```python
texto = "Python es genial"
print(texto.replace("Python", "Java"))  # "Java es genial"
```
##### partition(separador) → Divide en tres partes (antes, separador, después)
```python
print(texto.partition(","))  # ('manzana', ',', 'pera,plátano')
```
##### isalnum() → ¿Solo letras y números?
```python
print("Python123".isalnum())  # True
print("Python 123".isalnum())  # False (tiene espacio)
```
##### isalpha() → ¿Solo letras?
```python
print("Python".isalpha())  # True
print("Python123".isalpha())  # False
```
##### isdigit() → ¿Solo números?
```python
print("12345".isdigit())  # True
print("123a".isdigit())  # False
```
##### islower() → ¿Solo minúsculas?
```python
print("python".islower())  # True
print("Python".islower())  # False
```
##### isupper() → ¿Solo mayúsculas?
```python
print("PYTHON".isupper())  # True
print("Python".isupper())  # False
```
##### isspace() → ¿Solo espacios?
```python
print("   ".isspace())  # True
print("Hola mundo".isspace())  # False
```
##### join(iterable) → Une elementos de una lista con un separador
```python
palabras = ["Hola", "mundo"]
print(" ".join(palabras))  # "Hola mundo"
```
##### Repetición de cadena (*)
```python
print("Hola " * 3)  # "Hola Hola Hola "
```
##### range() 
```python
for i in range(5): # de 0 a 4
    print(i)

for i in range(2, 7): # del 2 al 6
    print(i)

for i in range(1, 10, 2): # de dos en dos: 1, 3,5,...
    print(i)

for i in range(10, 0, -2): # 10, 8, 6, 4, 2
print(i)

#Convertir range() en lista
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(2, 7)))     # [2, 3, 4, 5, 6]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]

suma = sum(range(1, 6))  # 1 + 2 + 3 + 4 + 5 = 15
print(suma)

#Generar índices en un for
nombres = ["Ana", "Juan", "Luis"]
for i in range(len(nombres)):
    print(f"Índice {i}: {nombres[i]}")
```
##### enumerate
 función que permite iterar sobre una secuencia (como una lista o una tupla) mientras se obtiene el índice y el valor de cada elemento
```python
frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

#Si queremos que los índices empiecen en 1 en lugar de 0:
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}: {fruta}")

# Modificar valores en una lista
numeros = [10, 20, 30, 40]

for i, num in enumerate(numeros):
    numeros[i] = num * 2  # Duplicar cada número

print(numeros)  # [20, 40, 60, 80]
```
##### Diferencia entre enumerate() y range(len())
Sin enumerate() (método tradicional):
```python
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")
```
Con enumerate() (más limpio y legible):
```python
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```
##### for con zip() (recorrer múltiples listas a la vez)
```python
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```
##### for con dict.items() (recorrer diccionarios)
```python
persona = {"nombre": "Juan", "edad": 28, "ciudad": "Lima"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

```
##### for con else (cuando no hay break)
```python
for i in range(5):
    print(i)
else:
    print("Bucle terminado sin interrupciones")

numeros = [1, 3, 5, 7, 9]
buscado = 4
for num in numeros:
    if num == buscado:
        print(f"Encontrado: {num}")
        break
else:
    print(f"{buscado} no está en la lista")

```
##### for con list comprehension (una sola línea)
```python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
```
##### for en una sola línea
```python
for i in range(3): print(i)
```
##### reversed()
```python
numeros = [1, 2, 3, 4, 5]
invertido = reversed(numeros)
print(list(invertido))  # [5, 4, 3, 2, 1]

# Invertir cadena
texto = "Python"
texto_invertido = "".join(reversed(texto))
print(texto_invertido)  # "nohtyP"

# tupla en orden inverso
numeros = (10, 20, 30, 40)
for num in reversed(numeros):
    print(num)

lista = [1, 2, 3, 4]
print(list(reversed(lista)))  # [4, 3, 2, 1]
print(lista[::-1])            # [4, 3, 2, 1] consume mas memoria

```
#### Ejemplo con end=" " (imprime en la misma línea)
```python
for i in range(1, 6):
    print(i, end=" ")  # Se imprimen en la misma línea con un espacio

# texto pegado
for i in range(1, 6):
    print(i, end="")

# Con guiones (end=" - ") → Separados con " - "
for i in range(1, 6):
    print(i, end=" - ") # 1 - 2 - 3 - 4 - 5 -

```

##### Map()
se usa para aplicar una función a cada elemento de un iterable (lista, tupla, conjunto, etc.), devolviendo un iterador con los resultados
```python
numeros = [1, 2, 3, 4, 5]
resultado = map(str, numeros)  # Convierte cada número en string
print(list(resultado))  # ['1', '2', '3', '4', '5']

numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x ** 2, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]

# multiplicar elementos de dos listas:

a = [1, 2, 3]
b = [4, 5, 6]
resultado = map(lambda x, y: x * y, a, b)
print(list(resultado))  # [4, 10, 18]

# Convertir nombres a mayúsculas
nombres = ["juan", "maria", "pedro"]
resultado = map(str.upper, nombres)
print(list(resultado))  # ['JUAN', 'MARIA', 'PEDRO']

# Usar map() con una función personalizada
def cuadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]

# Usar map() con str.split()
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = map(str.split, frases)
print(list(resultado))  
# [['Hola', 'mundo'], ['Python', 'es', 'genial'], ['Me', 'gusta', 'programar']]

# Usar map() con int()
numeros_str = ["1", "2", "3", "4"]
resultado = map(int, numeros_str)
print(list(resultado))  # [1, 2, 3, 4]

# Usar map() con len()
palabras = ["Python", "es", "genial"]
resultado = map(len, palabras)
print(list(resultado))  # [6, 2, 6]
```

##### lambda 
```python
doble = lambda x: x * 2
print(doble(5))  # 10

suma = lambda a, b: a + b
print(suma(3, 4))  # 7

multiplicar = lambda x, y: x * y
print(multiplicar(6, 7))  # 42

es_par = lambda x: x % 2 == 0
print(es_par(10))  # True
print(es_par(7))   # False

primera_letra = lambda palabra: palabra[0]
print(primera_letra("Python"))  # 'P'

```
#### filter()

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4, 6, 8, 10]

# filtra nombres que comienzan con A
nombres = ["Ana", "Pedro", "Andrea", "Luis", "Alberto"]
empiezan_con_a = filter(lambda nombre: nombre.startswith("A"), nombres)
print(list(empiezan_con_a))  # ['Ana', 'Andrea', 'Alberto']

# Filtrar números mayores a 5
numeros = [2, 5, 8, 1, 9, 3]
mayores_a_cinco = filter(lambda x: x > 5, numeros)
print(list(mayores_a_cinco))  # [8, 9]

# Filtrar palabras con más de 4 letras
palabras = ["sol", "luz", "computadora", "ratón", "teclado"]
largas = filter(lambda palabra: len(palabra) > 4, palabras)
print(list(largas))  # ['computadora', 'ratón', 'teclado']

# Filtrar valores None de una lista
valores = [10, None, 20, "", 30, 0, None, 40]
sin_nulos = filter(None, valores) # None en filter() elimina valores None, 0, "" y False.
print(list(sin_nulos))  # [10, 20, 30, 40]

numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6]
```
#### sorted()

```python
numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 5, 7, 9]

# Ordenar en forma descendente
numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros, reverse=True)
print(ordenados)  # [9, 7, 5, 2, 1]

# ordenar cadenas
nombres = ["Pedro", "Ana", "Luis", "Maria"]
ordenados = sorted(nombres)
print(ordenados)  # ['Ana', 'Luis', 'Maria', 'Pedro']

# Ordenar sin importar mayúsculas/minúsculas
nombres = ["Pedro", "ana", "Luis", "maria"]
ordenados = sorted(nombres, key=str.lower)
print(ordenados)  # ['ana', 'Luis', 'maria', 'Pedro']

# Ordenar listas de tuplas (Por un campo específico)
personas = [("Ana", 25), ("Luis", 30), ("Pedro", 22)]
ordenados = sorted(personas, key=lambda p: p[1])  # Ordena por edad
print(ordenados)
# [('Pedro', 22), ('Ana', 25), ('Luis', 30)]

# Ordenar diccionarios por un valor
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 92},
    {"nombre": "Pedro", "nota": 78}
]
ordenados = sorted(estudiantes, key=lambda est: est["nota"], reverse=True)
for est in ordenados:
    print(est["nombre"], est["nota"])
# Luis 92
# Ana 85
# Pedro 78

# Ordenar una lista de objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = [Persona("Ana", 25), Persona("Luis", 30), Persona("Pedro", 22)]
ordenados = sorted(personas, key=lambda p: p.edad)
for p in ordenados:
    print(p.nombre, p.edad)
# Pedro 22
# Ana 25
# Luis 30

```
#### Sort()
```python
numeros = [5, 2, 9, 1, 7]
numeros.sort()
print(numeros)  # [1, 2, 5, 7, 9]

numeros = [5, 2, 9, 1, 7]
numeros.sort(reverse=True)
print(numeros)  # [9, 7, 5, 2, 1]

nombres = ["Pedro", "Ana", "Luis", "Maria"]
nombres.sort()
print(nombres)  # ['Ana', 'Luis', 'Maria', 'Pedro']

nombres = ["Pedro", "ana", "Luis", "maria"]
nombres.sort(key=str.lower) # sin importar mayusculas o minusculas
print(nombres)  # ['ana', 'Luis', 'maria', 'Pedro']

personas = [("Ana", 25), ("Luis", 30), ("Pedro", 22)]
personas.sort(key=lambda p: p[1])  # Ordena por edad
print(personas)
# [('Pedro', 22), ('Ana', 25), ('Luis', 30)]

# ordenar diccionarios por un valor
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 92},
    {"nombre": "Pedro", "nota": 78}
]
estudiantes.sort(key=lambda est: est["nota"], reverse=True)
for est in estudiantes:
    print(est["nombre"], est["nota"])
# Luis 92
# Ana 85
# Pedro 78

```

#### reduce()
```python
from functools import reduce
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)  # 15

from functools import reduce
numeros = [2, 3, 4, 5]
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado)  # 120

from functools import reduce
numeros = [5, 9, 2, 8, 4]
mayor = reduce(lambda x, y: x if x > y else y, numeros)
print(mayor)  # 9

from functools import reduce
palabras = ["Hola", "mundo", "esto", "es", "Python"]
frase = reduce(lambda x, y: x + " " + y, palabras)
print(frase)  # "Hola mundo esto es Python"

from functools import reduce
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, numeros, 10)
print(resultado)  # 25
```

##### sum()
```python
numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros)
print(resultado)  # 15

numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros, 10)  # Empieza desde 10
print(resultado)  # 25

numeros = (10, 20, 30, 40)
resultado = sum(numeros)
print(resultado)  # 100

numeros = {1, 2, 3, 4, 5}
resultado = sum(numeros)
print(resultado)  # 15

notas = {"Juan": 85, "Ana": 92, "Luis": 78}
resultado = sum(notas.values())
print(resultado)  # 255

numeros = [10, -5, 20, -2, 30]
resultado = sum(x for x in numeros if x > 0)  # Sumar solo los positivos
print(resultado)  # 60

numeros = [1, 2, 3, 4, 5]
resultado = sum(x**2 for x in numeros)
print(resultado)  # 55
```
##### max()
```python
numeros = [10, 25, 30, 5, 100]
resultado = max(numeros)
print(resultado)  # 100

resultado = max(3, 8, 2, 10, 5)
print(resultado)  # 10

palabras = ["manzana", "pera", "kiwi", "sandía", "uva"]
resultado = max(palabras, key=len)
print(resultado)  # "manzana"

productos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Tablet", "precio": 500},
    {"nombre": "Celular", "precio": 1000}
]
producto_mas_caro = max(productos, key=lambda x: x["precio"])
print(producto_mas_caro)
# {'nombre': 'Celular', 'precio': 1000}

from datetime import datetime
fechas = [
    datetime(2023, 5, 17),
    datetime(2021, 8, 9),
    datetime(2024, 2, 25)
]
fecha_mas_reciente = max(fechas)
print(fecha_mas_reciente)  # 2024-02-25 00:00:00

datos = [("Ana", 90), ("Luis", 95), ("Juan", 88)]
mejor_estudiante = max(datos, key=lambda x: x[1])
print(mejor_estudiante)  # ("Luis", 95)

```


##### join()
```python
palabras = ["Hola", "mundo", "Python", "es", "genial"]
resultado = " ".join(palabras)
print(resultado)  # "Hola mundo Python es genial"

frutas = ["manzana", "pera", "uva"]
resultado = ", ".join(frutas)
print(resultado)  # "manzana, pera, uva"

texto = "Python"
resultado = "-".join(texto)
print(resultado)  # "P-y-t-h-o-n"

colores = ("rojo", "verde", "azul")
resultado = " | ".join(colores)
print(resultado)  # "rojo | verde | azul"

numeros = [1, 2, 3, 4, 5]
resultado = " - ".join(map(str, numeros))
print(resultado)  # "1 - 2 - 3 - 4 - 5"

datos = [
    ["Juan", "25", "Perú"],
    ["Ana", "30", "Argentina"],
    ["Luis", "22", "Chile"]
]
for fila in datos:
    print(",".join(fila))
#Juan,25,Perú
#Ana,30,Argentina
#Luis,22,Chile

diccionario = {'nombre':'Juan','apellido':'Perez','edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves:{llaves}, type:{type(llaves)}')
```
## LISTAS
```python
mi_lista = [1, 2, 3, 4, 5]  # Lista de enteros
otra_lista = ["a", "b", "c"]  # Lista de strings
mezclada = [1, "Hola", 3.5, True]  # Lista con diferentes tipos
vacia = []  # Lista vacía

mi_lista = [10, 20, 30, 40, 50]
print(mi_lista[0])  # 10 (Primer elemento)
print(mi_lista[-1])  # 50 (Último elemento)
print(mi_lista[2])  # 30 (Tercer elemento)

mi_lista = [1, 2, 3, 4, 5, 6, 7]
print(mi_lista[1:4])  # [2, 3, 4] (Desde el índice 1 hasta el 3)
print(mi_lista[:3])   # [1, 2, 3] (Desde el inicio hasta el índice 2)
print(mi_lista[3:])   # [4, 5, 6, 7] (Desde el índice 3 hasta el final)
print(mi_lista[::2])  # [1, 3, 5, 7] (Cada dos elementos)
print(mi_lista[::-1]) # [7, 6, 5, 4, 3, 2, 1] (Lista invertida)

mi_lista = [10, 20, 30]
mi_lista[1] = 25  # Modifica el segundo elemento
print(mi_lista)  # [10, 25, 30]

numeros = [1, 2, 3]

numeros.append(4)  # Agrega un elemento al final
numeros.insert(1, 99)  # Inserta 99 en la posición 1
numeros.remove(2)  # Elimina el primer 2 que encuentra
ultimo = numeros.pop()  # Elimina el último elemento y lo retorna
indice = numeros.index(99)  # Encuentra la posición de 99
conteo = numeros.count(1)  # Cuenta cuántas veces aparece 1
numeros.sort()  # Ordena la lista de menor a mayor
numeros.reverse()  # Invierte la lista
print(numeros)

a = [1, 2, 3]
b = [4, 5, 6]
nueva_lista = a + b  # Concatenar listas
print(nueva_lista)  # [1, 2, 3, 4, 5, 6]
a.extend(b)  # Agregar todos los elementos de b en a
print(a)  # [1, 2, 3, 4, 5, 6]

frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

frutas = ["manzana", "pera", "uva"]
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

# para transformar listas
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8]

# filtrar listas
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# comprensión de listas
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4]

# eliminar elementos de una lista:
mi_lista = [1, 2, 3, 4, 5]
del mi_lista[2]  # Elimina el tercer elemento
print(mi_lista)  # [1, 2, 4, 5]

mi_lista.remove(4)  # Elimina el valor 4
print(mi_lista)  # [1, 2, 5]

mi_lista.clear()  # Elimina todos los elementos
print(mi_lista)  # []

# Verificar si un elemento está en la lista
mi_lista = [1, 2, 3, 4, 5]
print(3 in mi_lista)  # True
print(10 in mi_lista)  # False

# copiar una lista correctamente:

original = [1, 2, 3]
copia = original[:]  # Método recomendado
otra_copia = original.copy()
print(copia)  # [1, 2, 3]
print(otra_copia)  # [1, 2, 3]

# Convertir otros tipos de datos en listas
cadena = "Hola"
lista_letras = list(cadena)  # ['H', 'o', 'l', 'a']
tupla = (1, 2, 3)
lista_desde_tupla = list(tupla)  # [1, 2, 3]

# Crear una lista de listas (Matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # 6 (Fila 1, Columna 2)

# generar listas con range
numeros = list(range(1, 6))
print(numeros)  # [1, 2, 3, 4, 5]

# listas con valores repetidos

repetidos = [0] * 5
print(repetidos)  # [0, 0, 0, 0, 0]

# Usar sorted() para ordenar sin modificar la lista
numeros = [3, 1, 4, 1, 5, 9]
ordenada = sorted(numeros)
print(ordenada)  # [1, 1, 3, 4, 5, 9]
descendente = sorted(numeros, reverse=True)
print(descendente)  # [9, 5, 4, 3, 1, 1]
```

## TUPLAS
son estructuras de datos inmutables, lo que significa que una vez creadas, no pueden modificarse. Son útiles cuando necesitas almacenar datos que no deben cambiar
```python
mi_tupla = (1, 2, 3, 4, 5)  # Tupla de enteros
otra_tupla = ("a", "b", "c")  # Tupla de strings
mezclada = (1, "Hola", 3.5, True)  # Tupla con diferentes tipos
vacia = ()  # Tupla vacía
una_tupla = (5,)  # Una tupla de un solo elemento (importante la coma)

mi_tupla = (10, 20, 30, 40, 50)
print(mi_tupla[0])  # 10 (Primer elemento)
print(mi_tupla[-1])  # 50 (Último elemento)
print(mi_tupla[2])  # 30 (Tercer elemento)

mi_tupla = (1, 2, 3, 4, 5, 6, 7)
print(mi_tupla[1:4])  # (2, 3, 4)
print(mi_tupla[:3])   # (1, 2, 3)
print(mi_tupla[3:])   # (4, 5, 6, 7)
print(mi_tupla[::2])  # (1, 3, 5, 7)
print(mi_tupla[::-1]) # (7, 6, 5, 4, 3, 2, 1)  # Tupla invertida

# desempaquetado de tuplas
tupla = (1, 2, 3)
a, b, c = tupla  # Asigna cada valor de la tupla a una variable
print(a, b, c)  # 1 2 3
# Uso con "*"
tupla2 = (10, 20, 30, 40, 50)
x, y, *resto = tupla2  # Captura los valores restantes en una lista
print(x, y, resto)  # 10 20 [30, 40, 50]

# iterar sobre una tupla
frutas = ("manzana", "pera", "uva")
for fruta in frutas:
    print(fruta)

frutas = ("manzana", "pera", "uva")
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

mi_tupla = (1, 2, 2, 3, 4, 2)
print(mi_tupla.count(2))  # 3 (Cuenta cuántas veces aparece el número 2)
print(mi_tupla.index(3))  # 3 (Encuentra el índice del valor 3)


tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nueva_tupla = tupla1 + tupla2
print(nueva_tupla)  # (1, 2, 3, 4, 5, 6)


mi_tupla = (1, 2, 3)
repetida = mi_tupla * 3
print(repetida)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

lista = [1, 2, 3, 4]
tupla = tuple(lista)
print(tupla)  # (1, 2, 3, 4)

mi_tupla = (1, 2, 3, 4, 5)
print(3 in mi_tupla)  # True
print(10 in mi_tupla)  # False

tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada[1][2])  # 6 (Fila 1, Columna 2)

mi_tupla = (1, 2, 3)
mi_lista = list(mi_tupla)
print(mi_lista)  # [1, 2, 3]

# ordenar
tupla = (3, 1, 4, 1, 5, 9)
ordenada = sorted(tupla)  # Devuelve una lista
print(ordenada)  # [1, 1, 3, 4, 5, 9]
descendente = sorted(tupla, reverse=True)
print(descendente)  # [9, 5, 4, 3, 1, 1]

tupla_ordenada = tuple(sorted(tupla))
print(tupla_ordenada)  # (1, 1, 3, 4, 5, 9)

tupla = (1, 2, 3, 4)
dobles = tuple(map(lambda x: x * 2, tupla))
print(dobles)  # (2, 4, 6, 8)

tupla = (1, 2, 3, 4, 5, 6)
pares = tuple(filter(lambda x: x % 2 == 0, tupla))
print(pares)  # (2, 4, 6)

# combinar tuplas
nombres = ("Ana", "Juan", "Carlos")
edades = (25, 30, 35)
combinado = tuple(zip(nombres, edades))
print(combinado)  # (('Ana', 25), ('Juan', 30), ('Carlos', 35))

#  Tuplas como Claves en un Diccionario
coordenadas = {
    (10, 20): "Punto A",
    (30, 40): "Punto B"
}
print(coordenadas[(10, 20)])  # "Punto A"

```

### Import
```python
import math  # Importa todo el módulo math
print(math.sqrt(25))  # 5.0
print(math.pi)  # 3.141592653589793

#usar un alias
import numpy as np  # Importamos numpy con un alias más corto
array = np.array([1, 2, 3, 4])
print(array)

# importar solo funciones específicas
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)  # 3.141592653589793

# importar todo
from math import *
print(sin(0))  # 0.0
print(factorial(5))  # 120

# Importar y Renombrar una Función
from math import factorial as fact
print(fact(5))  # 120

try:
    import numpy as np
except ImportError:
    print("Numpy no está instalado. Usa: pip install numpy")

# importar en tiempo de ejecución
modulo = __import__("math")
print(modulo.sqrt(36))  # 6.0

import importlib
modulo_math = importlib.import_module("math")
print(modulo_math.pow(2, 3))  # 8.0


```






