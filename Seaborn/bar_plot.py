import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

var = sns.load_dataset("penguins")
# sns.set(style="darkgrid")
# print(var.head())
# sns.barplot(x=var.island ,y = var.bill_length_mm,color="g",palette="a")
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island" ,y = "bill_length_mm",data= var,hue="sex",order=order_1,hue_order=["Female","Male"]
            , ci=100,n_boot=2,orient="v",saturation=10,errcolor="y",errwidth=10,capsize=0.2,alpha=1)


plt.show()