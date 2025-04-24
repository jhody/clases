
# NumPy es una biblioteca fundamental para realizar cálculos científicos en Python. Aquí aprenderemos a usar arrays y a realizar operaciones básicas con ellos.
# Dataset base
import numpy as np
# Creación de Arrays
# Los arrays de NumPy son similares a las listas de Python, pero optimizados para operaciones matemáticas.

# Crear un array 1D
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
# Resultado:
# [1 2 3 4 5]

# Crear un array 2D (matriz)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Resultado:
# [[1 2 3]
#  [4 5 6]]

# Crear un array de ceros
arr_zeros = np.zeros((3, 3))
print(arr_zeros)
# Resultado:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# Crear un array de unos
arr_ones = np.ones((2, 4))
print(arr_ones)
# Resultado:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# Crear un array con un rango de números
arr_range = np.arange(0, 10, 2)
print(arr_range)
# Resultado:
# [0 2 4 6 8]

# Sumar un número a un array
arr_1d + 10
# Resultado:
# [11 12 13 14 15]

# Realizar operaciones aritméticas entre arrays
arr_1d * 2
# Resultado:
# [ 2  4  6  8 10]

# Realizar operaciones entre arrays de la misma dimensión
arr_1d + np.array([5, 4, 3, 2, 1])
# Resultado:
# [6 6 6 6 6]

# Sumar todos los elementos de un array
np.sum(arr_1d)
# Resultado:
# 15

# Promedio de los elementos
np.mean(arr_1d)
# Resultado:
# 3.0

# Desviación estándar
np.std(arr_1d)
# Resultado:
# 1.4142135623730951

# Mínimo y máximo
np.min(arr_1d), np.max(arr_1d)
# Resultado:
# (1, 5)

# Redimensionar arrays
# Cambiar la forma de un array 1D a 2D
arr_reshaped = arr_1d.reshape(5, 1)
print(arr_reshaped)
# Resultado:
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]

# Aplanar un array 2D
arr_flattened = arr_2d.flatten()
print(arr_flattened)
# Resultado:
# [1 2 3 4 5 6]

# Producto punto (dot product)
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

np.dot(arr_a, arr_b)
# Resultado:
# 32

# Transponer una matriz
arr_transpose = arr_2d.T
print(arr_transpose)
# Resultado:
# [[1 4]
#  [2 5]
#  [3 6]]

# Índices y cortes (slicing)
arr_1d[2]
# Resultado:
# 3

# Cortar un sub-array
arr_1d[1:4]
# Resultado:
# [2 3 4]

# Seleccionar una fila de un array 2D
arr_2d[0]
# Resultado:
# [1 2 3]

# Producto Escalar (Dot Product)
# ---------------------------------
# El producto escalar, también conocido como el producto punto, es una operación fundamental en álgebra lineal. Se utiliza frecuentemente en cálculos de matrices y vectores.
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

producto_escalar = np.dot(arr_a, arr_b)
print(producto_escalar)
# Resultado:
# 32
# Explicación: El producto escalar entre dos vectores a y b es la suma de los productos de sus elementos correspondientes:
#       1∗4+2∗5+3∗6=32

# Multiplicación de Matrices
# La multiplicación de matrices es otra operación crucial. En NumPy, puedes multiplicar matrices usando el método np.dot o el operador @.
# Ejemplo de multiplicación de matrices
matriz_1 = np.array([[1, 2], [3, 4]])
matriz_2 = np.array([[5, 6], [7, 8]])

producto_matrices = np.dot(matriz_1, matriz_2)
print(producto_matrices)
# Resultado:
# [[19 22]
#  [43 50]]

# Transposición de una Matriz
# La transposición de una matriz cambia sus filas por columnas y viceversa.
matriz = np.array([[1, 2, 3], [4, 5, 6]])
matriz_transpuesta = matriz.T
print(matriz_transpuesta)
# Resultado:
# [[1 4]
#  [2 5]
#  [3 6]]

#  Inversión de una Matriz
# La inversa de una matriz A es una matriz B tal que 𝐴⋅𝐵=𝐼 (donde I es la matriz identidad). Solo las matrices cuadradas (de igual número de filas y columnas) tienen una inversa.
matriz = np.array([[4, 7], [2, 6]])
matriz_inversa = np.linalg.inv(matriz)
print(matriz_inversa)
# Resultado:
# [[ 0.6 -0.7]
#  [-0.2  0.4]]

# Determinante de una Matriz
# El determinante de una matriz es un valor escalar que puede ser utilizado para decidir si una matriz es invertible o no. Si el determinante es cero, la matriz no es invertible.
matriz = np.array([[4, 7], [2, 6]])
determinante = np.linalg.det(matriz)
print(determinante)
# Resultado:
# 10.000000000000002

#  Operaciones entre Arrays con Diferentes Dimensiones (Broadcasting)
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[4, 5, 6], [7, 8, 9]])

resultado = arr_2d + arr_1d
print(resultado)
# Resultado:
# [[5 7 9]
#  [8 10 12]]



