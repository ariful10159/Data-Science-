import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 1, 4, 4, 6]

plt.plot(x, y)

# Provide 5 labels for 5 x-values
# plt.xticks(x, labels=["Python", "C", "C++", "Java", "JavaScript"])
# plt.yticks(x)

# plt.xlim(0,10)
# plt.ylim(0,10)

plt.axis([0,6,0,7])

plt.show()
