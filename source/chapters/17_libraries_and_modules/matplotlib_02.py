"""
Line chart with four values.
The x-axis values are specified as well.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.plot(x, y)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
