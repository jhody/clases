# separa para entrenar y testear
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]  # Datos (inputs)
y = [2, 4, 6, 8,10,12,14,16,18,20]                      # Etiquetas (outputs deseados)

# Separar datos: 70% para entrenar, 30% para probar
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

print("Entrenamiento:", X_entrenamiento)
print("Prueba:", X_prueba)



frutas = [['manzana'], ['plátano'], ['uva'], ['fresa']]
colores = ['rojo', 'amarillo', 'morado', 'rojo']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(frutas, colores, test_size=0.5)

print("Frutas para entrenar:", X_train)
print("Colores para entrenar:", y_train)
print("Frutas para probar:", X_test)
print("Colores esperados:", y_test)

