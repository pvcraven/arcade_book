"""
Annotating a graph
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.annotate('Here',
             xy = (2, 3),
             xycoords = 'data',
             xytext = (-40, 20),
             textcoords = 'offset points',
             arrowprops = dict(arrowstyle="->",
                               connectionstyle="arc,angleA=0,armA=30,rad=10"),
             )

plt.plot(x, y)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
