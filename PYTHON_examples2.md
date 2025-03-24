
## Clases

```python
class MiClase:
    pass  # Clase vacía

objeto = MiClase()
print(type(objeto))  # <class '__main__.MiClase'>

# Atributos y Métodos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

# Crear un objeto con atributos
persona1 = Persona("Juan", 30)
print(persona1.nombre)  # Juan
print(persona1.edad)    # 30

# Métodos
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  

    def saludar(self):
        return f"Hola, soy {self.nombre}"

# Llamar un método
persona1 = Persona("Ana")
print(persona1.saludar())  # Hola, soy Ana


```
### Métodos Especiales (Dunder Methods)

```python
#__init__ (Constructor)

class Auto:
    def __init__(self, marca):
        self.marca = marca

# __str__ (Representación en Texto)
class Auto:
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"Auto de marca {self.marca}"

auto1 = Auto("Toyota")
print(auto1)  # Auto de marca Toyota

# __repr__ (Representación para Debugging)
class Auto:
    def __repr__(self):
        return f"Auto(marca='{self.marca}')"

```
### Métodos de Clase y Métodos Estáticos
```python
# Método de Clase (@classmethod)
class Persona:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

    @classmethod
    def cantidad_personas(cls):
        return cls.contador

# Llamando el método de clase
p1 = Persona("Carlos")
p2 = Persona("Ana")
print(Persona.cantidad_personas())  # 2

# Método Estático (@staticmethod)
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematica.sumar(3, 4))  # 7

```
### Herencia en Python
```python
# Herencia Simple
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"

# Crear un objeto de la subclase
perro = Perro()
print(perro.hacer_sonido())  # Guau Guau

# Herencia Múltiple
class A:
    def metodo_a(self):
        return "A"

class B:
    def metodo_b(self):
        return "B"

class C(A, B):
    pass

obj = C()
print(obj.metodo_a())  # A
print(obj.metodo_b())  # B

```
### Encapsulamiento, Propiedades y Métodos Getter/Setter

```python
# encapsulamiento (_ y __)
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre  # _nombre = protegido
        self.__edad = 30  # __edad = privado

p = Persona("Luis")
print(p._nombre)  # Accesible pero no recomendado
# print(p.__edad)  # Error

# Uso de property (Getter y Setter)
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# uso de propiedades:
p = Persona("David")
print(p.nombre)  # David
p.nombre = "Carlos"
print(p.nombre)  # Carlos

```
### Clases Abstractas e Interfaces
```python
# Clases Abstractas con ABC
from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

c = Cuadrado(4)
print(c.area())  # 16

```
### Métodos Especiales Avanzados (__call__, __getitem__, __setitem__)
```python
# __call__: Hacer una clase "llamable"
class Contador:
    def __init__(self):
        self.cuenta = 0

    def __call__(self):
        self.cuenta += 1
        return self.cuenta

c = Contador()
print(c())  # 1
print(c())  # 2

# __getitem__ y __setitem__
class MiLista:
    def __init__(self):
        self.datos = {}

    def __getitem__(self, clave):
        return self.datos.get(clave, "No existe")

    def __setitem__(self, clave, valor):
        self.datos[clave] = valor

# Usar la clase como un diccionario
lista = MiLista()
lista["nombre"] = "Juan"
print(lista["nombre"])  # Juan


```
## SOBRE CARGA DE OPERADORES

```python
# Sobrecarga del Operador + (__add__)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
resultado = v1 + v2
print(resultado)  # Vector(6, 8)

# Sobrecarga del Operador - (__sub__)
class Vector:
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
# ejemplo de uso:
resultado = v1 - v2
print(resultado)  # Vector(-2, -2)

# Sobrecarga del Operador * (__mul__)
class Vector:
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)

resultado = v1 * 3
print(resultado)  # Vector(6, 9)

# Sobrecarga del Operador == (__eq__)
class Vector:
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
v3 = Vector(2, 3)
print(v1 == v3)  # True
print(v1 == v2)  # False

# Sobrecarga de !=, <, <=, >, >=
#Estos operadores se sobrecargan con:
    #__ne__ → !=
    #__lt__ → <
    #__le__ → <=
    #__gt__ → >
    #__ge__ → >=
class Vector:
    def __lt__(self, otro):  # Menor que
        return (self.x**2 + self.y**2) < (otro.x**2 + otro.y**2)

    def __le__(self, otro):  # Menor o igual que
        return (self.x**2 + self.y**2) <= (otro.x**2 + otro.y**2)
print(v1 < v2)   # True
print(v1 <= v2)  # True

# Sobrecarga de str() y repr() (__str__ y __repr__)
class Vector:
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
print(str(v1))   # Vector(2, 3)
print(repr(v1))  # Vector(x=2, y=3)

#Sobrecarga del Operador [] (__getitem__, __setitem__) 
class Vector:
    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __setitem__(self, index, valor):
        if index == 0:
            self.x = valor
        elif index == 1:
            self.y = valor

print(v1[0])  # 2
v1[1] = 10
print(v1)     # Vector(2, 10)

# Sobrecarga del Operador () (__call__)
class Vector:
    def __call__(self):
        return f"Coordenadas: ({self.x}, {self.y})"
print(v1())  # Coordenadas: (2, 10)

```
## MANEJO DE ARCHIVOS
```python
# Abrir y Cerrar un Archivo (open() y close())
archivo = open("archivo.txt", "r")  # Modo lectura
contenido = archivo.read()
print(contenido)
archivo.close()  # Cerrar el archivo

# Modos de apertura (mode):
#   "r" → Lectura (error si el archivo no existe).
#   "w" → Escritura (borra el contenido si el archivo ya existe).
#   "a" → Añadir al final del archivo.
#   "x" → Creación exclusiva (error si el archivo ya existe).
#   "b" → Modo binario (usado con imágenes, PDFs, etc.).
#   "t" → Modo texto (predeterminado).
# Ejemplo con with open() (no necesita close()):
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer un Archivo Completo (read())
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el contenido
    print(contenido)

# Leer Línea por Línea (readline(), readlines())
with open("archivo.txt", "r") as archivo:
    linea = archivo.readline()  # Lee una sola línea
    print(linea)

with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()  # Devuelve una lista con todas las líneas
    print(lineas)

# Escribir en un Archivo (write())
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")  # Sobrescribe el contenido
# Escribir múltiples líneas con writelines():
with open("archivo.txt", "w") as archivo:
    archivo.writelines(["Línea 1\n", "Línea 2\n", "Línea 3\n"])

# Agregar Texto sin Sobrescribir (a)
with open("archivo.txt", "a") as archivo:
    archivo.write("Nueva línea agregada\n")

# Leer y Escribir (r+)
with open("archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    archivo.write("\nNueva línea agregada después de leer.")

# Manejo de Archivos Binarios (rb, wb)
    #  Ejemplo: Copiar una imagen
with open("imagen.jpg", "rb") as origen:
    contenido = origen.read()

with open("copia.jpg", "wb") as destino:
    destino.write(contenido)

# Comprobar si un Archivo Existe
#   (os.path.exists())
import os

if os.path.exists("archivo.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")

# Eliminar un Archivo (os.remove())
import os
if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
    print("Archivo eliminado")
else:
    print("El archivo no existe")

# Manipular Carpetas (os.mkdir(), os.rmdir(), shutil.rmtree())
import os
os.mkdir("nueva_carpeta")  # Crea una carpeta
os.rmdir("nueva_carpeta")  # Elimina la carpeta (debe estar vacía)
# Para eliminar una carpeta con contenido:
import shutil
shutil.rmtree("nueva_carpeta")  # Elimina la carpeta y todo su contenido

```
## Uso de with en Python
El bloque with se usa para manejar recursos como archivos, sockets, conexiones a bases de datos, etc., asegurando que se cierren correctamente, incluso si ocurre un error.
### Uso de with para Manejo de Archivos
```python
# Sin with:
archivo = open("archivo.txt", "r")
contenido = archivo.read()
archivo.close()  # Debemos cerrar el archivo manualmente
# Con with:
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()  # Se cierra automáticamente
# Ventaja: No necesitas close(), el archivo se cierra correctamente, incluso si hay un error.

# Leer un Archivo Línea por Línea con with
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # `.strip()` elimina saltos de línea extra

# Escribir en un Archivo con with
with open("archivo.txt", "w") as archivo:
    archivo.write("Nueva línea\n")  # Escribe y cierra automáticamente

# Agregar Texto sin Sobrescribir (a)
with open("archivo.txt", "a") as archivo:
    archivo.write("Otra línea agregada\n")

# Trabajar con Archivos Binarios con with
with open("imagen.jpg", "rb") as origen, open("copia.jpg", "wb") as destino:
    destino.write(origen.read())
# Ventaja: Se pueden manejar múltiples archivos con with.

# Uso de with en Bloques Personalizados (__enter__ y __exit__)
Puedes crear una clase que implemente __enter__ y __exit__ para definir su comportamiento en un bloque with.
class MiRecurso:
    def __enter__(self):
        print("Recurso adquirido")
        return self  # Devuelve el objeto

    def __exit__(self, exc_type, exc_value, traceback):
        print("Recurso liberado")

with MiRecurso():
    print("Usando el recurso")

# salida:   Recurso adquirido  
#           Usando el recurso  
#           Recurso liberado  


```
# POSTGRESS
### conector postgress
instalar en consola, el entorno virtual de pycharm,
para conectar con postgress
```bach
    pip install psycopg2

```
### conector mysql
```bach
    pip install mysql-connector
```

```python
import psycopg2
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db',
)
print(conexion)

# primera forma
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()

# segunda forma
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = 2
            cursor.execute(sentencia, (id_persona, ))# la coma al final es pq es una tupla
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

```
### Fetchall y Fetchone(sólo un registro)
```python
    registros = cursor.fetchall()
    registros = cursor.fetchone()

# enviando una tupla en la consulta
    sentencia = 'SELECT * FROM persona WHERE id_persona in %s'
    llaves_primarias = ((1,2,3),)
    cursor.execute(sentencia, llaves_primarias)

    
    sentencia = 'SELECT * FROM persona WHERE id_persona in %s'
    entrada = '1,2,3'
    llaves_primarias = (tuple(entrada.split(',')),)
    cursor.execute(sentencia, llaves_primarias)
```

### Conectarse a PostgreSQL con with
No necesitas llamar conexion.close() ni cursor.close(), ya que with lo hace automáticamente.
```python
import psycopg2

# Parámetros de conexión
db_params = {
    "dbname": "mi_base",
    "user": "mi_usuario",
    "password": "mi_contraseña",
    "host": "localhost",
    "port": "5432"
}

# Usando with para conexión y cursor
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(cursor.fetchone())  # Muestra la versión de PostgreSQL

```
### Crear una Tabla con with
```python
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                edad INT
            );
        """)
        print("Tabla creada correctamente")

```
### Insertar Datos con with
```python
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 25))
        print("Usuario insertado")

# otro ejemplo:
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Carlos','Lara','cladr@gmail.com')
            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# insertar varios registros: executemany
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = (
                ('Carlos','Lara','cladr@gmail.com'),
                ('Angel','Quintana','cladr@gmail.com'),
                ('Marcos','Gonzales','cladr@gmail.com')
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()


```
### Leer Datos con with
```python
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios;")
        usuarios = cursor.fetchall()  # Obtiene todas las filas
        for usuario in usuarios:
            print(usuario)

```
### Actualizar Datos con with
```python
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET edad = %s WHERE nombre = %s", (30, "Juan"))
        print("Usuario actualizado")

# actualizar un registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos','Juarez','cladr@gmail.com',1)
            cursor.execute(sentencia, valores)
            registros_actualizados= cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

    
# actualizar varios registros (executemany)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan Carlos','Juarez','cladr@gmail.com',1),
                ('María ','Juarez','cladr@gmail.com',2),
                ('Andrés ','Juarez','cladr@gmail.com',3)
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados= cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
```
### Eliminar Datos con with
```python
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE nombre = %s", ("Juan",))
        print("Usuario eliminado")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM  persona WHERE id_persona=%s'
            valores = (7,)
            cursor.execute(sentencia, valores)
            registros_eliminados= cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

    
# eliminar varios registros 
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM  persona WHERE id_persona IN %s'
            entrada = '1,2,3'
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados= cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
```
### Manejo de Errores con try-except
```python
try:
    with psycopg2.connect(**db_params) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios;")
            for usuario in cursor.fetchall():
                print(usuario)
except psycopg2.Error as e:
    print("Error en la base de datos:", e)

```
### Conexión con contextlib.closing
Si solo necesitas la conexión sin with anidados:
```python
from contextlib import closing

with closing(psycopg2.connect(**db_params)) as conexion, closing(conexion.cursor()) as cursor:
    cursor.execute("SELECT * FROM usuarios;")
    print(cursor.fetchall())
# closing() garantiza que los objetos se cierren automáticamente.

```
## Transacciones en PostgreSQL
### Transacción Básica (Automática con with)
Cuando usas with psycopg2.connect(...), los cambios se confirman automáticamente cuando el bloque termina sin errores.
```python
import psycopg2 as db

db_params = {
    "dbname": "mi_base",
    "user": "mi_usuario",
    "password": "mi_contraseña",
    "host": "localhost",
    "port": "5432"
}

with db.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Carlos", 28))
        # No es necesario `conexion.commit()`, se hace automáticamente si no hay errores
print("Usuario insertado correctamente")

```
### Transacción Manual con commit() y rollback()
Puedes desactivar el modo de autocommit y manejar la transacción manualmente.
Ventaja:

Control total sobre cuándo confirmar (commit()) o revertir (rollback()).
```python
try:
    conexion = psycopg2.connect(**db_params)
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Ana", 35))
    
    conexion.commit()  # Confirmar los cambios
    print("Transacción completada")
except psycopg2.Error as e:
    conexion.rollback()  # Deshacer cambios en caso de error
    print("Error en la transacción:", e)
finally:
    cursor.close()
    conexion.close()

```
### Transacción con Múltiples Operaciones (Todas o Ninguna)
Si una operación falla, no se guardará ninguna.
```python
try:
    with psycopg2.connect(**db_params) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Luis", 40))
            cursor.execute("UPDATE usuarios SET edad = edad + 1 WHERE nombre = %s", ("Luis",))
            # Si una falla, ninguna se guarda
    print("Transacción completada")
except psycopg2.Error as e:
    print("Error en la transacción:", e)

```
### Transacción con SAVEPOINT (Puntos de Control)
Si quieres hacer un rollback solo a una parte específica de la transacción, usa SAVEPOINT.

Ventaja:

- Si ocurre un error, se revierte solo lo después del SAVEPOINT.
- Todo lo anterior al SAVEPOINT sigue vigente.
```python
try:
    with psycopg2.connect(**db_params) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Pedro", 50))

            cursor.execute("SAVEPOINT sp1")  # Guardamos el punto de control

            cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Error", "XX"))  # Falla
            
            cursor.execute("RELEASE SAVEPOINT sp1")  # Si todo va bien, liberamos el SAVEPOINT
except psycopg2.Error as e:
    with psycopg2.connect(**db_params) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("ROLLBACK TO SAVEPOINT sp1")  # Revierte solo lo posterior al SAVEPOINT
    print("Se revirtió parte de la transacción:", e)

```
### Transacciones con isolation_level
PostgreSQL permite configurar el nivel de aislamiento de una transacción.

Niveles de aislamiento en PostgreSQL:

- READ COMMITTED (Por defecto) → Ve solo los cambios confirmados.
- REPEATABLE READ → Bloquea las filas leídas hasta que la transacción termina.
- SERIALIZABLE → La transacción se comporta como si fuera la única en ejecución

```python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

with psycopg2.connect(**db_params) as conexion:
    conexion.set_isolation_level(ISOLATION_LEVEL_SERIALIZABLE)
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Sergio", 45))

```
### Transacción en Múltiples Conexiones
Si dos conexiones intentan modificar la misma fila, puedes bloquearla con FOR UPDATE.
```python
# Problema sin Bloqueo: Condición de Carrera
# Proceso 1
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT edad FROM usuarios WHERE nombre = 'Juan'")
        edad = cursor.fetchone()[0]
        edad += 1
        cursor.execute("UPDATE usuarios SET edad = %s WHERE nombre = 'Juan'", (edad,))
# Si otro proceso hace lo mismo al mismo tiempo, pueden sobrescribirse los valores.

# Solución con SELECT ... FOR UPDATE
# Proceso 1
with psycopg2.connect(**db_params) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT edad FROM usuarios WHERE nombre = 'Juan' FOR UPDATE")
        edad = cursor.fetchone()[0]
        edad += 1
        cursor.execute("UPDATE usuarios SET edad = %s WHERE nombre = 'Juan'", (edad,))
# Esto bloquea la fila hasta que la transacción termina, evitando sobrescribir cambios.


```
### autocommit
si no se hace commit no se guardaran los cambios
```python
import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',database='tempp')

try:
    conexion.autocommit = False # no se guarda los cambios
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores = ('Maria','Esparza','mespas@gmail.com')
    cursor.execute(sentencia,valores)
    conexion.commit()
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
```

