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


