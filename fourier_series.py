import random
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_an(f, n):
    """Calcula o a_n da série de Fourier."""
    return 1/sp.pi * sp.integrate(f * sp.cos(n * x), (x, -sp.pi, sp.pi))

def get_bn(f, n):
    """Calcula o b_n da série de Fourier."""
    return 1/sp.pi * sp.integrate(f * sp.sin(n * x), (x, -sp.pi, sp.pi))

def fourier_series(a0, an, bn, n, x_value):
    """Calcula a soma parcial da série de Fourier."""
    fourier_sum = a0/2
    for i in range(1, n + 1):
        fourier_sum += an[i-1] * sp.cos(i * x_value) + bn[i-1] * sp.sin(i * x_value)
    return fourier_sum

def update_plot(n):
    """Atualiza o gráfico."""
    y_fourier = [fourier_series(a0, an, bn, n, x_value) for x_value in x_axis]
    print(f'Calculando n = {n}')
    ax.clear()
    ax.plot(x_axis, y_original)
    ax.plot(x_axis, y_fourier)
    ax.set_title(f'n = {n}')
    ax.set_ylim([-5, 5])
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Variável independente
x = sp.symbols('x')

# Função
f = sp.Piecewise((-1, (x > -sp.pi) & (x < 0)), (1, (x > 0) & (x < sp.pi)))

# Número de termos
n = 10

# Computa os valores de a_0, a_n e b_n
a0 = 1/sp.pi * sp.integrate(f, (x, -sp.pi, sp.pi))
an = [get_an(f, n).evalf() for n in range(1, n + 1)]
bn = [get_bn(f, n).evalf() for n in range(1, n + 1)]

# Gera os valores do eixo x e y
x_axis = [i * 0.01 for i in range(-314, 315)]
y_original = [sp.lambdify(x, f, 'math')(x_value) for x_value in x_axis]

# Gera o gráfico
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update_plot, frames=range(1, n + 1), interval=250)

# Salva o arquivo .gif
PATH = f'gifs/graph_approximation{random.randint(1, 10000)}.gif'
ani.save(PATH, writer='imagemagick', fps=2)
plt.show()