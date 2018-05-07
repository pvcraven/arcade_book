"""
Line chart with four values.
The x-axis defaults to start at zero.
"""
import matplotlib.pyplot as plt

y = [1, 3, 8, 4]

plt.plot(y)
plt.ylabel('Element Value')
plt.xlabel('Element Number')

plt.show()
