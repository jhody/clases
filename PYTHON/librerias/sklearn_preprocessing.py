# preprocessing de sklearn (scikit-learn)! Esta sublibrería es fundamental para preparar datos antes de entrenar modelos de machine learning
from sklearn import preprocessing
# Importa el módulo preprocessing de scikit-learn

# Normalizar datos con MinMaxScaler (escala entre 0 y 1)
import numpy as np
from sklearn.preprocessing import MinMaxScaler

datos = np.array([[1], [2], [3], [4], [5]])
escalador = MinMaxScaler()
normalizados = escalador.fit_transform(datos)
print(normalizados)
# Resultado:
# [[0.  ]
#  [0.25]
#  [0.5 ]
#  [0.75]
#  [1.  ]]

# Estandarizar datos con StandardScaler (media = 0, desviación = 1)
from sklearn.preprocessing import StandardScaler

datos = np.array([[1], [2], [3], [4], [5]])
scaler = StandardScaler()
estandar = scaler.fit_transform(datos)
print(estandar)
# Resultado aproximado:
# [[-1.41]
#  [-0.71]
#  [ 0.  ]
#  [ 0.71]
#  [ 1.41]]

# Codificar etiquetas con LabelEncoder
from sklearn.preprocessing import LabelEncoder

etiquetas = ['perro', 'gato', 'gato', 'pez']
encoder = LabelEncoder()
codificadas = encoder.fit_transform(etiquetas)
print(codificadas)
# Resultado:
# [2 1 1 0]

# One-hot encoding con OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

valores = [['rojo'], ['verde'], ['azul'], ['rojo']]
encoder = OneHotEncoder(sparse=False)
onehot = encoder.fit_transform(valores)
print(onehot)
# Resultado:
# [[0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]
#  [0. 0. 1.]]

# Binarizar datos (mayores a umbral = 1, si no = 0)
from sklearn.preprocessing import Binarizer

datos = np.array([[1], [4], [6]])
binarizer = Binarizer(threshold=3)
binarizados = binarizer.transform(datos)
print(binarizados)
# Resultado:
# [[0]
#  [1]
#  [1]]

# Normalizar filas (para modelos que necesitan vectores unitarios)
from sklearn.preprocessing import normalize

X = np.array([[1, 2], [2, 2], [3, 5]])
normalizado = normalize(X, norm='l2')
print(normalizado)
# Resultado aproximado:
# [[0.45 0.89]
#  [0.71 0.71]
#  [0.51 0.85]]


# Imputar valores faltantes (rellenar con la media)
from sklearn.impute import SimpleImputer

X = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = SimpleImputer(strategy='mean')
completado = imputer.fit_transform(X)
print(completado)
# Resultado:
# [[1. 2.]
#  [4. 3.]
#  [7. 6.]]


# RESUMEN:
# MinMaxScaler	Pone todos los números entre 0 y 1	Alturas convertidas proporcionalmente
# StandardScaler	Centra los datos con media 0 y misma escala	Notas ajustadas a media 0
# LabelEncoder	Convierte palabras en números	‘perro’ → 2
# OneHotEncoder	Crea columnas para cada palabra	‘rojo’ → [0,0,1]
# Binarizer	Convierte en 0 o 1 según un límite	6 → 1 si el límite era 5

