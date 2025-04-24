import sklearn

from sklearn.tree import DecisionTreeClassifier

# Entrenamos con ejemplos: tamaño y fruta
X = [[5], [6], [7], [10], [11], [12]]   # Tamaño
y = ['manzana', 'manzana', 'manzana', 'sandía', 'sandía', 'sandía']

# Creamos el robot que aprenderá
robot = DecisionTreeClassifier()

# Entrenamos al robot
robot.fit(X, y)

# Probamos con una fruta de tamaño 9
print(robot.predict([[9]]))  # El robot dice: ['sandía']

# 2. DIVIDIR LOS DATOS: train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(X_train)  # Datos para entrenar
print(X_test)   # Datos para probar

# 3. ENTRENAR Y PROBAR
robot.fit(X_train, y_train)
predicciones = robot.predict(X_test)

print(predicciones)
print("¿Lo hizo bien?", predicciones == y_test)

# 4. MEDIR SU DESEMPEÑO: accuracy_score
from sklearn.metrics import accuracy_score

print("Precisión:", accuracy_score(y_test, predicciones))  # Ej: 1.0 o 0.66

# 5. NORMALIZAR DATOS con preprocessing
from sklearn.preprocessing import StandardScaler

datos = [[1, 100], [2, 200], [3, 300]]
limpiador = StandardScaler()
datos_limpios = limpiador.fit_transform(datos)

print(datos_limpios)
# Cada valor se transforma para que todos estén “en el mismo rango”

# 6. USAR OTROS MODELOS
# Además de árboles (DecisionTreeClassifier), sklearn tiene otros cerebritos como:
# Modelo	¿Para qué sirve?
# LinearRegression	Predecir números (como precios)
# KNeighborsClassifier	Adivinar según “vecinos” similares
# SVC (máquinas de soporte)	Separar clases difíciles
# RandomForestClassifier	Un bosque de decisiones más sabio

# TEMA 1: Regresión Lineal (Linear Regression)
# La regresión lineal intenta dibujar una línea recta que pase lo más cerca posible de los puntos, para poder predecir un número.
# Supongamos que tenemos estos datos:
# Peso (kg) | Precio (S/.)
# 1 | 1.5
# 2 | 2.0
# 3 | 2.5
# 4 | 3.0
# Queremos saber cuánto costará una fruta que pesa 5 kg.
#  Paso 1: Preparar los datos
from sklearn.linear_model import LinearRegression

# Datos de ejemplo: peso y precio
peso = [[1], [2], [3], [4]]  # X
precio = [1.5, 2.0, 2.5, 3.0]  # y

# Paso 2: Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(peso, precio)  # Aprende la relación

# Paso 3: Predecir el precio para 5 kg
prediccion = modelo.predict([[5]])
print(prediccion)  # Resultado: [3.5]

# El modelo aprendió que el precio sube 0.5 por cada kilo. Entonces, si 4 kg = 3.0, entonces 5 kg = 3.5.
# Extra: Ver la fórmula que aprendió
print("Pendiente:", modelo.coef_)     # → Cuánto sube el precio por kg
print("Intersección:", modelo.intercept_)  # → Precio base si el peso fuera 0

# Extra visual (opcional con matplotlib)
import matplotlib.pyplot as plt

plt.scatter(peso, precio, color='blue')           # Puntos reales
plt.plot(peso + [[5]], modelo.predict(peso + [[5]]), color='red')  # Línea
plt.xlabel("Peso (kg)")
plt.ylabel("Precio (S/.)")
plt.title("Regresión Lineal: Peso vs Precio")
plt.grid()
plt.show()

# tema 2: Clasificación con KNN (vecinos cercanos) explicado igual de simple?
# El modelo de KNN mira los vecinos más cercanos a un punto nuevo y decide en qué grupo ponerlo según los vecinos.
#  Ejemplo: Clasificar frutas por tamaño y dulzura
# Tamaño | Dulzura | Tipo
# 1 | 1 | Limón
# 2 | 1 | Limón
# 4 | 5 | Mango
# 5 | 4 | Mango
# Queremos saber qué tipo es una fruta con tamaño 3 y dulzura 3.
# Paso 1: Preparar los datos
from sklearn.neighbors import KNeighborsClassifier

# Características: tamaño y dulzura
X = [[1, 1], [2, 1], [4, 5], [5, 4]]  # datos
y = ["Limón", "Limón", "Mango", "Mango"]  # etiquetas

nueva_fruta = [[3, 3]]

# Paso 2: Crear y entrenar el modelo
modelo = KNeighborsClassifier(n_neighbors=3)  # Mira a los 3 vecinos más cercanos
modelo.fit(X, y)

# Paso 3: Predecir el tipo de la nueva fruta
prediccion = modelo.predict(nueva_fruta)
print(prediccion)  # Resultado: ['Mango']
# La fruta nueva está más cerca de los mangos (vecinos dulces), así que el modelo la clasifica como "Mango".

# Extra visual (opcional)
import matplotlib.pyplot as plt

for i in range(len(X)):
    color = 'green' if y[i] == "Mango" else 'yellow'
    plt.scatter(X[i][0], X[i][1], color=color, label=y[i] if i < 2 else "")

plt.scatter(nueva_fruta[0][0], nueva_fruta[0][1], color='red', label='¿Qué soy?')
plt.xlabel("Tamaño")
plt.ylabel("Dulzura")
plt.legend()
plt.title("Clasificación KNN: Frutas")
plt.grid()
plt.show()

# TEMA 3: Árboles de Decisión
# ¿Qué hace?
# Un árbol de decisión hace preguntas para tomar decisiones.
# Como un juego de sí/no:
# "¿Es dulce?" → "¿Es grande?" → Entonces es mango.

# Ejemplo: Clasificar frutas (otra vez 🍋🥭)
# Tamaño | Dulzura | Tipo
# 1 | 1 | Limón
# 2 | 1 | Limón
# 4 | 5 | Mango
# 5 | 4 | Mango
# Paso 1: Preparar los datos
from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [2, 1], [4, 5], [5, 4]]  # características
y = ["Limón", "Limón", "Mango", "Mango"]  # etiquetas

# Paso 2: Crear y entrenar el modelo
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Paso 3: Predecir el tipo de fruta
fruta_nueva = [[3, 3]]
prediccion = modelo.predict(fruta_nueva)
print(prediccion)  # Resultado: ['Mango']
# El árbol hizo preguntas tipo “¿dulzura mayor a 2.5?” y decidió que lo más probable es Mango.

# Extra: Dibujar el árbol (requiere graphviz)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
plot_tree(modelo, feature_names=["Tamaño", "Dulzura"], class_names=["Limón", "Mango"], filled=True)
plt.title("Árbol de decisión")
plt.show()

# TEMA 4: Regresión con Árboles de Decisión
# A diferencia de clasificación (que elige un grupo), la regresión predice un número exacto.

# Por ejemplo: “¿Cuánto va a costar esta casa según sus metros y cuartos?”
# Ejemplo: Predecir precios de casas 🏠
# Metros² | Cuartos | Precio (en miles)
# 50 | 1 | 100
# 60 | 2 | 150
# 80 | 3 | 200
# 100 | 4 | 250
# Queremos predecir el precio de una casa de 70 m² y 2 cuartos.
# Paso 1: Preparar los datos
from sklearn.tree import DecisionTreeRegressor

X = [[50, 1], [60, 2], [80, 3], [100, 4]]
y = [100, 150, 200, 250]  # precios

# Paso 2: Crear y entrenar el modelo
modelo = DecisionTreeRegressor()
modelo.fit(X, y)

# Paso 3: Predecir el precio
casa_nueva = [[70, 2]]
prediccion = modelo.predict(casa_nueva)
print(prediccion)  # Resultado: [150.]

# El árbol ve que 70 m² y 2 cuartos están más cerca del ejemplo [60, 2], cuyo precio era 150. Así que predice 150.
# Extra: Ver el árbol (opcional)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
plot_tree(modelo, feature_names=["Metros", "Cuartos"], filled=True)
plt.title("Árbol de regresión de precios")
plt.show()

# Tema 5: Random Forest (Clasificación) (Bosque Aleatorio)! 🌳🌳🌳
# Imagina que no decides solo con un árbol, sino con muchos árboles votando. Eso es un Random Forest.
# Crea muchos árboles y votan cuál es la mejor predicción.
# Es como tener un equipo de expertos, no solo uno.
# Ejemplo: Clasificar frutas 🍋🥭 (otra vez)
# Tamaño | Dulzura | Tipo
# 1 | 1 | Limón
# 2 | 1 | Limón
# 4 | 5 | Mango
# 5 | 4 | Mango

# Paso 1: Datos
from sklearn.ensemble import RandomForestClassifier

X = [[1, 1], [2, 1], [4, 5], [5, 4]]
y = ["Limón", "Limón", "Mango", "Mango"]

# Paso 2: Crear y entrenar el modelo
modelo = RandomForestClassifier(n_estimators=10)  # 10 árboles
modelo.fit(X, y)

# Paso 3: Predecir fruta nueva
nueva_fruta = [[3, 3]]
prediccion = modelo.predict(nueva_fruta)
print(prediccion)  # Resultado: ['Mango']
# Varios árboles deciden su respuesta. Si la mayoría dice "Mango", el resultado es Mango.

# ¿Y para regresión?
# Solo cambia el modelo:
from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor(n_estimators=10)
modelo.fit(X, y)  # y ahora serían precios, por ejemplo

# TEMA 6: SVM (Support Vector Machine)
# SVM encuentra la línea (o curva) que mejor separa las clases, con el máximo margen posible.
# Imagina que tienes puntos azules y rojos, y quieres trazar una línea entre ellos que los separe lo mejor posible.

# Ejemplo simple: Clasificar colores 🔵🔴
# Ancho | Alto | Color
# 1 | 1 | Azul
# 2 | 1 | Azul
# 4 | 5 | Rojo
# 5 | 4 | Rojo

# Paso 1: Datos
from sklearn.svm import SVC

X = [[1, 1], [2, 1], [4, 5], [5, 4]]
y = ["Azul", "Azul", "Rojo", "Rojo"]

# Paso 2: Crear y entrenar el modelo
modelo = SVC(kernel='linear')  # Usamos una línea como separación
modelo.fit(X, y)

# Paso 3: Predecir un color nuevo
nuevo = [[3, 3]]
prediccion = modelo.predict(nuevo)
print(prediccion)  # Resultado: ['Rojo']
# La SVM traza la línea de separación lo más equilibrada posible. Si el punto (3, 3) cae del lado de los rojos, devuelve 'Rojo'.

# ⚙️ Otros kernel
# 'linear': línea recta.
# 'rbf': curva suave (usa para datos no lineales).
# 'poly': curvas con polinomios.
modelo = SVC(kernel='rbf')

# ¿Y para regresión? Se usa SVR:
from sklearn.svm import SVR

modelo = SVR()
modelo.fit(X, [1.0, 1.5, 4.0, 4.5])  # valores continuos

# Tema 7: KNN – K Vecinos más Cercanos! (K-Nearest Neighbors)
# Es uno de los algoritmos más simples pero poderosos si se usan bien.
# Busca los K vecinos más cercanos a tu nuevo dato y vota cuál es la clase más común.
# Imagina que preguntas a tus amigos más cercanos qué fruta es y eliges la mayoría.

# Ejemplo: Clasificar frutas 🍋🥭
# Tamaño | Dulzura | Tipo
# 1 | 1 | Limón
# 2 | 1 | Limón
# 4 | 5 | Mango
# 5 | 4 | Mango

#  Paso 1: Datos
from sklearn.neighbors import KNeighborsClassifier

X = [[1, 1], [2, 1], [4, 5], [5, 4]]
y = ["Limón", "Limón", "Mango", "Mango"]

# Paso 2: Crear y entrenar el modelo
modelo = KNeighborsClassifier(n_neighbors=3)  # Usamos 3 vecinos
modelo.fit(X, y)

# Paso 3: Predecir fruta nueva
nueva_fruta = [[3, 3]]
prediccion = modelo.predict(nueva_fruta)
print(prediccion)  # Resultado: ['Mango']
# El punto (3,3) está más cerca de los mangos (4,5) y (5,4), así que se predice "Mango".

# Puedes cambiar el número de vecinos:
modelo = KNeighborsClassifier(n_neighbors=1)
# Más vecinos = más consenso, pero puede perder precisión con pocos datos.

# Para regresión:
from sklearn.neighbors import KNeighborsRegressor

modelo = KNeighborsRegressor(n_neighbors=3)
modelo.fit(X, [0.5, 0.7, 4.5, 4.3])

# TEMA 8: Evaluación de Modelos
# Evalúa el rendimiento de un modelo para ver si está acertando con las predicciones.
# ⚙️ Métricas comunes para clasificación:
# Precisión (Accuracy): ¿Qué porcentaje de predicciones fueron correctas?
# Matriz de Confusión: ¿Cuántos falsos positivos y falsos negativos hubo?
# Precisión, Recall y F1-Score: Métodos más detallados, útiles cuando hay clases desbalanceadas.

# Ejemplo: Clasificar frutas 🍋🥭
# Supón que tienes un modelo para clasificar frutas como Limón o Mango, y las etiquetas predichas no son perfectas.
# Tamaño | Dulzura | Predicción | Real
# 1 | 1 | Limón | Limón
# 2 | 1 | Limón | Limón
# 4 | 5 | Mango | Mango
# 5 | 4 | Mango | Limón

# Paso 1: Importar las herramientas
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Paso 2: Definir los valores reales y predicciones
y_real = ["Limón", "Limón", "Mango", "Limón"]
y_pred = ["Limón", "Limón", "Mango", "Mango"]

# Paso 3: Calcular la precisión
precision = accuracy_score(y_real, y_pred)
print(f"Precisión: {precision}")
# La precisión nos dice cuántas veces el modelo acertó.

# Paso 4: Matriz de Confusión
matriz = confusion_matrix(y_real, y_pred, labels=["Limón", "Mango"])
print("Matriz de Confusión:")
print(matriz)
#             | Pred: Limón | Pred: Mango
#  Real Limón | 2 | 1
#  Real Mango | 0 | 1
# La matriz nos dice cuántas veces predijo cada clase correctamente y cuántos errores cometió.

# Paso 5: Reporte de clasificación
reporte = classification_report(y_real, y_pred)
print("Reporte de clasificación:")
print(reporte)
# Este reporte incluye precisión, recall, y F1-score para cada clase. Es útil cuando las clases no están balanceadas.

# Para regresión (precisión y errores):
# Para regresión, las métricas cambian, y usamos:
#   Error Cuadrático Medio (MSE): Mide la diferencia promedio entre lo predicho y lo real.
#   Error Absoluto Medio (MAE): El valor absoluto de la diferencia entre las predicciones y los valores reales.
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_real_regresion = [100, 150, 200]
y_pred_regresion = [110, 140, 195]

mse = mean_squared_error(y_real_regresion, y_pred_regresion)
mae = mean_absolute_error(y_real_regresion, y_pred_regresion)

print(f"MSE: {mse}")
print(f"MAE: {mae}")

#  TEMA 9: Guardar y Cargar Modelos
# Cuando entrenas un modelo, puedes guardarlo para no tener que volver a entrenarlo cada vez. ¡Muy útil en proyectos reales!

# Paso 1: Entrenar un modelo simple
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)

# Paso 2: Guardar el modelo con joblib
import joblib

joblib.dump(modelo, "modelo_entrenado.pkl")
# Guarda el modelo entrenado en un archivo llamado modelo_entrenado.pkl

# Paso 3: Cargar el modelo más tarde
modelo_cargado = joblib.load("modelo_entrenado.pkl")
# Carga el modelo guardado y ahora puedes usarlo directamente

# Paso 4: Usar el modelo cargado para predecir
resultado = modelo_cargado.predict([X_test[0]])
print("Predicción:", resultado)
# Resultado: una predicción sobre la clase de la muestra

# TEMA 10: Pipelines en Scikit-learn
# Un Pipeline te permite encadenar varios pasos de preprocesamiento y entrenamiento en una sola estructura.
# ✅ Ventaja: Todo el flujo (escalar, transformar, entrenar) queda organizado y es más fácil de guardar, reutilizar y probar.

# Paso 1: Crear un pipeline con escalador + modelo
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('escalador', StandardScaler()),           # Paso 1: Escalado de datos
    ('clasificador', LogisticRegression())     # Paso 2: Entrenar modelo
])

# Paso 2: Usar el pipeline con datos
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

pipe.fit(X_train, y_train)
# Entrena: primero escala los datos, luego entrena el modelo

#  Paso 3: Predecir con el pipeline
resultado = pipe.predict(X_test[:3])
print("Predicción:", resultado)
# Resultado: las clases predichas para las primeras 3 muestras del test

# Paso 4: Guardar todo el pipeline
import joblib
joblib.dump(pipe, "pipeline_entrenado.pkl")
# Guarda todo el proceso (escalado + modelo) en un archivo

#  Paso 5: Cargar y usar directamente
pipe_cargado = joblib.load("pipeline_entrenado.pkl")
print(pipe_cargado.predict([X_test[0]]))
# Usa el pipeline sin preocuparte por escalar o preparar los datos de nuevo

#  Ideal para:
#  Mantener el flujo limpio y automático.
#  Reutilizar en producción.
#  Evitar errores al aplicar transformaciones distintas en entrenamiento y prueba.

# TEMA 11: Validación cruzada con cross_val_score
# En vez de entrenar y probar con una sola división de los datos, la validación cruzada divide los datos en varias partes (llamadas “folds”) y repite el entrenamiento muchas veces para tener una evaluación más confiable.
# ¿Por qué es útil?
# Evita confiar en un solo train_test_split, lo que puede dar una falsa seguridad. En cambio, mide cómo se comporta tu modelo con múltiples combinaciones de entrenamiento/prueba.

# Ejemplo básico con 5 folds
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
modelo = LogisticRegression(max_iter=200)

resultados = cross_val_score(modelo, X, y, cv=5)
# Hace 5 pruebas (con diferentes divisiones) y evalúa el modelo
print("Precisión por fold:", resultados)
print("Precisión promedio:", resultados.mean())

#  Salida esperada:
Precisión por fold: [0.96 0.96 0.9  0.96 1.  ]
Precisión promedio: 0.956
# El modelo tiene una precisión promedio de 95.6% al evaluar con 5 divisiones distintas del dataset.

# Validación cruzada con un pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ('escalador', StandardScaler()),
    ('modelo', LogisticRegression())
])

resultados = cross_val_score(pipe, X, y, cv=5)
print("Precisión promedio del pipeline:", resultados.mean())

# Recuerda:
# cv=5 significa 5 divisiones (se puede cambiar).
# La función cross_val_score evalúa usando la métrica por defecto (accuracy para clasificación).
# Se puede usar con cualquier modelo o pipeline.

# TEMA 12: Métricas de evaluación de modelos de clasificación

# Cuando entrenas un modelo, no basta con ver el accuracy (precisión general). A veces necesitas saber más:
# ¿Cuántos positivos reales detectó?
# ¿Cuántos falsos positivos dio?
# ¿Cómo fue su equilibrio entre precisión y cobertura?

# Paso 1: Entrenar un modelo
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Paso 2: Métricas básicas
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("Accuracy:", accuracy_score(y_test, y_pred))       # Qué tanto acertó en general
print("Precision:", precision_score(y_test, y_pred, average='macro'))  # Qué tan precisas fueron sus predicciones
print("Recall:", recall_score(y_test, y_pred, average='macro'))        # Cuántos positivos reales encontró
print("F1 Score:", f1_score(y_test, y_pred, average='macro'))          # Equilibrio entre precisión y recall
# average='macro' hace el promedio de todas las clases (útil para datasets multiclase como iris).

# Paso 3: Matriz de confusión
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

matriz = confusion_matrix(y_test, y_pred)
sns.heatmap(matriz, annot=True, cmap="Blues", fmt="d")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.title("Matriz de Confusión")
plt.show()

#  La matriz muestra cuántos casos reales fueron clasificados correctamente (diagonal) o mal (fuera de la diagonal).

# Paso 4: Reporte detallado
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
# Te muestra precisión, recall y F1 para cada clase (muy útil para clasificaciones multiclase).

# Resumen
# Métrica	¿Qué mide?
# Accuracy	% total de aciertos
# Precision	% de predicciones positivas que eran correctas
# Recall	% de casos positivos reales que fueron detectados
# F1-Score	Media entre precisión y recall
# Confusion Matrix	Visualiza aciertos y errores por clase

# Clasificadores más usados en Scikit-learn (con ejemplos claros)
# Te voy a mostrar los modelos más comunes para clasificación en scikit-learn, cómo se usan y qué hacen. Todos usan la misma estructura:
modelo = CLASIFICADOR()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)

# 1. K-Nearest Neighbors (KNN) – El más intuitivo
from sklearn.neighbors import KNeighborsClassifier

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Clasifica observando a los k vecinos más cercanos.

# 2. Decision Tree – Árbol de decisiones
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Aprende reglas tipo "si pasa esto, entonces haz esto". Fácil de entender visualmente.

# 3. Random Forest – Muchos árboles trabajando juntos
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Usa varios árboles y vota cuál es la mejor predicción. Muy preciso.

# 4. Support Vector Machine (SVM) – Líneas que separan clases
from sklearn.svm import SVC

modelo = SVC(kernel='linear')  # También puede ser 'rbf', 'poly'
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Encuentra la mejor línea (o plano) que separa las clases.

# 5. Logistic Regression – Para probabilidades y clasificación binaria
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Aunque se llama "regresión", se usa mucho para clasificar.

# ¿Cómo compararlos?
from sklearn.metrics import accuracy_score

modelos = [
    ("KNN", KNeighborsClassifier()),
    ("Árbol", DecisionTreeClassifier()),
    ("Bosque", RandomForestClassifier()),
    ("SVM", SVC()),
    ("Logística", LogisticRegression(max_iter=200))
]

for nombre, modelo in modelos:
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print(f"{nombre}: {accuracy_score(y_test, y_pred):.2f}")

# ¿Cuál elegir?
# Modelo        | Ventaja Principal | Cuándo usarlo
# KNN           | Simple y rápido   | Pocos datos y fácil de entender
# Árbol         | Muy visual        | Datos con decisiones claras
# Random Forest | Precisión alta    | Datos con ruido o sin patrones simples
# SVM           | Muy potente en espacios pequeños | Datos bien separados
# Regresión Log.| Interpretable y rápido | Problemas binarios o multiclase simples

# TEMA 14: Regresores más usados en Scikit-learn (para predecir números)
# Cuando quieres predecir valores continuos (como precios, temperaturas, puntuaciones…), usas un regresor en lugar de un clasificador.
# 1. Linear Regression – Regresión lineal simple
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
#  Aprende una línea recta que mejor se ajuste a los datos.

# Ejemplo
# Si X_test = [[2], [4], [6]], entonces y_pred puede ser:
# [4.2, 7.8, 11.5]  ← valores numéricos estimados

# 2. Polynomial Regression – Regresión con curvas
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

modelo = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Ajusta curvas (no solo líneas rectas) a los datos.

# 3. Decision Tree Regressor – Árbol para regresión
from sklearn.tree import DecisionTreeRegressor

modelo = DecisionTreeRegressor()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Toma decisiones tipo "si X < 3, entonces predice 10".

# Toma decisiones tipo "si X < 3, entonces predice 10".
from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor(n_estimators=100)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
# Mezcla muchos árboles para una predicción más precisa.

# 5. Support Vector Regressor (SVR) – Separación con margen
from sklearn.svm import SVR

modelo = SVR(kernel='rbf')
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
#  Similar a SVM, pero ajustado para predecir números con margen.

# 6. Evaluar el rendimiento de modelos regresores
from sklearn.metrics import mean_squared_error, r2_score

print("MSE:", mean_squared_error(y_test, y_pred))  # Más bajo es mejor
print("R2:", r2_score(y_test, y_pred))  # Cerca de 1 es mejor

# Comparación rápida de varios regresores
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

modelos = [
    ("Lineal", LinearRegression()),
    ("Árbol", DecisionTreeRegressor()),
    ("Bosque", RandomForestRegressor(n_estimators=100))
]

for nombre, modelo in modelos:
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"{nombre}: MSE = {mse:.2f}")



