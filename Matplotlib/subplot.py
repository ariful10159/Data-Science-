import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

plt.figure(figsize=(10, 8))  # Set figure size for better visibility

# Subplot 1: Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y, color="g")
plt.title("Line Plot")

# Subplot 2: Pie Chart (Fixed)
plt.subplot(2, 2, 2)
plt.pie([x[1]], labels=["Value"], colors=["r"])  # Fixed: List instead of a single value
plt.title("Pie Chart")

# Subplot 3: Bar Chart
plt.subplot(2, 2, 3)
plt.bar(x, y, color="y")
plt.title("Bar Chart")

# Subplot 4: Stack Plot
plt.subplot(2, 2, 4)
plt.stackplot(x, y, colors=["b"])
plt.title("Stack Plot")

plt.tight_layout()  # Adjust layout to prevent overlap

plt.savefig("4_figure132.jpg",dpi=2000,facecolor="y",transparent=True, bbox_inches="tight")
plt.show()

 