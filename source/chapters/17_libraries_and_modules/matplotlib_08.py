"""
How to add x axis value labels.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.plot(x, y)

labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']
plt.xticks(x, labels)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
