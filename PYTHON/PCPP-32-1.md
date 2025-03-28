# Clase 1: Manipulación avanzada de excepciones en Python
#### Bloques try-except anidados
```python
try:
    x = int(input("Ingrese un número: "))  # Puede fallar si no ingresa un número
    try:
        resultado = 10 / x  # Puede fallar si x es 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Debe ingresar un número válido.")

```
#### Uso de try-except-else-finally
```python
try:
    archivo = open("datos.txt", "r")  # Puede fallar si el archivo no existe
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
else:
    print("Contenido leído correctamente.")
finally:
    print("Cerrando el programa.")

```
#### Creación de excepciones personalizadas
Podemos definir nuestras propias excepciones heredando de Exception.
```python
class EdadInvalidaError(Exception):
    def __init__(self, edad, mensaje="Edad no válida. Debe ser mayor de 18."):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

try:
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        raise EdadInvalidaError(edad)  # Lanza una excepción personalizada
except EdadInvalidaError as e:
    print(f"Error: {e}")

```
#### Registro de errores con logging 
El módulo logging permite registrar errores en un archivo para su análisis posterior.
```python
import logging

logging.basicConfig(filename="errores.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except Exception as e:
    logging.error(f"Ocurrió un error: {e}")
    print("Se ha registrado un error en el archivo 'errores.log'.")

```
Podemos configurar logging para registrar mensajes en la consola y en un archivo.
```python
import logging

# Configuración básica
logging.basicConfig(
    filename="app.log",  # Nombre del archivo donde se guardarán los logs
    level=logging.DEBUG,  # Niveles: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del mensaje
    datefmt="%Y-%m-%d %H:%M:%S"  # Formato de la fecha
)

logging.debug("Este es un mensaje de depuración.")
logging.info("Este es un mensaje informativo.")
logging.warning("Este es una advertencia.")
logging.error("Este es un error.")
logging.critical("Este es un mensaje crítico.")

```
Uso de logging en el manejo de excepciones
```python
import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ZeroDivisionError as e:
    logging.error(f"Error de división por cero: {e}")
    print("No se puede dividir por cero.")
except ValueError as e:
    logging.error(f"Error de tipo de dato: {e}")
    print("Debe ingresar un número válido.")
except Exception as e:
    logging.critical(f"Error inesperado: {e}")
    print("Ha ocurrido un error inesperado.")

```
Usando logging con funciones
```python
import logging

logging.basicConfig(
    filename="operaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f"División exitosa: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        logging.error(f"Intento de división por cero: {e}")
        return "Error: No se puede dividir por cero."

# Pruebas
print(dividir(10, 2))
print(dividir(10, 0))

```
Configurar múltiples handlers (consola y archivo)
Podemos usar varios handlers al mismo tiempo, por ejemplo, mostrar errores en consola y guardar todo en un archivo.
```python
import logging

# Crear el logger
logger = logging.getLogger("MultiLogger")
logger.setLevel(logging.DEBUG)

# Handler para la consola (solo muestra WARNING o superior)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

# Handler para el archivo (guarda todo desde DEBUG)
file_handler = logging.FileHandler("multi_logs.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Agregar ambos handlers al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Mensajes de prueba
logger.debug("Este mensaje solo se guardará en el archivo.")
logger.info("Este mensaje solo se guardará en el archivo.")
logger.warning("Advertencia que se muestra en consola y archivo.")
logger.error("Error visible en consola y archivo.")
logger.critical("Mensaje crítico visible en consola y archivo.")

```
#### RotatingFileHandler (Para limitar tamaño del archivo)
Si un archivo de logs crece demasiado, podemos hacer que se cree un nuevo archivo automáticamente cuando llegue a un tamaño límite.
```python
import logging
from logging.handlers import RotatingFileHandler

# Configurar el logger
logger = logging.getLogger("RotatingLogger")
logger.setLevel(logging.DEBUG)

# Handler con rotación de archivos
handler = RotatingFileHandler("rotating.log", maxBytes=500, backupCount=3)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(handler)

# Generar muchos logs para llenar el archivo
for i in range(100):
    logger.info(f"Mensaje {i}")

```
#### Resumen de handlers con logging
- StreamHandler ->    Muestra logs en la consola.
- FileHandler ->	Guarda logs en un archivo de texto.
- RotatingFileHandler ->	Divide los logs en varios archivos cuando el tamaño es grande.
- TimedRotatingFileHandler ->	Crea un nuevo archivo de logs cada cierto tiempo.
# threading 
```python
import threading

def tarea():
    print("¡Hola! Soy un hilo trabajando.")

# Crear un hilo
hilo = threading.Thread(target=tarea)

# Iniciar el hilo
hilo.start()

# Esperar a que termine
hilo.join()

print("Fin del programa.")
```
Crear múltiples hilos

 Cada hilo tiene un número y trabaja al mismo tiempo.
```python
import threading

def tarea(num):
    print(f"Hilo {num} está trabajando.")

hilos = []
for i in range(5):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos terminaron.")
```
(Usar Thread no devuelve nada)
```python
import threading

def tarea():
    return "Hola"

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()

print("No se puede capturar el resultado directamente 😞")

```
Usar ThreadPoolExecutor para manejar hilos fácilmente

- ThreadPoolExecutor facilita crear hilos sin start() ni join().
- executor.map(tarea, datos) ejecuta la función en paralelo.
```python
import concurrent.futures

def tarea(num):
    return f"Hilo {num} finalizó."

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    resultados = executor.map(tarea, range(5))

print(list(resultados))

```
Comunicación entre hilos con queue.Queue

```python
import threading
import queue

cola = queue.Queue()

def productor():
    for i in range(5):
        cola.put(i)
        print(f"Produje {i}")

def consumidor():
    while not cola.empty():
        item = cola.get()
        print(f"Consumí {item}")

hilo1 = threading.Thread(target=productor)
hilo2 = threading.Thread(target=consumidor)

hilo1.start()
hilo1.join()
hilo2.start()
hilo2.join()
```
Sincronización con Lock (Evitar problemas de acceso a una variable compartida)

- lock = threading.Lock() evita que dos hilos cambien contador al mismo tiempo.
- with lock: bloquea la variable para que solo un hilo la use a la vez.

```python
import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(1000000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(2)]

for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()

print(f"Contador final: {contador}")

```

threading.Event para coordinar hilos
```python
import threading
import time

evento = threading.Event()

def esperar_evento():
    print("Esperando evento...")
    evento.wait()
    print("Evento recibido!")

hilo = threading.Thread(target=esperar_evento)
hilo.start()

time.sleep(2)
evento.set()  # Activa el evento
hilo.join()

```
Crear una clase con hilos (Thread con class)
```python
import threading

class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self): # método q se ejecuta cuando se llama a start()
        print(f"Hilo {self.nombre} en ejecución.")

hilo1 = MiHilo("A")
hilo2 = MiHilo("B")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

```
Caso real: Descargas en paralelo con threading
```python
import threading
import requests

def descargar(url):
    respuesta = requests.get(url)
    print(f"Descargado {url} con {len(respuesta.content)} bytes.")

urls = ["https://example.com", "https://python.org", "https://github.com"]
hilos = [threading.Thread(target=descargar, args=(url,)) for url in urls]

for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()

print("Descargas finalizadas.")

```
### resumen final:
- Thread(target=función)	Crea un hilo para ejecutar una función
- start()	Inicia el hilo
- join()	Espera a que el hilo termine
- ThreadPoolExecutor	Maneja hilos fácilmente sin start() ni join()
- queue.Queue()	Permite compartir datos entre hilos
- Lock()	Evita que varios hilos modifiquen la misma variable al mismo tiempo
- Event()	Permite que un hilo espere a que otro haga algo
- class MiHilo(Thread)	Crear hilos con clases

# Clase 2: Módulo multiprocessing
El módulo multiprocessing permite ejecutar código en procesos independientes, aprovechando los múltiples núcleos del procesador.
#### Creando un Proceso Simple
```python
import multiprocessing
import time

def tarea():
    print("Iniciando proceso...")
    time.sleep(2)
    print("Proceso terminado.")

if __name__ == "__main__":
    proceso = multiprocessing.Process(target=tarea)
    proceso.start()  # Inicia el proceso
    proceso.join()   # Espera a que termine antes de continuar
    print("Fin del programa principal.")

```
#### Multiprocesamiento con Argumentos
```python
import multiprocessing

def saludar(nombre):
    print(f"Hola, {nombre}")

if __name__ == "__main__":
    proceso = multiprocessing.Process(target=saludar, args=("Carlos",))
    proceso.start()
    proceso.join()

```
#### Crear Múltiples Procesos
```python
import multiprocessing

def tarea(num):
    print(f"Proceso {num} ejecutándose")

if __name__ == "__main__":
    procesos = []
    for i in range(5):
        p = multiprocessing.Process(target=tarea, args=(i,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()  # Espera a que todos los procesos terminen

    print("Todos los procesos han finalizado.")

```
#### Comunicación entre Procesos con Queue
Como los procesos son independientes, comparten datos a través de multiprocessing.Queue.
```python
import multiprocessing

def trabajador(q):
    q.put("Mensaje desde el proceso hijo")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    proceso = multiprocessing.Process(target=trabajador, args=(queue,))
    proceso.start()
    print(queue.get())  # Recibe el mensaje del proceso hijo
    proceso.join()
# queue.put() envía datos y queue.get() los recibe.
```
#### Pool de Procesos
Cuando queremos ejecutar una función varias veces en procesos paralelos, usamos Pool.
```python
import multiprocessing
import time

def cuadrado(n):
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:# Se crea 4 procesos.
        resultados = pool.map(cuadrado, [1, 2, 3, 4, 5]) # Ejecuta la función en paralelo sobre cada elemento de la lista.
    print(resultados)

```
#### sando asyncio para Tareas Asíncronas

Ventajas de asyncio:
- ✔ Ideal para tareas que esperan respuestas (HTTP, bases de datos).
- ✔ No bloquea el programa mientras espera.
- ✔ Más eficiente en uso de recursos comparado con threading.
```python
import asyncio

async def tarea(nombre):
    for i in range(3):
        print(f"Tarea {nombre} - Iteración {i}")
        await asyncio.sleep(1)  # Simula una tarea sin bloquear

async def main():
    await asyncio.gather(tarea("A"), tarea("B"))

asyncio.run(main())

```
# Excepciones
#### Usando else y finally
```python
try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes ingresar un número válido.")
else:
    print(f"El resultado es {resultado}")  # Solo se ejecuta si no hay error
finally:
    print("Fin del programa.")  # Siempre se ejecuta

```
#### Lanzar Excepciones con raise
Podemos generar errores manualmente con raise:
```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print(f"Error: {e}")

```
# Clase 4: Programación Orientada a Objetos (POO) en Python
La Programación Orientada a Objetos (POO) es un paradigma que permite organizar el código en clases y objetos, facilitando la reutilización y el mantenimiento.
#### Encapsulamiento: Atributos Privados
Para proteger los atributos, se usa __ (doble guion bajo).
```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

    def depositar(self, cantidad):
        self.__saldo += cantidad

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.mostrar_saldo()
# print(cuenta.__saldo)  # Esto generará un error
# Los atributos privados no pueden ser accedidos directamente (__saldo).
```
#### Herencia
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")

mi_perro = Perro("Firulais")
mi_perro.hacer_sonido()

```
#### Polimorfismo
El polimorfismo permite usar un mismo método en diferentes clases.
```python
class Gato:
    def hacer_sonido(self):
        return "Miau"

class Vaca:
    def hacer_sonido(self):
        return "Muuu"

def imprimir_sonido(animal):
    print(animal.hacer_sonido())

gato = Gato()
vaca = Vaca()
imprimir_sonido(gato)
imprimir_sonido(vaca)

```
#### Métodos y Atributos de Clase (@classmethod y @staticmethod)
```python
class MiClase:
    contador = 0  # Atributo de clase

    @classmethod
    def incrementar(cls):
        cls.contador += 1

    @staticmethod
    def mensaje():
        print("Hola desde un método estático.")

MiClase.incrementar()
print(MiClase.contador)  # 1
MiClase.mensaje()
# @classmethod usa cls para modificar atributos de la clase.
# @staticmethod no necesita self ni cls.
```
# Clase 5: Decoradores en Python
Los decoradores en Python son funciones que modifican el comportamiento de otras funciones o métodos sin cambiar su código. Se utilizan para añadir funcionalidades como validaciones, logs o control de acceso
#### Creando un Decorador Simple
```python
def decorador(funcion):
    def nueva_funcion():
        print("Antes de ejecutar la función.")
        funcion()
        print("Después de ejecutar la función.")
    return nueva_funcion

@decorador
def saludo():
    print("Hola, mundo.")

saludo()

```
#### Decoradores con Parámetros en la Función
```python
def decorador(funcion):
    def nueva_funcion(nombre):
        print("Ejecutando función con argumento:", nombre)
        funcion(nombre)
        print("Finalizando función.")
    return nueva_funcion

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")

```
#### Decoradores con *args y **kwargs (Multiparámetros)
```python
def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Llamando a la función...")
        resultado = funcion(*args, **kwargs)
        print("Función ejecutada.")
        return resultado
    return nueva_funcion

@decorador
def sumar(a, b):
    return a + b

print(sumar(5, 3))

```
#### Decoradores con Parámetros
```python
def repetir(n):
    def decorador(funcion):
        def nueva_funcion(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return nueva_funcion
    return decorador

@repetir(3)
def hola():
    print("Hola!")

hola()

```
#### Usando functools.wraps para Mantener Información de la Función Original
Cuando usamos decoradores, la información de la función original se pierde. functools.wraps lo soluciona.
```python
import functools

def decorador(funcion):
    @functools.wraps(funcion)
    def nueva_funcion(*args, **kwargs):
        print("Ejecutando función decorada.")
        return funcion(*args, **kwargs)
    return nueva_funcion

@decorador
def ejemplo():
    """Esto es una función de ejemplo."""
    print("Hola, mundo.")

print(ejemplo.__name__)  # Sin functools: 'nueva_funcion', con functools: 'ejemplo'
print(ejemplo.__doc__)   # Mantiene la documentación original
# @functools.wraps(funcion) mantiene el nombre y docstring de la función decorada.
```
#### Decoradores Anidados
Podemos usar varios decoradores en una función.
```python
def decorador_1(funcion):
    def nueva_funcion():
        print("Decorador 1 antes.")
        funcion()
        print("Decorador 1 después.")
    return nueva_funcion

def decorador_2(funcion):
    def nueva_funcion():
        print("Decorador 2 antes.")
        funcion()
        print("Decorador 2 después.")
    return nueva_funcion

@decorador_1
@decorador_2
def hola():
    print("Hola!")

hola()
```
# Clase 6: Programación Funcional en Python
La programación funcional es un paradigma que trata las funciones como ciudadanos de primera clase. Python permite el uso de funciones puras, funciones de orden superior y expresiones lambda.
#### Funciones de Orden Superior
Las funciones de orden superior son aquellas que pueden recibir funciones como argumento o retornar funciones.
```python
def operar(funcion, a, b):
    return funcion(a, b)

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

print(operar(sumar, 5, 3))       # 8
print(operar(multiplicar, 5, 3)) # 15

```
#### Funciones Lambda (Funciones Anónimas)
Las funciones lambda permiten definir funciones en una sola línea sin usar def.
```python
doble = lambda x: x * 2
print(doble(5))  # 10
```
#### Ejemplo con múltiples parámetros
```python
suma = lambda a, b: a + b
print(suma(3, 4))  # 7

```
#### Uso en sorted()
```python
lista = [(1, "Manzana"), (3, "Banana"), (2, "Cereza")]
lista.sort(key=lambda x: x[0])
print(lista)  # Ordena por el primer elemento de la tupla

```
#### Funciones map(), filter() y reduce()
Python tiene funciones funcionales para procesar colecciones de datos sin usar bucles.
##### map() – Aplica una función a cada elemento
Sustituye bucles for al aplicar una función a cada elemento.
```python
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8]

```
##### filter() – Filtra elementos según una condición
Solo deja los números pares.
```python 
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]
```
##### reduce() – Reduce una lista a un solo valor
 Importante: reduce() está en functools.


```python 
from functools import reduce

numeros = [1, 2, 3, 4]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 10
# Suma todos los elementos de la lista.
``` 
#### Closures (Funciones que Recuerdan su Estado)
Las closures permiten que una función interna recuerde variables de su contexto.
```python 
def multiplicador(n):
    def multiplica(x):
        return x * n
    return multiplica

doble = multiplicador(2)
triple = multiplicador(3)

print(doble(5))  # 10
print(triple(5)) # 15
# multiplicador(2) retorna la función multiplica(x), recordando n = 2.
``` 

#### Recursión
``` python
# factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


``` 
# Clase 8: Módulos y Paquetes en Python
En esta clase aprenderás cómo organizar el código en módulos y paquetes, facilitando la reutilización y el mantenimiento en proyectos grandes
#### ¿Qué es un módulo en Python?
Un módulo es un archivo de Python (.py) que contiene funciones, clases o variables reutilizables.
#### Importación completa (import modulo)
``` python
import math
print(math.sqrt(16))  # 4.0

``` 
#### Importar solo funciones específicas (from modulo import función)
``` python
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)        # 3.141592653589793

```
#### Importar con alias (import modulo as alias) 
``` python
import math as m
print(m.sqrt(9))  # 3.0

``` 
#### Importar todo (from modulo import *) ❌ (No recomendado)
``` python
from math import *
print(sqrt(36))  # 6.0
#  No es recomendable porque puede generar conflictos con otros nombres de funciones.
``` 
#### Módulos Propios y __name__ == "__main__"
Python ejecuta el código de los módulos importados al momento de la importación, lo que puede ser un problema. Para evitarlo, usamos if __name__ == "__main__".
``` python
# modulo.py
def mensaje():
    print("Este es un mensaje desde modulo.py")

if __name__ == "__main__":
    mensaje()  # Esto solo se ejecuta si el archivo se ejecuta directamente

# main.py
import modulo  # No ejecuta `mensaje()` porque `__name__` no es "__main__"

``` 
####  ¿Qué es un paquete en Python?
Un paquete es una carpeta que contiene módulos y un archivo especial __init__.py (puede estar vacío).
```python
# mi_paquete/
#│── __init__.py
#│── operaciones.py
#│── mensajes.py

# Contenido de operaciones.py:
def suma(a, b):
    return a + b
# Contenido de mensajes.py:
def saludo():
    return "Hola desde mensajes"

# Uso del paquete en otro archivo (main.py):
from mi_paquete.operaciones import suma
from mi_paquete.mensajes import saludo

print(suma(5, 3))  # 8
print(saludo())    # Hola desde mensajes

# Desde Python 3.3, __init__.py puede estar vacío, pero sigue siendo recomendable incluirlo para definir inicializaciones del paquete.
``` 
#### Importar Paquetes desde Otras Rutas
Si el paquete no está en la misma carpeta, podemos agregar su ruta manualmente.
```python
import sys
sys.path.append("ruta/del/paquete")
import mi_paquete
# Esto permite importar paquetes desde cualquier ubicación del sistema.
``` 
####  Módulos Estándar
Python tiene muchos módulos listos para usar:
##### os (Sistema Operativo)
```python
import os
print(os.getcwd())  # Muestra el directorio actual
``` 
##### sys (Sistema y argumentos de línea de comandos)
```python
import sys
print(sys.argv)  # Muestra los argumentos pasados al script

```
##### random (Números Aleatorios)
```python
import random
print(random.randint(1, 10))  # Número aleatorio entre 1 y 10

```
##### datetime (Fechas y Horas)
```python
from datetime import datetime
print(datetime.now())  # Muestra la fecha y hora actual

```
# Clase 10: Manejo de Archivos en Python
En esta clase aprenderás cómo leer, escribir y manipular archivos en Python, un tema esencial para el examen PCPP-32-1.
#### Apertura y Cierre de Archivos (open())
modos de apertura:
- "r"	Leer (predeterminado)
- "w"	Escribir (borra contenido si existe)
- "a"	Añadir (escribe al final sin borrar)
- "r+"	Leer y escribir
- "w+"	Leer y escribir (borra contenido)
```python
archivo = open("ejemplo.txt", "w")  # Abre el archivo en modo escritura
archivo.write("Hola, este es un archivo de texto.\n")
archivo.close()  # Cierra el archivo
```
#### Leer Archivos (read(), readline(), readlines())
```python
# Leer todo el contenido (read())
archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
print(contenido)  # Muestra todo el contenido del archivo
archivo.close()

# Leer línea por línea (readline())
archivo = open("ejemplo.txt", "r")
print(archivo.readline())  # Lee la primera línea
archivo.close()

# Leer todas las líneas (readlines())
archivo = open("ejemplo.txt", "r")
lineas = archivo.readlines()  # Retorna una lista con las líneas
for linea in lineas:
    print(linea.strip())  # strip() elimina saltos de línea
archivo.close()
```
#### Escribir en Archivos (write())
Importante: Si el archivo ya existe, write() borra su contenido antes de escribir.
```python
archivo = open("ejemplo.txt", "w")
archivo.write("Este es un nuevo contenido.\n")
archivo.write("Segunda línea.\n")
archivo.close()

```
#### Agregar contenido (append)
Para añadir contenido sin borrar el existente, usamos "a".
```python
archivo = open("ejemplo.txt", "a")
archivo.write("Esta línea se agrega al final.\n")
archivo.close()
```
#### Usando with open() (Mejor Práctica)
Ventaja: No es necesario cerrar el archivo manualmente.
```python
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # El archivo se cierra automáticamente

```
#### Archivos JSON (json module)
```python
# Escribir un JSON en un archivo
import json

datos = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Lima"
}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)  # `indent` mejora la visualización

# Leer un JSON desde un archivo
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)  # {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Lima'}

# Archivos CSV (csv module)
# Ejemplo de un archivo CSV:
# nombre,edad,ciudad
# Carlos,30,Lima
# Ana,25,Arequipa
# Luis,40,Cusco
```
#### Escribir en un CSV
```python
import csv

datos = [
    ["nombre", "edad", "ciudad"],
    ["Carlos", 30, "Lima"],
    ["Ana", 25, "Arequipa"],
    ["Luis", 40, "Cusco"]
]

with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)  # Escribir múltiples filas

```
#### Leer un CSV
```python
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Muestra cada fila como una lista

```
# Clase 21: Expresiones Regulares en Python (re) 
Las expresiones regulares (regex) son secuencias de caracteres que forman un patrón de búsqueda en un texto. Se utilizan para encontrar, validar o reemplazar datos dentro de cadenas de texto.
Para usarlas en Python, se usa el módulo re.
```python
import re
```
#### Métodos Principales del Módulo re
```python
# Buscar una palabra en una cadena
import re
texto = "Hola, bienvenido a Python"
patron = "Python"
resultado = re.search(patron, texto) # Busca la palabra "Python" en texto.
if resultado:
    print("Patrón encontrado en la posición:", resultado.start()) # resultado.start(): Devuelve la posición donde se encontró el patrón.
else:
    print("Patrón no encontrado")

# Coincidencia Exacta con re.match()
# re.match() solo busca al inicio de la cadena.
# Coincidir solo si la palabra está al inicio:
import re
texto = "Python es genial"
patron = "Python"
resultado = re.match(patron, texto)
if resultado:
    print("El texto comienza con 'Python'")
else:
    print("No coincide")

# Buscar Todas las Coincidencias con re.findall()
import re
texto = "Python es un lenguaje. Me gusta Python."
patron = "Python"
resultado = re.findall(patron, texto)
print("Coincidencias encontradas:", resultado)

# search(): Busca la primera coincidencia en el texto
import re
texto = "Mi número es 987-123-456"
patron = r"\d{3}-\d{3}-\d{3}"  # Busca un número con el formato 000-000-000
resultado = re.search(patron, texto)
if resultado:
    print("Encontrado:", resultado.group())  # 987-123-456


```

#### Usar Caracteres Especiales en Regex
- .	Cualquier carácter	    a.b     →   "acb"
- ^	Inicio de línea	        ^Hola   →   "Hola mundo"
- $	Fin de línea	        mundo$  →   "Hola mundo"
- *	0 o más repeticiones    ab*     →   "a", "ab", "abb"
- +	1 o más repeticiones    ab+     →   "ab", "abb"
- ?	0 o 1 repetición        ab?     →   "a", "ab"

```python
# Buscar palabras que comiencen con 'P'
import re

texto = "Python es Poderoso y Popular."
patron = r"\bP\w+"

resultado = re.findall(patron, texto)
print("Palabras encontradas:", resultado)

# Buscar palabras que comiencen con 'P'
import re

texto = "Python es Poderoso y Popular."
patron = r"\bP\w+"

resultado = re.findall(patron, texto)
print("Palabras encontradas:", resultado)
# \b → Límite de palabra.
# P\w+ → Encuentra palabras que comiencen con "P".
```
#### Grupos de Captura con Paréntesis
Los paréntesis permiten extraer partes de una coincidencia.
```python
import re
texto = "Juan tiene 25 años y María tiene 30."
patron = r"(\w+) tiene (\d+) años"
resultado = re.findall(patron, texto)
print(resultado)
# salida: [('Juan', '25'), ('María', '30')]

```
#### Reemplazo con re.sub()
re.sub() permite reemplazar texto basado en un patrón.
```python
# Reemplazar números por 'X'
import re

texto = "Mi número es 123-456-7890"
patron = r"\d"

nuevo_texto = re.sub(patron, "X", texto)
print(nuevo_texto)
# salida: Mi número es XXX-XXX-XXXX
```
#### Expresiones Regulares Avanzadas
Validar un correo electrónico
```python
import re
correo = "usuario@email.com"
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(patron, correo):
    print("Correo válido")
else:
    print("Correo inválido")
```
#### finditer(): Encuentra todas las coincidencias con detalles
```python
texto = "Números: 123, 456, 789"
patron = r"\d+"  # Encuentra números
for match in re.finditer(patron, texto):
    print(f"Número encontrado: {match.group()} en la posición {match.start()}")

```
#### Uso de Grupos de Captura
Podemos capturar partes específicas de un patrón con paréntesis ().
```python
texto = "Correo: contacto@empresa.com"
patron = r"(\w+)@(\w+\.\w+)"

resultado = re.search(patron, texto)
if resultado:
    print("Usuario:", resultado.group(1))  # contacto
    print("Dominio:", resultado.group(2))  # empresa.com
```
#### Clase 22: Manejo de Fechas y Horas con datetime  
Python tiene el módulo datetime para manejar fechas y horas.
```python
from datetime import datetime

# Obtener la fecha y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)
# También podemos obtener solo la fecha o la hora:
print("Solo la fecha:", ahora.date())
print("Solo la hora:", ahora.time())

# Crear Fechas y Horas Personalizadas
# Podemos definir una fecha y hora específicas usando datetime().
from datetime import datetime

fecha_personalizada = datetime(2025, 12, 25, 18, 30, 0)
print("Fecha personalizada:", fecha_personalizada) # Esto representa 25 de diciembre de 2025 a las 18:30.

```
#### Formateo de Fechas con strftime()
##### Convertir una fecha en texto con formato personalizado:
- %Y	Año completo	2025
- %y	Año corto	    25
- %m	Mes (01-12)	    03
- %d	Día (01-31)	    27
- %H	Hora (00-23)	14
- %M	Minuto (00-59)	45
- %S	Segundo (00-59)	30
```python
formato = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha formateada:", formato)

```
#### Convertir Cadenas a Fechas con strptime()
Convertir texto a objeto datetime:
```python
fecha_str = "27-03-2025 14:30"
formato = "%d-%m-%Y %H:%M"
fecha_convertida = datetime.strptime(fecha_str, formato)

print("Fecha convertida:", fecha_convertida)

```
#### Operaciones con Fechas (timedelta)
El módulo timedelta permite hacer cálculos con fechas.
```python
from datetime import datetime, timedelta

hoy = datetime.now()
dentro_de_7_dias = hoy + timedelta(days=7)
hace_3_horas = hoy - timedelta(hours=3)

print("Fecha en 7 días:", dentro_de_7_dias)
print("Hace 3 horas:", hace_3_horas)
```
Otros usos de timedelta:

- timedelta(weeks=2): Agrega 2 semanas
- timedelta(hours=5, minutes=30): Agrega 5 horas y 30 minutos
- timedelta(seconds=60): Agrega 1 minuto

#### Diferencia entre Fechas
Podemos calcular cuántos días, horas o minutos hay entre dos fechas.
```python
fecha1 = datetime(2025, 3, 27)
fecha2 = datetime(2025, 4, 10)

diferencia = fecha2 - fecha1
print("Días de diferencia:", diferencia.days)
```
#### Manejo de Zonas Horarias con pytz
```python
import pytz
from datetime import datetime

zona_horaria = pytz.timezone("America/Lima")
hora_local = datetime.now(zona_horaria)

print("Hora en Lima:", hora_local.strftime("%Y-%m-%d %H:%M:%S"))

```
Para usar pytz, instálalo con:
```bash
pip install pytz
```
# Clase 24: Desarrollo de Aplicaciones en Red con socket
Un socket es un punto de comunicación entre dos dispositivos en una red.

Python permite crear sockets para comunicaciones TCP (orientadas a conexión) y UDP (sin conexión).

TCP (Transmission Control Protocol): Asegura que los datos lleguen correctamente.

UDP (User Datagram Protocol): Más rápido, pero sin garantía de entrega.

💡 En esta clase nos enfocaremos en sockets TCP.
#### Crear un Servidor TCP con socket
El servidor escucha conexiones y responde a los clientes.

```python
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 12345))  # Escucha en cualquier IP en el puerto 12345
servidor.listen(5)  # Permite hasta 5 conexiones en cola

print("Servidor esperando conexiones...")

while True:
    cliente, direccion = servidor.accept()  # Acepta una conexión
    print(f"Cliente conectado desde {direccion}")
    
    mensaje = "¡Hola desde el servidor!"
    cliente.send(mensaje.encode("utf-8"))  # Envía mensaje al cliente
    cliente.close()  # Cierra la conexión con el cliente
```

#### Crear un Cliente TCP con socket
El cliente se conecta al servidor y recibe datos.
```python
import socket

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 12345))  # Conectarse al servidor en localhost

mensaje = cliente.recv(1024)  # Recibe mensaje del servidor
print("Mensaje del servidor:", mensaje.decode("utf-8"))

cliente.close()
# Ejecuta primero el servidor y luego el cliente para ver la comunicación.
```
#### Manejo de Múltiples Clientes con threading
Para manejar varios clientes al mismo tiempo, usamos threading.
```python
import socket
import threading

def manejar_cliente(cliente, direccion):
    print(f"Cliente conectado desde {direccion}")
    cliente.send("¡Bienvenido!".encode("utf-8"))
    cliente.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 12345))
servidor.listen(5)

print("Servidor en espera de clientes...")

while True:
    cliente, direccion = servidor.accept()
    hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
    hilo.start()

# Cada cliente será manejado en un hilo separado.
```
#### Crear un Chat Cliente-Servidor
Ejemplo de chat básico entre un servidor y varios clientes.
```python
# Código del Servidor de Chat
import socket
import threading

clientes = []

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break
            for c in clientes:
                c.send(mensaje)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 12345))
servidor.listen(5)

print("Servidor de chat en espera de conexiones...")

while True:
    cliente, direccion = servidor.accept()
    print(f"Cliente conectado desde {direccion}")
    clientes.append(cliente)
    hilo = threading.Thread(target=manejar_cliente, args=(cliente,))
    hilo.start()

# Código del Cliente de Chat
import socket
import threading

def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode("utf-8")
            print(mensaje)
        except:
            print("Conexión perdida")
            cliente.close()
            break

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 12345))

hilo = threading.Thread(target=recibir_mensajes, args=(cliente,))
hilo.start()

while True:
    mensaje = input("")
    cliente.send(mensaje.encode("utf-8"))

# Ejecuta primero el servidor y luego varios clientes en diferentes terminales para chatear en grupo.
```
# Clase 25: Comunicación en Tiempo Real con WebSockets
WebSockets permiten una comunicación bidireccional en tiempo real entre un cliente y un servidor.

#### Instalación de la librería websockets
```bash
pip install websockets

```
#### Crear un Servidor WebSocket
El servidor WebSocket espera conexiones y responde a los clientes.
```python
import asyncio
import websockets

async def servidor(websocket, path):
    print("Cliente conectado")
    while True:
        mensaje = await websocket.recv()  # Recibe mensaje del cliente
        print(f"Mensaje recibido: {mensaje}")
        await websocket.send(f"Echo: {mensaje}")  # Responde al cliente

# Iniciar servidor en localhost y puerto 12345
start_server = websockets.serve(servidor, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

```
#### Crear un Cliente WebSocket
```python
import asyncio
import websockets

async def cliente():
    async with websockets.connect("ws://localhost:12345") as websocket:
        await websocket.send("Hola, servidor!")  # Envía mensaje
        respuesta = await websocket.recv()  # Recibe respuesta
        print(f"Servidor dice: {respuesta}")

asyncio.get_event_loop().run_until_complete(cliente())
```
#### Crear un Chat en Tiempo Real con WebSockets
Vamos a hacer un chat donde varios clientes pueden enviar y recibir mensajes en tiempo real.
```python
# Código del Servidor de Chat
import asyncio
import websockets

clientes = set()  # Conjunto de clientes conectados

async def manejar_cliente(websocket, path):
    clientes.add(websocket)
    try:
        async for mensaje in websocket:
            print(f"Mensaje recibido: {mensaje}")
            # Enviar mensaje a todos los clientes conectados
            for cliente in clientes:
                if cliente != websocket:
                    await cliente.send(mensaje)
    except:
        pass
    finally:
        clientes.remove(websocket)

# Iniciar el servidor WebSocket
start_server = websockets.serve(manejar_cliente, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Código del Cliente de Chat
import asyncio
import websockets

async def recibir_mensajes(websocket):
    while True:
        try:
            mensaje = await websocket.recv()
            print(f"\nMensaje recibido: {mensaje}")
        except:
            print("Desconectado del servidor.")
            break

async def cliente():
    async with websockets.connect("ws://localhost:12345") as websocket:
        asyncio.create_task(recibir_mensajes(websocket))  # Hilo para recibir mensajes
        
        while True:
            mensaje = input("Tú: ")
            await websocket.send(mensaje)  # Enviar mensaje al servidor

asyncio.run(cliente())

```

# Clase 27: Optimización de Código

