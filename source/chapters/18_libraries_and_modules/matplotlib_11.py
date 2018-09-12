"""
Create a pie chart
"""
import matplotlib.pyplot as plt

# Labels for the pie chart
labels = ['C', 'Java', 'Objective-C', 'C++', 'C#', 'PHP', 'Python']

# Sizes for each label. We use this to make a percent
sizes = [17, 14, 9, 6, 5, 3, 2.5]

# For list of colors, see:
# https://matplotlib.org/examples/color/named_colors.html
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'darkcyan', 'aquamarine', 'rosybrown']

# How far out to pull a slice. Normally zero.
explode = (0, 0.0, 0, 0, 0, 0, 0.2)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

# Finally, plot the chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.show()
