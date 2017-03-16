"""
This example shows graphing two different series
on the same graph.
"""
import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1)
plt.plot(x, y2)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()

