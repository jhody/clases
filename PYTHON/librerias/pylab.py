# es una combinación de funciones de matplotlib.pyplot y numpy, pensada para un estilo de trabajo similar a MATLAB.
#  Nota: Aunque pylab es útil para aprender, hoy se recomienda usar directamente matplotlib.pyplot y numpy separados por claridad. Aun así, vamos a aprenderlo.
# from pylab import *

# Carga todas las funciones de matplotlib y numpy
# x = linspace(0, 10, 100)  # 100 puntos entre 0 y 10
y = sin(x)

plot(x, y)
show()
# Muestra la curva seno

# Personalizar el gráfico
plot(x, y, 'r--')  # línea roja punteada
title("Seno de x")
xlabel("x")
ylabel("sin(x)")
grid(True)
show()
# Gráfico personalizado con color y etiquetas

# Gráfico de barras
nombres = ['A', 'B', 'C']
valores = [5, 8, 6]

bar(nombres, valores)
show()
# Muestra un gráfico de barras

# Gráfico de dispersión (scatter)
x = randn(100)
y = randn(100)

scatter(x, y)
show()
# Muestra puntos distribuidos al azar

# Varios gráficos juntos
subplot(2, 1, 1)
plot(x, y)
title("Gráfico 1")

subplot(2, 1, 2)
hist(x, bins=20)
title("Histograma")

show()
# Muestra dos gráficos en una sola ventana

# Funciones matemáticas
x = linspace(-2*pi, 2*pi, 200)
y1 = sin(x)
y2 = cos(x)

plot(x, y1, label='sin(x)')
plot(x, y2, label='cos(x)')
legend()
show()
# Muestra dos funciones en el mismo gráfico

# Guardar gráfico
plot(x, y1)
savefig("grafico_pylab.png")
# Guarda el gráfico como imagen PNG

# Estilos y colores rápidos
plot(x, y1, 'g-')  # línea verde
plot(x, y2, 'b:')  # línea azul punteada
show()
# Estilo de línea definido en un solo string

# Interactividad básica
ion()  # modo interactivo
plot([1, 2, 3], [4, 5, 6])
draw()
# Permite modificar el gráfico en tiempo real (útil para scripts largos)


