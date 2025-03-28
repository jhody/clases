
## Request
Librería de Python que permite hacer peticiones HTTP de manera sencilla. Se usa para consumir APIs, descargar datos de la web, hacer scrapping, etc.

```bash
pip install requests
```

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)  # Código de respuesta HTTP
print(response.text)  # Contenido en formato string
print(response.json())  # Contenido en formato JSON (diccionario)
```
#### Enviando parámetros en una petición GET
```python
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(response.url)  # Muestra la URL con los parámetros
print(response.json())  # Muestra la respuesta en JSON

```
#### Enviando datos con una petición POST
- json=data automáticamente convierte el diccionario a JSON y lo envía.
- También puedes usar data=data, pero enviará los datos como x-www-form-urlencoded.
```python
data = {
    "title": "Nuevo post",
    "body": "Este es el contenido del post",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print(response.status_code)
print(response.json())  # Respuesta del servidor

```
#### Métodos HTTP: PUT, PATCH y DELETE
```python
data = {"title": "Título actualizado", "body": "Contenido nuevo", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)

print(response.status_code)
print(response.json())

```
#### Método PATCH (Actualizar parcialmente un recurso)
```python
data = {"title": "Título modificado"}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=data)

print(response.status_code)
print(response.json())

```
#### Método DELETE (Eliminar un recurso)
```python
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)  # 200 si fue exitoso, 404 si no existe

```
#### Manejo de encabezados (headers)
```python
headers = {"Authorization": "Bearer TU_TOKEN", "Content-Type": "application/json"}
response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)

print(response.status_code)
```
#### Manejo de errores y excepciones
```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1000")
    response.raise_for_status()  # Lanza un error si la respuesta no es 200

    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("Error HTTP:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error de conexión:", errc)
except requests.exceptions.Timeout as errt:
    print("Error de timeout:", errt)
except requests.exceptions.RequestException as err:
    print("Error general:", err)

```
#### Enviar archivos en una petición
```python
files = {"archivo": open("documento.txt", "rb")}
response = requests.post("https://httpbin.org/post", files=files)

print(response.json())

```
#### Uso de sesiones con requests
Si necesitas mantener una sesión activa (como en una autenticación).

Ventaja: La sesión mantiene los encabezados y cookies entre peticiones:
```python
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer TU_TOKEN"})

    response = session.get("https://jsonplaceholder.typicode.com/posts")
    print(response.json())

```
### Configuración avanzada
#### Definir un timeout
Para evitar que el código quede esperando indefinidamente:
```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=3)
    print(response.json())
except requests.exceptions.Timeout:
    print("La petición tardó demasiado y fue cancelada.")

```
#### Uso de proxies 
Si necesitas hacer peticiones a través de un proxy:
```python
proxies = {
    "http": "http://usuario:contraseña@proxy.com:8080",
    "https": "https://usuario:contraseña@proxy.com:8080"
}
response = requests.get("https://jsonplaceholder.typicode.com/posts", proxies=proxies)

print(response.status_code)

```
#### Autenticación
Para APIs que requieren autenticación básica:
```python
from requests.auth import HTTPBasicAuth

response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=HTTPBasicAuth("user", "pass"))

print(response.status_code)

```
## os
La librería os permite interactuar con el sistema operativo desde Python, incluyendo el manejo de archivos, directorios, variables de entorno y procesos
```python
# Nombre del sistema operativo
print(os.name)  # 'posix' en Linux/Mac, 'nt' en Windows

# Información detallada del sistema
import platform
print(platform.system())   # 'Windows', 'Linux', 'Darwin' (Mac)
print(platform.release())  # Versión del sistema
print(platform.version())  # Detalles completos del SO
print(platform.architecture())  # Arquitectura (32 o 64 bits)

# Obtener una variable de entorno
print(os.getenv("HOME"))  # Ruta del home en Linux/Mac
print(os.getenv("USER"))  # Usuario actual

# Listar todas las variables de entorno
print(os.environ)  # Devuelve un diccionario con todas las variables

# Establecer una variable de entorno
os.environ["MI_VARIABLE"] = "Hola Mundo"
print(os.getenv("MI_VARIABLE"))

# Obtener el directorio actual
print(os.getcwd())  # Directorio donde se ejecuta el script

# Cambiar de directorio
os.chdir("/ruta/deseada")  # Cambia de directorio
print(os.getcwd())  # Confirma el cambio

# Listar archivos en un directorio
print(os.listdir("."))  # Lista archivos y carpetas en el directorio actual

# Crear un nuevo directorio
os.mkdir("nueva_carpeta")  # Crea una carpeta en el directorio actual
os.makedirs("padre/hijo/nieto") # Para crear una carpeta y subcarpetas si no existen:

# Eliminar un directorio
os.rmdir("nueva_carpeta")  # Elimina solo si está vacío

# Para eliminar una carpeta con contenido, usa shutil.rmtree("nombre") (requiere import shutil).
import shutil
shutil.rmtree("nombre")

# Comprobar si un archivo o directorio existe
ruta = "archivo.txt"
print(os.path.exists(ruta))  # True si existe, False si no
print(os.path.isfile(ruta))  # True si es archivo
print(os.path.isdir(ruta))   # True si es directorio

# Obtener información de un archivo
ruta = "archivo.txt"
print(os.path.getsize(ruta))  # Tamaño en bytes
print(os.path.abspath(ruta))  # Ruta absoluta

# Ejecutar un comando y mostrar la salida
os.system("ls")  # En Linux/Mac
os.system("dir")  # En Windows

# jemplo avanzado: Capturar la salida del comando
import subprocess

resultado = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(resultado.stdout)

# Unir rutas
# Para trabajar con rutas de manera portátil (compatible con Windows y Linux/Mac), usa os.path
ruta = os.path.join("carpeta", "archivo.txt")
print(ruta)  # 'carpeta/archivo.txt' en Linux, 'carpeta\archivo.txt' en Windows

# Separar nombre y extensión
nombre, extension = os.path.splitext("archivo.txt")
print(nombre)     # 'archivo'
print(extension)  # '.txt'

# Obtener el nombre del archivo o la carpeta desde una ruta
print(os.path.basename("/ruta/archivo.txt"))  # 'archivo.txt'
print(os.path.dirname("/ruta/archivo.txt"))   # '/ruta'

#  Eliminar un archivo
os.remove("archivo.txt")
# Para eliminar una carpeta con contenido:
import shutil
shutil.rmtree("carpeta")


```
## queue
se usa para manejar estructuras de datos en las que los elementos se procesan en orden de llegada o según prioridad
```python
import queue
```
Python ofrece tres tipos principales de colas:
- queue.Queue	Cola FIFO (First In, First Out)
- queue.LifoQueue	Pila LIFO (Last In, First Out)
- queue.PriorityQueue	Cola de prioridad (menor valor = mayor prioridad)

Ejemplo: Agregar y sacar elementos en orden FIFO (Primero en entrar, primero en salir)
```python
import queue

q = queue.Queue()  # Crear la cola

q.put("A")  # Agregar elementos
q.put("B")
q.put("C")

print(q.get())  # 'A' (Se extrae el primer elemento)
print(q.get())  # 'B'
print(q.get())  # 'C'
```
- 🔹 put(item): Agrega un elemento a la cola.
- 🔹 get(): Saca un elemento en orden de llegada.
- 🔹 qsize(): Devuelve el número de elementos en la cola.
- 🔹 empty(): Devuelve True si la cola está vacía.

Ejemplo: Último en entrar, primero en salir (como una pila)
```python
import queue

stack = queue.LifoQueue()

stack.put("X")
stack.put("Y")
stack.put("Z")

print(stack.get())  # 'Z' (Último en entrar, primero en salir)
print(stack.get())  # 'Y'
print(stack.get())  # 'X'
```
Cola de prioridad (queue.PriorityQueue)

 Elementos con prioridad (el menor valor sale primero)
```python
import queue

pq = queue.PriorityQueue()

pq.put((2, "Bajo"))   # Tupla (prioridad, elemento)
pq.put((1, "Alto"))
pq.put((3, "Medio"))

print(pq.get())  # (1, 'Alto') → Prioridad más baja (1) sale primero
print(pq.get())  # (2, 'Bajo')
print(pq.get())  # (3, 'Medio')

# -------------
pq.put((10, "Importante"))
pq.put((5, "Normal"))
pq.put((1, "Urgente"))

while not pq.empty():
    print(pq.get()[1])  # Extrae solo el valor

```


