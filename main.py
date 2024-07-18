import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import numpy as np

DIFF_INTERVAL = 0.01
X_LOWER = -5
X_UPPER = 5
Y_LOWER = 0
Y_UPPER = 10
MAX_V = 10

x, y = np.meshgrid(np.linspace(X_LOWER, X_UPPER, 100), np.linspace(Y_LOWER, Y_UPPER, 100))

# Complex potential
def F(z):
    return z**2

def phi(x, y):
    return np.real(F(x + 1j*y))

def psi(x, y):
    return np.imag(F(x + 1j*y))

def u(x, y):
    dFdz = (F(x+DIFF_INTERVAL + 1j*y) - F(x + 1j*y)) / DIFF_INTERVAL # df/dz = df/dx
    return np.real(dFdz), -np.imag(dFdz)

def plot_velocity():
    ux, uy = u(x, y)
    V = np.sqrt(ux**2 + uy**2)
    for i in range(len(V)):
        for j in range(len(V[i])):
            if V[i][j] > MAX_V:
                V[i][j] = MAX_V

    stream = plt.streamplot(x, y, ux, uy, density=2, linewidth=1, color=V, cmap=cm["Blues"])
    plt.colorbar(stream.lines)

def main():
    plot_velocity()
    plt.grid()
    plt.xlim(X_LOWER, X_UPPER)
    plt.ylim(Y_LOWER, Y_UPPER)
    plt.show()

if __name__ == "__main__":
    main()
