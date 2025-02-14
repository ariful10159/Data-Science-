# Pandas dataframe 
import pandas as pd
data = {
    "Name ": ['   Ariful', 'islam' ,'Masum' ],
    "duration": [20, 40, 60]
}

df = pd.DataFrame(data)

print(df)

# located raw and coloum 
print(df.loc[0])

print(df.loc[[0,1,2]])

df = pd.DataFrame(data , index= ["day1","day2","day3"])
print(df)
print(df.loc["day2"])

#load files into a dataframe 

df1 = pd.read_csv('')
