import math
import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return 2*x*y

def euler(y0,fx,h,f):
    y=[]
    y.append(y0)
    for i in range(1,len(x)):
        y.append ( y[i-1] + h*f(x[i-1],y[i-1]) )
    return y


n = 6
a = 1
b = 1.5
h = abs(a-b)/(n-1)
x = np.linspace(a,b,n)


y = euler(1,x,h,f)

plt.plot(x,y,'b')
plt.grid()

print('Valor de h: ', h)

print ('Valor final de x: ',x[-1])
print ('Valor final de y: ',y[-1])

"""
Resultados:
Valor de h:  0.1
Valor final de x:  1.5
Valor final de y:  2.9278126080000004
"""
