import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

# Load the dataset
var = sns.load_dataset("tips")

# Create stripplot with corrected parameters
sns.stripplot(x="day", y="total_bill", data=var, hue="sex", palette="rocket_r",
              linewidth=1, edgecolor="r", size=5, alpha=0.5)

# Show the plot
plt.show()
