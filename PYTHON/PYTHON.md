
Instalar la versión edition [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows):

clase #156
```python
print('*** Regresar una tupla de valores desde una función ***')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {42}')
```
clase #157
```python
print('*** Obtener coordenadas x,y,z ***')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

# Llamar la funcion
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')
```
clase #158 Alcance de variables
```python
print('*** Alcance de Variables ***')

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # incrementamos la variable global
    contador_global += 1
    # incrementar la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias vece la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')
```
clase #159:Argumentos variables *args en Python
```python
print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
superheroe_superpoderes('Ironam', 'Tony Stark', 'Armadura','Playboy','Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan Perez')
```
160. Argumentos variables en forma de diccionarios **kwargs en Python
```python
# *args - arguments - tupla
# **kwargs - keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamarmos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armandura','Playboy', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')

```
161. Suma con Argumentos Variables
```python
print('*** Suma con Argumentos Variables ***')

# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Resultado de la suma: {resultado}')

```
162. Ejemplo con kwargs - Detalle de Persona
```python
print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')
```
163. Ejemplo de función números pares en Python
```python
print('*** Funcion par ***')

# Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Proporciona un valor numérico: '))
    print(f'Número par? {es_par(numero)}')

```
165. Ejemplo de funciones recursivas en Python
```python
print('*** Imprimir del 1 al 5 de forma recursiva ***')

# definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')  # 1
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Programa principal
funcion_recursiva(5)
```
167. Ejercicio - Factorial de un número con recursividad en Python
```python
print('*** Factorial del Número 5 ***')

# Definimos la funcion factorial recursiva
def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

numero = 5
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es: {resultado}')
```
169. Potencia de un número con recursividad
```python
print('*** Potencia número usando funciones recursivas ***')

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)

print(f'2 elevado a la 3: {potencia(2, 3)}')
print(f'5 elevado a la 0: {potencia(5, 0)}')
print(f'4 elevado a la 5: {potencia(4, 5)}')
```


