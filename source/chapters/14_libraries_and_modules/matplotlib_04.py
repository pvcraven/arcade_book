
import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1, label = "Series 1")
plt.plot(x, y2, label = "Series 2")

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()
