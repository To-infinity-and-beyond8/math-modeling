import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inte
import math
# Пределы изменяющейся переменной
# В данной задаче переменная - глубина погружения (z)
z = np.arange(0, 100, 1)
# Создаем диф. функцию для показателя преломления
def prelomlenie_function(n,z):
    dndz = alpha
# Коэффициент alpha — градиент показателя преломления
    return dndz
# Определить нач. условия и параметры
n_1 = 2 # граничное значение показателя преломления
n_0 = 1 # начальное значение показателя преломления
h = 100 # высота пластинок
alpha = (n_1 - n_0)*h
# Решение диф. уравнения
solve = inte.odeint(prelomlenie_function, n_0, z)
# Создаем диф. функцию для хода луча
def svet_function(x,z):
    math.sin(math.pi / 6)*n_0/n_1 = math.sin(ugol_prelomlenia)
    x = z * math.cos(ugol_prelomlenia) / math.sin(ugol_prelomlenia)
# закон Снеллиуса
# Определить нач. условия и параметры

    x_0 = 0
# Решение диф. уравнения
solvee = inte.odeint(svet_function, x_0, z)
# Построение решения
plt.plot(z, solvee[:, 0], color = 'r', label = 'График зависимости ')
plt.legend( loc ='upper left', borderaxespad=0)
plt.xlabel('X')
plt.ylabel('t')
plt.show()


