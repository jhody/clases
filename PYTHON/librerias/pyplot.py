# usada para hacer gráficos en Python.

# Primer gráfico de línea
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()
# Dibuja una línea que conecta los puntos (1,10), (2,20), (3,25), (4,30)

# Personalizar el gráfico:
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.title("Crecimiento")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
# Cambia el color, el estilo de línea, y agrega título y etiquetas

# Graficar varias líneas
y2 = [5, 15, 20, 35]

plt.plot(x, y, label="Producto A")
plt.plot(x, y2, label="Producto B")
plt.legend()
plt.show()
# Muestra dos líneas con leyendas distintas

# Gráfico de barras
productos = ["A", "B", "C"]
ventas = [100, 150, 90]

plt.bar(productos, ventas)
plt.title("Ventas por producto")
plt.show()
# Muestra barras en lugar de líneas

# Gráfico de barras horizontales
plt.barh(productos, ventas, color='purple')
plt.title("Ventas por producto")
plt.show()
# Igual que el anterior pero con barras horizontales

# Gráfico de pastel (pie)
etiquetas = ["A", "B", "C"]
porcentajes = [40, 35, 25]

plt.pie(porcentajes, labels=etiquetas, autopct='%1.1f%%')
plt.title("Participación de mercado")
plt.show()
# Muestra una torta con los porcentajes

# Scatter Plot (Puntos dispersos)
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y)
plt.title("Valores dispersos")
plt.show()
# Muestra puntos sin unirlos con líneas

# Histograma
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Distribución")
plt.show()
# Muestra cómo se distribuyen los valores en rangos

# Subgráficos (subplot)
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Gráfico 1")

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [6, 5, 4])
plt.title("Gráfico 2")

plt.tight_layout()
plt.show()
# Crea 2 gráficos en una misma ventana

# Personalización avanzada
plt.plot(x, y, color='red', linewidth=2, linestyle='-', marker='*', markersize=10)
plt.title("Línea personalizada", fontsize=16)
plt.xlabel("Eje X", fontsize=12)
plt.ylabel("Eje Y", fontsize=12)
plt.grid(True, linestyle=':', linewidth=0.5)
plt.show()
# Total control de estilos de línea, fuente, y cuadrícula

# Guardar gráfico como imagen
plt.plot(x, y)
plt.savefig("grafico.png")
# Guarda la figura como archivo PNG en tu carpeta

# Estilo predefinido con plt.style
plt.style.use('ggplot')
plt.plot(x, y)
plt.title("Gráfico con estilo ggplot")
plt.show()
# Cambia automáticamente el estilo visual del gráfico



