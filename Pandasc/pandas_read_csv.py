import pandas as pd 

df = pd.read_csv('data.csv')

print( df.to_string())

#max_rows 

print(pd.options.display.max_rows)
