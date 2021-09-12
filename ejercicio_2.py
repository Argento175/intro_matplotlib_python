# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
# NOTA: aproveche los ejemplos "multi_line_plot" de clase

# Alumno: Se desea graficar varias funciones en un mismmo gráfico (axe)

import numpy as np
import matplotlib.pyplot as plt

# Las funciones que se desean implementar y graficar son:
# y1 = x**2
# y2 = x**3

# Su implementación es la siguiente:
def grafico_2():
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)


    fig = plt.figure()
    fig.suptitle('Gráfico 2',c= 'darkblue', fontsize=20)
    ax = fig.add_subplot()

    ax.plot(x, y1,c='green', label='Y 1')
    ax.plot(x, y2,c='magenta', label='Y 2')
    ax.plot(x, x,c='black', label='x')
    ax.legend()
    ax.grid()
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico
    grafico_2()

    print("terminamos")