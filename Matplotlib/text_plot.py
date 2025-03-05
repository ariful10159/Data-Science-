import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 5, 4, 5]

plt.plot(x, y)
plt.xlabel("Days")
plt.ylabel("Python")
plt.title("Wscube")

# Adding text at a specific point
plt.text(2, 3, "python", fontsize=15, style="italic", bbox={"facecolor": "red"})

# Annotating a point with an arrow
plt.annotate("python", xy=(2, 1), xytext=(3, 3), 
                                         arrowprops=dict(facecolor="black", shrink=0.05))

plt.show()
