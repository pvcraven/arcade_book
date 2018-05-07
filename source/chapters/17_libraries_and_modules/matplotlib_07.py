"""
How to do a bar chart.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.bar(x, y)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
