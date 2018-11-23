import numpy as np
import matplotlib.pyplot as plit

def y(x):
    return 2*x**2 - 5*x + 3

xarray = np.linspace(0,5,100)
yarray = np.zeros(len(xarray))

for i in range(len(xarray)):
    yarray[i] = y(xarray[i])

plit.plot(xarray,yarray)
plit.grid()
