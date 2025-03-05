import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y =  [1,2,3,4,5]

plt.step(x,y,color="r", marker = "o", ms= 15, mfc = "g",label= "python")
plt.xlabel("x - axis ", fontsize=15)
plt.ylabel("y - axis ")
plt.title("Python")
plt.legend(loc = 3)
plt.show()