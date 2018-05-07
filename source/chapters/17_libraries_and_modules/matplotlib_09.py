"""
Using the numpy package to graph a function over
a range of values.
"""
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0.0, 2.0, 0.001)
y = numpy.sin(2 * numpy.pi * x)

plt.plot(x, y)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
