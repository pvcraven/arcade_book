"""
This shows how to set line style and markers.
"""
import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

# First character: Line style
# One of '-', '--',  '-.', ':', 'None', ' ', "

# Second character: color
# http://matplotlib.org/1.4.2/api/colors_api.html

# Third character: marker shape
# http://matplotlib.org/1.4.2/api/markers_api.html

plt.plot(x, y1, '-ro')
plt.plot(x, y2, '--g^')

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
