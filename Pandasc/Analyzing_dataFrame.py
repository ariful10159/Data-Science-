import pandas as pd 

df = pd.read_csv('data.csv')

print(df.head(10))



''' if the number of rows is not specified, the head() method will return the top 5 rows.
'''

print(df.tail())

print(df.info())