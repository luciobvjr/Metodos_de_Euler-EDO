import numpy as np
from matplotlib import pyplot as plt

def F(x,y): #y'
    f = y + np.cos(y) - x 
    return f

def Euler_aperfeicoado():
    h = float(input('Valor de h = '))
    xbar = float(input('Valor de x = '))
    n = (xbar - 1) / h 
    n = int(n)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = 1
    y[0] = 2

    for i in np.arange(0,n):
        x[i+1] = x[i] + h
        k1 = F(x[i],y[i])
        k2 = F(x[i+1],y[i] + h*k1)
        y[i+1] = y[i] + (h/2) * (k1 + k2)

    print('O valor de y correspondente =',y[-1])
    plt.plot(x,y)
    plt.show()

Euler_aperfeicoado()