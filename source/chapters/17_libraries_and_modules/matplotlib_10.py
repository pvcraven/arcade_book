"""
Using 'fill' to fill in a graph
"""
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0.0, 2.0, 0.001)
y = numpy.sin(2 * numpy.pi * x)

plt.plot(x, y)

# 'b' means blue. 'alpha' is the transparency.
plt.fill(x, y, 'b', alpha=0.3)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
