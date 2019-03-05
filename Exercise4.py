# ZADANIE 4
from numpy import *
from matplotlib.pyplot import *


def createPlot(a):
    arr = []
    x = linspace(0, a, 200)
    for i in x:
        y = sin(i) * i
        arr.append(y)
    plot(arr)
    xlabel('x')
    ylabel('y')
    show()

createPlot(100)