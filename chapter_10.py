import numpy as np
import matplotlib.pyplot as plt

def crazy_plot(t):
    x = np.sin(t) + .5*np.sin(5*t) + .25*np.cos(2.3*t)
    y = np.cos(t) + .5*np.cos(5*t) + .25*np.sin(2.3*t)
    return x, y


t = np.linspace(0, np.pi*24, 100000)
x, y = crazy_plot(t)

# plt.plot(x, y)
# plt.show()


def polar_2_cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.array(x), np.array(y)


def funky_r(theta):
    r1 = np.sin(1.2*theta)**2
    r2 = np.cos(6*theta)**3
    return r1 + r2

N = 1000000
theta = np.linspace(0, 20*np.pi, N)
r = funky_r(theta)

x, y = polar_2_cart(r, theta)

plt.plot(x, y)
plt.show()
















#
