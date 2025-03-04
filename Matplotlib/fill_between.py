import matplotlib.pyplot as plt 
import numpy as np 

x =np.array ([1,2,3,4,5])
y = np.array([5,2,5,3.5,5])

plt.plot(x,y,color= "r")

plt.fill_between(x,y,label="python",color="g",where=(x>=2) & (x<=4),alpha=1)
plt.xlabel("x- axis ")
plt.ylabel("y-axis ")
plt.title("python ")
plt.legend(loc=2)
plt.show()