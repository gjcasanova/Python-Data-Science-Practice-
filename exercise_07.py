import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    with np.errstate(invalid='ignore'):
        return np.sqrt(1-np.power((abs(x)-1), 2))


def f2(x):
    with np.errstate(invalid='ignore'):
        return np.arccos(1-abs(x)) - np.pi


def main():
    x = np.arange(start=-10.0, stop=10.01, step=0.01)
    y_1 = f1(x)
    y_2 = f2(x)
    plt.plot(x, y_1, color='green', label='f1')
    plt.plot(x, y_2, color='red', label='f2')
    plt.legend(['f1(x)', 'f2(x)'])
    plt.xlim((-2, 2))
    plt.ylim((-3, 1))
    plt.show()


if __name__ == '__main__':
    main()
