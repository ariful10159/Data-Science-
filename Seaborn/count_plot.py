import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

# Load the dataset
var = sns.load_dataset("tips")

# Create a barplot
# sns.barplot(x="sex", y="size", data=var)
sns.countplot(x="sex", data=var,hue="smoker",color="r")

# Show the plot
plt.show()