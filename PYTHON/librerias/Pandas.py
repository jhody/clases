
import pandas as pd  # Importa la librería pandas con el alias "pd"

# Crear un DataFrame simple
df = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [25, 30]})  # Crea una tabla con columnas 'Nombre' y 'Edad'
df.head()  # Muestra las primeras 5 filas del DataFrame
df.info()  # Muestra información del DataFrame como columnas y tipos de datos
df.describe()  # Muestra estadísticas básicas como media, conteo y desviación estándar
df['Nombre']  # Devuelve la columna 'Nombre' como una Serie
df[df['Edad'] > 25]  # Muestra solo las filas donde la edad es mayor a 25
df['Mayor de edad'] = df['Edad'] >= 18  # Crea una nueva columna con valores booleanos
df = pd.read_csv('archivo.csv')  # Carga un archivo CSV en un DataFrame
df.to_csv('nuevo_archivo.csv', index=False)  # Guarda el DataFrame a un archivo CSV sin el índice
df[(df['Edad'] > 20) & (df['Nombre'] == 'Luis')]  # Filtra filas con edad > 20 y nombre Luis
df['Nombre'] = df['Nombre'].replace('Luis', 'Luisito')  # Reemplaza "Luis" por "Luisito" en la columna
df.dropna()  # Elimina todas las filas que tengan al menos un valor nulo
df.fillna(0)  # Reemplaza los valores nulos con 0
df['Edad'] = df['Edad'].astype(str)  # Convierte la columna 'Edad' a tipo texto
df.rename(columns={'Edad': 'Años'})  # Cambia el nombre de la columna 'Edad' a 'Años'
df[['Nombre', 'Edad']]  # Devuelve solo las columnas 'Nombre' y 'Edad'
df = df[['Edad', 'Nombre']]  # Cambia el orden de las columnas
df['Edad + 5'] = df['Edad'] + 5  # Crea nueva columna con la edad más 5
df.drop(columns='Edad + 5')  # Elimina la columna llamada 'Edad + 5'
df.groupby('Nombre').size()  # Agrupa por 'Nombre' y cuenta cuántas veces aparece cada uno
df.groupby('Nombre')['Edad'].mean()  # Calcula la edad promedio por cada nombre
df.groupby('Nombre')['Edad'].agg(['mean', 'max'])  # Muestra la media y el máximo de edad por nombre
df.groupby(['Nombre', 'Mayor de edad']).size()  # Agrupa por dos columnas y cuenta
df.groupby('Nombre')['Edad'].mean().reset_index()  # Devuelve un DataFrame normal tras agrupar
df.groupby('Nombre').filter(lambda x: x['Edad'].mean() > 25)  # Deja grupos cuya media de edad sea > 25
df.groupby('Nombre')['Edad'].apply(lambda x: x.max() - x.min())  # Resta entre máximo y mínimo por grupo
# Ejemplo:
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Marta']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Edad': [25, 30, 40]
})
# merge (inner join por defecto)
pd.merge(df1, df2, on='ID')
# Resultado:
#    ID Nombre  Edad
# 0   1    Ana    25
# 1   2   Luis    30

# merge con how='outer': Une todos los datos de ambos DataFrames, rellenando con NaN donde no hay coincidencia.
pd.merge(df1, df2, on='ID', how='outer')
# Resultado:
#    ID Nombre  Edad
# 0   1    Ana  25.0
# 1   2   Luis  30.0
# 2   3   Marta   NaN
# 3   4    NaN  40.0

# Merge con how='left': Muestra todo lo de df1 y lo que coincida desde df2.
pd.merge(df1, df2, on='ID', how='left')
# Resultado:
#    ID Nombre  Edad
# 0   1    Ana  25.0
# 1   2   Luis  30.0
# 2   3  Marta   NaN

# merge con how='right': Muestra todo lo de df2 y lo que coincida desde df1.
pd.merge(df1, df2, on='ID', how='right')
# Resultado:
#    ID Nombre  Edad
# 0   1    Ana    25
# 1   2   Luis    30
# 2   4    NaN     40

# concat: unir verticalmente (uno debajo del otro)
# Une filas de los DataFrames, duplicando en este caso df1.
pd.concat([df1, df1])
# Resultado:
#    ID Nombre
# 0   1    Ana
# 1   2   Luis
# 2   3  Marta
# 0   1    Ana
# 1   2   Luis
# 2   3  Marta

# concat horizontal (por columnas)
#  Une columnas por posición (ojo: no une por ID, solo por índice).
pd.concat([df1, df2], axis=1)
# Resultado:
#    ID Nombre  ID  Edad
# 0   1    Ana   1    25
# 1   2   Luis   2    30
# 2   3  Marta   4    40

# Pivotear y transformar datos 
# -----------------------------
# (cómo convertir filas en columnas y viceversa)
# Dataset de ejemplo:
df = pd.DataFrame({
    'Nombre': ['Ana', 'Ana', 'Luis', 'Luis'],
    'Año': [2023, 2024, 2023, 2024],
    'Ventas': [100, 150, 200, 250]
})
# pivot: transforma valores únicos en columnas
df.pivot(index='Nombre', columns='Año', values='Ventas')
#  Convierte los años en columnas, organizando las ventas por nombre.
# Resultado:
# Año    2023  2024
# Nombre            
# Ana     100   150
# Luis    200   250

# reset_index() para quitar el índice jerárquico
df.pivot(index='Nombre', columns='Año', values='Ventas').reset_index()
# Quita el índice de filas y lo convierte en una columna normal.
# Resultado:
# Año Nombre  2023  2024
# 0     Ana   100   150
# 1    Luis   200   250

# melt: pasa columnas a filas
# Convierte columnas de año en filas, útil para graficar o limpiar datos.
pivot_df = df.pivot(index='Nombre', columns='Año', values='Ventas').reset_index()

pd.melt(pivot_df, id_vars='Nombre', var_name='Año', value_name='Ventas')
# Resultado:
#   Nombre   Año  Ventas
# 0    Ana  2023     100
# 1   Luis  2023     200
# 2    Ana  2024     150
# 3   Luis  2024     250

# stack: aplana columnas en un nuevo índice
# Convierte columnas en niveles de fila (Series con índice jerárquico).
df.pivot(index='Nombre', columns='Año', values='Ventas').stack()
# Resultado:
# Nombre  Año 
# Ana     2023    100
#         2024    150
# Luis    2023    200
#         2024    250
# dtype: int64

# unstack: lo contrario de stack
# Convierte un índice jerárquico en columnas.
df.set_index(['Nombre', 'Año'])['Ventas'].unstack()
# Resultado:
# Año    2023  2024
# Nombre            
# Ana     100   150
# Luis    200   250

# Manejo de valores faltantes (NaN) en pandas
# -------------------------------------------
# Vamos a trabajar con un DataFrame con algunos valores faltantes para mostrar cómo se pueden detectar, eliminar o reemplazar.
#  Dataset con valores faltantes:
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro'],
    'Edad': [25, np.nan, 35, np.nan],
    'Ciudad': ['Lima', 'Cusco', np.nan, 'Arequipa']
})

# Ver valores faltantes
# True indica que hay un valor faltante (NaN).
df.isna()
# Resultado:
#   Nombre   Edad  Ciudad
# 0  False  False   False
# 1  False   True   False
# 2  False  False    True
# 3  False   True   False

# Contar valores faltantes por columna
#  Cuenta cuántos NaN hay en cada columna.
df.isna().sum()
# Resultado:
# Nombre    0
# Edad      2
# Ciudad    1

# Eliminar filas con NaN
# Solo mantiene las filas que no tienen NaN.
df.dropna()
# Resultado:
#   Nombre  Edad Ciudad
# 0    Ana  25.0   Lima

# Rellenar NaN con un valor fijo
# Cambia todos los NaN por 0.
df.fillna(0)
# Resultado:
#   Nombre  Edad   Ciudad
# 0    Ana  25.0     Lima
# 1   Luis   0.0     Cusco
# 2  Marta  35.0         0
# 3  Pedro   0.0  Arequipa

#  Rellenar con diferentes valores por columna
# Se reemplaza Edad por el promedio y Ciudad por texto personalizado.
df.fillna({
    'Edad': df['Edad'].mean(),  # promedio
    'Ciudad': 'Desconocida'
})
# Resultado:
#   Nombre      Edad      Ciudad
# 0    Ana  25.000000        Lima
# 1   Luis  30.000000        Cusco
# 2  Marta  35.000000  Desconocida
# 3  Pedro  30.000000    Arequipa

# Rellenar hacia adelante (forward fill)
# Rellena cada NaN con el valor anterior.
df.fillna(method='ffill')
# Resultado:
#   Nombre  Edad   Ciudad
# 0    Ana  25.0     Lima
# 1   Luis  25.0     Cusco
# 2  Marta  35.0     Cusco
# 3  Pedro  35.0  Arequipa

# Rellenar hacia atrás (backward fill)
# Rellena NaN con el siguiente valor válido (si hay).
df.fillna(method='bfill')
# Resultado:
#   Nombre  Edad   Ciudad
# 0    Ana  25.0     Lima
# 1   Luis  35.0     Cusco
# 2  Marta  35.0  Arequipa
# 3  Pedro   NaN  Arequipa

# Agrupar y resumir datos con groupby() en pandas
# --------------------------------------------------
# Esta es una de las funciones más poderosas en pandas: permite agrupar datos por categorías y aplicar funciones como suma, promedio, conteo, etc.
# Dataset de ejemplo:
df = pd.DataFrame({
    'Vendedor': ['Ana', 'Ana', 'Luis', 'Luis', 'Marta'],
    'Zona': ['Norte', 'Sur', 'Norte', 'Sur', 'Norte'],
    'Ventas': [100, 150, 200, 250, 180]
})

# Agrupar por una columna y sumar
# Agrupa por vendedor y suma sus ventas.
df.groupby('Vendedor')['Ventas'].sum()
# Resultado:
# Vendedor
# Ana     250
# Luis    450
# Marta   180
# Name: Ventas, dtype: int64

# Agrupar por dos columnas
df.groupby(['Vendedor', 'Zona'])['Ventas'].sum()
# Agrupa por vendedor y zona.
# Resultado:
# Vendedor  Zona 
# Ana       Norte    100
#           Sur      150
# Luis      Norte    200
#           Sur      250
# Marta     Norte    180
# Name: Ventas, dtype: int64

# Convertir a DataFrame (con .reset_index())
df.groupby(['Vendedor', 'Zona'])['Ventas'].sum().reset_index()
# Resultado:
# Vendedor  Zona  Ventas
# 0      Ana Norte     100
# 1      Ana   Sur     150
# 2     Luis Norte     200
# 3     Luis   Sur     250
# 4    Marta Norte     180
# -- Vuelve a un DataFrame con columnas normales.

# Funciones estadísticas básicas
df.groupby('Zona')['Ventas'].mean()
# Resultado:
# Zona
# Norte    160.0
# Sur      200.0
# Name: Ventas, dtype: float64
# Promedio de ventas por zona.

# agg: múltiples funciones a la vez
df.groupby('Vendedor')['Ventas'].agg(['sum', 'mean', 'count'])
# Resultado:
#           sum   mean  count
# Vendedor                    
# Ana       250  125.0      2
# Luis      450  225.0      2
# Marta     180  180.0      1
# --Aplica varias funciones estadísticas a la vez.

# Filtrar grupos con .filter()
df.groupby('Vendedor').filter(lambda x: x['Ventas'].sum() > 300)
# Resultado:
#   Vendedor   Zona  Ventas
# 2     Luis  Norte     200
# 3     Luis    Sur     250
# -- Solo muestra los grupos que cumplen una condición (ventas totales > 300).

# Combinar DataFrames (merge, concat, join)
# ------------------------------------------
# Esto es útil cuando tienes datos en varias tablas (como en SQL) y quieres unirlos para analizarlos juntos.
# Dos DataFrames de ejemplo:
import pandas as pd

clientes = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Marta']
})

ventas = pd.DataFrame({
    'ID': [1, 2, 4],
    'Venta': [100, 200, 300]
})

# merge: como un JOIN en SQL
pd.merge(clientes, ventas, on='ID')
# Resultado:
#    ID Nombre  Venta
# 0   1    Ana    100
# 1   2   Luis    200
# --Une ambos DataFrames por la columna "ID" (solo coincidencias).

# Tipos de merge
# how='inner' (por defecto): solo coincidencias
pd.merge(clientes, ventas, on='ID', how='inner')
# Igual al anterior

# how='left': todos los clientes, aunque no tengan ventas
pd.merge(clientes, ventas, on='ID', how='left')
# Resultado:
#    ID Nombre  Venta
# 0   1    Ana  100.0
# 1   2   Luis  200.0
# 2   3  Marta    NaN

# how='right': todas las ventas, aunque no haya cliente
pd.merge(clientes, ventas, on='ID', how='right')
# Resultado:
#    ID Nombre  Venta
# 0   1    Ana  100.0
# 1   2   Luis  200.0
# 2   4    NaN  300.0

# how='outer': todos los datos, aunque no coincidan
pd.merge(clientes, ventas, on='ID', how='outer')
# Resultado:
#    ID Nombre  Venta
# 0   1    Ana  100.0
# 1   2   Luis  200.0
# 2   3  Marta    NaN
# 3   4    NaN  300.0

# concat: unir filas o columnas
# Unir por filas (axis=0)
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

pd.concat([df1, df2])
# Resultado:
#    A
# 0  1
# 1  2
# 0  3
# 1  4

# Unir por columnas (axis=1)
pd.concat([df1, df2], axis=1)
# Resultado:
#    A  A
# 0  1  3
# 1  2  4

# join: unir usando el índice
clientes.set_index('ID').join(ventas.set_index('ID'))
# Resultado:
#    Nombre  Venta
# ID               
# 1     Ana  100.0
# 2    Luis  200.0
# 3   Marta    NaN
# --Une por índice en lugar de columna específica.

#  Tablas dinámicas (pivot_table), tablas cruzadas (crosstab) y ordenamiento (sort_values)
# -------------------------------------------
# Estas herramientas te permiten resumir y organizar tus datos como lo harías en Excel con una tabla dinámica.
# Dataset base:
import pandas as pd

df = pd.DataFrame({
    'Vendedor': ['Ana', 'Ana', 'Luis', 'Luis', 'Marta'],
    'Zona': ['Norte', 'Sur', 'Norte', 'Sur', 'Norte'],
    'Ventas': [100, 150, 200, 250, 180]
})

# pivot_table: tabla dinámica
pd.pivot_table(df, values='Ventas', index='Vendedor', columns='Zona', aggfunc='sum')
# Resultado:
# Zona      Norte    Sur
# Vendedor              
# Ana        100  150.0
# Luis       200  250.0
# Marta      180    NaN
# --Resume las ventas por zona y vendedor.

# Varias funciones a la vez
pd.pivot_table(df, values='Ventas', index='Vendedor', aggfunc=['sum', 'mean'])
# Resultado:
#           sum   mean
# Ventas                
# Ana       250  125.0
# Luis      450  225.0
# Marta     180  180.0
# Usa más de una función con aggfunc.

# crosstab: tabla cruzada (categorías)
pd.crosstab(df['Vendedor'], df['Zona'])
# Resultado:
# Zona     Norte  Sur
# Vendedor            
# Ana           1    1
# Luis          1    1
# Marta         1    0
# --Cuenta cuántas veces aparece cada combinación (frecuencias).

# sort_values: ordenar
# Ordenar por columna 'Ventas' descendente
df.sort_values(by='Ventas', ascending=False)
# Resultado:
#   Vendedor   Zona  Ventas
# 3     Luis    Sur     250
# 2     Luis  Norte     200
# 4    Marta  Norte     180
# 1      Ana    Sur     150
# 0      Ana  Norte     100

# sort_index: ordenar por el índice
df.set_index('Vendedor').sort_index()
# Resultado:
#           Zona  Ventas
# Vendedor                
# Ana       Norte     100
# Ana         Sur     150
# Luis      Norte     200
# Luis        Sur     250
# Marta     Norte     180

# Manejo de valores nulos y duplicados
# Trabajar con datos reales implica tratar con valores faltantes (NaN) o filas repetidas. Aquí te muestro cómo identificarlos y manejarlos.
#  Dataset base:
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Marta', 'Luis', None],
    'Edad': [25, np.nan, 30, 30, 22],
    'Ciudad': ['Lima', 'Cusco', 'Lima', 'Cusco', None]
})

# Verificar valores nulos
df.isnull()
# Resultado:
#   Nombre   Edad  Ciudad
# 0  False  False   False
# 1  False   True   False
# 2  False  False   False
# 3  False  False   False
# 4   True  False    True
# --True indica valores nulos.

# Contar valores nulos por columna
df.isnull().sum()
# Resultado:
# Nombre    1
# Edad      1
# Ciudad    1

# Eliminar filas con valores nulos
df.dropna()
# Resultado:
#   Nombre  Edad Ciudad
# 0    Ana  25.0   Lima
# 2  Marta  30.0   Lima
# 3   Luis  30.0  Cusco

# Rellenar valores nulos
df.fillna('Desconocido')
# Resultado:
#     Nombre       Edad     Ciudad
# 0      Ana       25.0       Lima
# 1     Luis  Desconocido      Cusco
# 2    Marta       30.0       Lima
# 3     Luis       30.0      Cusco
# 4  Desconocido     22.0  Desconocido

# También puedes rellenar por columnas numéricas:
df['Edad'].fillna(df['Edad'].mean())
# Resultado: reemplaza el NaN por la media de la columna Edad

# Detectar duplicados
df.duplicated()
# Resultado:
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False

# Eliminar duplicados
df.drop_duplicates()
# Resultado:
#   Nombre  Edad Ciudad
# 0    Ana  25.0   Lima
# 1   Luis   NaN  Cusco
# 2  Marta  30.0   Lima
# 4   None  22.0   None

# Agrupaciones y estadísticas (groupby, agg, estadísticas básicas)
# ---------------------------------
# Esta clase te enseñará cómo agrupar datos y aplicar funciones estadísticas para obtener resúmenes de los mismos.
# Dataset base:
import pandas as pd

df = pd.DataFrame({
    'Departamento': ['Ventas', 'Ventas', 'Soporte', 'Soporte', 'Ventas'],
    'Empleado': ['Ana', 'Luis', 'Marta', 'Pedro', 'Carlos'],
    'Ventas': [150, 200, 300, 250, 180]
})

# groupby: agrupar por una columna
df.groupby('Departamento').sum()
# Resultado:
#              Ventas
# Departamento        
# Soporte        550
# Ventas         530
# --Agrupa los datos por "Departamento" y calcula la suma de las ventas de cada grupo.

# Varias funciones con agg
df.groupby('Departamento').agg({'Ventas': ['sum', 'mean', 'max']})
# Resultado:
#               Ventas               
#                 sum   mean  max
# Departamento                   
# Soporte         550   275.0  300
# Ventas          530   176.6  200
# --- Aplica múltiples funciones estadísticas a la columna "Ventas".

# groupby con múltiples columnas
df['Año'] = [2021, 2021, 2022, 2022, 2021]

df.groupby(['Año', 'Departamento']).sum()
# Resultado:
#                Ventas
# Año  Departamento       
# 2021 Ventas        350
#     Soporte       450
# 2022 Soporte       250
# --Agrupa por dos columnas: "Año" y "Departamento", y calcula la suma de ventas para cada combinación.

# Estadísticas básicas
df['Ventas'].mean()
# Resultado:
# 216.0

# Desviación estándar
df['Ventas'].std()
# Resultado:
# 58.86849740153757

# Mínimo
df['Ventas'].min()
# Resultado:
# 150

# Máximo
df['Ventas'].max()
# Resultado:
# 300

# Mediana
df['Ventas'].median()
# Resultado:
# 200.0

# Manipulación avanzada de cadenas (str methods)
# -------------------------------------------------
# En esta clase veremos cómo trabajar con columnas de tipo cadena de texto en un DataFrame usando métodos de str.
# Dataset base:
import pandas as pd

df = pd.DataFrame({
    'Nombre': ['Ana Pérez', 'Luis García', 'Marta López', 'Pedro Díaz', 'Carlos Gómez'],
    'Correo': ['ana.perez@mail.com', 'luis.garcia@mail.com', 'marta.lopez@mail.com', 'pedro.diaz@mail.com', 'carlos.gomez@mail.com']
})

# Convertir a minúsculas o mayúsculas
df['Nombre'].str.lower()
# Resultado:
# 0      ana pérez
# 1    luis garcía
# 2    marta lópez
# 3    pedro díaz
# 4    carlos gómez

# A mayúsculas
df['Nombre'].str.upper()
# Resultado:
# 0      ANA PÉREZ
# 1    LUIS GARCÍA
# 2    MARTA LÓPEZ
# 3    PEDRO DÍAZ
# 4    CARLOS GÓMEZ

# Buscar una subcadena
df['Correo'].str.contains('mail')
# Resultado:
# 0     True
# 1     True
# 2     True
# 3     True
# 4     True

# Buscar subcadena en una columna específica
df['Nombre'].str.contains('Luis')
# Resultado:
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False

# Reemplazar subcadenas
df['Correo'].str.replace('mail.com', 'example.com')
# Resultado:
# 0       ana.perez@example.com
# 1     luis.garcia@example.com
# 2    marta.lopez@example.com
# 3     pedro.diaz@example.com
# 4    carlos.gomez@example.com

# Extraer una subcadena con expresiones regulares
df['Nombre'].str.extract('(\w+)', expand=False)
# Resultado:
# 0       Ana
# 1      Luis
# 2     Marta
# 3     Pedro
# 4    Carlos

# Separar cadenas en columnas
df['Nombre'].str.split(' ', expand=True)
# Resultado:
#        0      1
# 0     Ana   Pérez
# 1    Luis  García
# 2   Marta   López
# 3   Pedro    Díaz
# 4  Carlos   Gómez

# Longitud de las cadenas
df['Nombre'].str.len()
# Resultado:
# 0     9
# 1    12
# 2    11
# 3    10
# 4    12































