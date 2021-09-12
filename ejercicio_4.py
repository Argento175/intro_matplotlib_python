# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def grafico_4():
    x = np.linspace(-10, 10, 40)
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)


    fig = plt.figure()
    fig.suptitle('Gráficos generales',c='darkblue', fontsize=20)
    ax = fig.add_subplot()

    ax1 = fig.add_subplot(1, 1, 1)  
    ax2 = fig.add_subplot(1, 2, 2)  
    ax3 = fig.add_subplot(2, 1, 1)  
    ax4 = fig.add_subplot(2, 2, 2) 
    ax1.plot(y1,c='black',label='función: cuadrática')
    ax1.legend()
    ax1.grid()
    ax2.plot(y2,c='magenta',label='función: cúbica')
    ax2.legend()
    ax2.grid()
    ax3.plot(y3,c='green',label='función: a la cuarta')
    ax3.legend()
    ax3.grid()
    ax4.plot(y4,c='blue',label='función: raíz cuadrada')
    ax4.legend()
    ax4.grid()
    plt.show()
    print("Fin de presentación...")



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Alumnos: Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    # x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    # y1 = x**2
    # y2 = x**3
    # y3 = x**4
    # y4 = np.sqrt(x)

    # Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    grafico_4()
    print("terminamos")
