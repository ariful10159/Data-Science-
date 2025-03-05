import matplotlib.pyplot as plt

# Corrected data (fixed missing comma)
x = [35, 16, 40, 59, 23, 10, 17, 42, 24, 40, 24, 58, 12, 42, 21, 59, 55, 46, 24, 26, 30, 44, 31, 59,
     28, 37, 53, 28, 46, 29, 17, 27, 55, 29, 44, 28, 45, 18, 20, 46, 43, 53, 59, 47, 45, 34, 15, 21,
     56, 59]

# Define bins
bins = [10, 20, 30, 40, 50, 60]  

# Create histogram
plt.hist(x, bins=bins, color="b", edgecolor="r", rwidth=1.2)

# Add labels and title
plt.xlabel("Value Ranges", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram Plot", fontsize=14)

# Show plot
plt.axvline(45,color="g",label="line")
plt.legend()
plt.grid()
plt.show()
