import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 2, 5, 7, 3, 4]

plt.stem(x, y, linefmt=":", markerfmt="ro", bottom=0, basefmt="g", label="python",orientation="horizontal")
plt.legend()
plt.show()
