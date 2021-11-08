import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.sqrt(1 - np.power(abs(x)-1, 2))


def f2(x):
    return np.arccos(1-abs(x)) - np.pi


def main():
    # Generamos valores en X
    x = np.arange(start=-10, stop=10.01, step=0.01)
    # Calculamos Y para f1 y f2
    y_1 = f1(x)
    y_2 = f2(x)
    # Configurar el grafica
    plt.plot(x, y_1, color='green', label='f1')
    plt.plot(x, y_2, color='red', label='f2')
    plt.legend()
    plt.xlim((-2, 2))
    plt.ylim((-3, 1))
    # Mostramos
    plt.show()


if __name__ == '__main__':
    main()
