from scipy.optimize import fsolve
from matplotlib import pyplot as plt
import numpy as np

def F(x,y): #y'
    f = y + np.cos(y) - x 
    return f

def F_newton(yf,xf,y0,h):
    return yf - y0 - h*(yf + np.cos(yf) - xf)

def Euler_implicito():
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
        y[i+1] = y[i] + h * F(x[i+1],fsolve(F_newton,[y[i]],(x[i+1],y[i],h)))
    
    print('O valor de y correspondente =',y[-1])
    plt.plot(x,y)
    plt.show()

Euler_implicito()