import matplotlib.pyplot as plt
import numpy as np

x = ["Python", "C", "C++", "Java"]
y = [80, 70, 60, 82]
z = [20, 30, 40, 50]

height = 0.2  # Adjusted bar height for better spacing
p = np.arange(len(x))
p1 = [j + height for j in p]

plt.ylabel("Language", fontsize=20)  # Label for y-axis (since it's horizontal)
plt.xlabel("No", fontsize=20)  # Label for x-axis
plt.title("Wscube", fontsize=20)  # Title of the chart

plt.barh(p, y, height, color="r", label="Popularity")
plt.barh(p1, z, height, color="y", label="Popularity1")

plt.yticks(p + height / 2, x, rotation=10)  # Adjusted for better readability

plt.legend()
plt.show()  # Display the chart
