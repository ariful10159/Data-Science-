import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # Match length with 'area'
area = [1, 2, 3, 4, 5]  # Now both lists have the same length

plt.stackplot(x, area, labels=["Area"])
plt.legend()
plt.show()