import matplotlib.pyplot as plt 

day = [1,2,3,4,5,6,7]
no  = [2,3,1,4,5,3,6]
no2 = [3,5,0,4,6,4,5]
color = ["r", "y", "g", "b", "r", "g", "m"]  # Fixed length to match data
sizes = [400, 200, 500, 600, 100, 900, 300]

plt.scatter(day, no, c=color, s=sizes,  edgecolors="g",cmap="viridis")  # Fixed errors
plt.scatter(day, no2, c=color, s=sizes,  edgecolors="r",cmap="viridis")  # Fixed errors

t=plt.colorbar()
t.set_label("ColorBar",fontsize=15)
plt.title("Scatter plot", fontsize=15)
plt.xlabel("Days", fontsize=15)
plt.ylabel("No", fontsize=15)
plt.show()
