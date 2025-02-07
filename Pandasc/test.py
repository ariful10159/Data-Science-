import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('matches.csv')

#print(data.head(3))

#print(data.tail(2))

#print(data.shape)

#print(data.info())

#print(data.describe())

#print(data['winner']) 

#(type(data['winner']))

'''def city_count(city):
    mask = data['city']==city
    return data[mask].shape[0]

count = city_count('Rajkot')
print(f"Number of occurrences of 'Rajkot': {count}")

'''
'''result=data['city']=='Hyderabad'
print(result)'''

'''result= data['city']=='Hyderabad'
print(data[result])'''

'''result= data['city']=='Hyderabad'
print(data[result].shape[0])'''

'''result1 = data['city']=='Hyderabad'
result2 = data['date']>'2010-01-01'

print(data[result1 & result2])
print(data[result1 & result2].shape)'''


'''result3= data['winner'].value_counts()
print(result3)
'''
'''result4 = data['winner'].value_counts().plot(kind='bar')
print(result4)
plt.clf()


result5= data['toss_decision'].value_counts().plot(kind='pie')
print(result5)
plt.show()'''

#print((data['team2'].value_counts() + data['team1'].value_counts()).sort_values(ascending=False ))

'''result6 = data.drop_duplicates(subset=['city','season'])
print(result6)


result7 = data.drop_duplicates(subset=['city','season']).shape
print(result7)

result8=data.drop_duplicates('season',keep='last')[['season','winner']].sort_values('season')
print(result8)'''

data1 = pd.read_csv('deliveries.csv')

'''print(data1.shape)

runs = data1.groupby('batsman')
print(runs.get_group('V Kohli'))

print(runs['batsman_runs'].sum().sort_values(ascending=False).head())
'''
'''result9 = data1['batsman_runs']!=4
mask1= data1[result9]

print(mask1['batsman_runs'])'''

'''result9 = data1['batsman_runs']==6
mask1= data1[result9]

result10=mask1.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(5)

#result11 = result10.get_group('V Kohli')
#print(result10)

result11 = data1['batsman_runs']==6
mask3= data1[result11]

result12=mask3.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(5)

#result11 = result10.get_group('V Kohli')
result_v_kohli = result12[result12.index=='V Kohli']
print(result_v_kohli)

2010 WHICH TEAM MOST RUNS 

vk = data1[data1['batsman'] == 'V Kohli']
print(vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3))

'''
'''
#isin()
#Find the most destructive death over batsman in the history of IPL 
#Strike Rate = (Number of runs / Number of balls)/100
#Min batsman 200 balls in over 16 - 20

death_over=  data1[data1['over']>15]
all_batsman=death_over.groupby('batsman')['batsman_runs'].count()
x=all_batsman>200
batsman_list=all_batsman[x].index.tolist()
#runs scored by all these 43 batsman 
#balls played by these 43 batsman 

final = data1[data1['batsman'].isin(batsman_list)]
runs = final.groupby('batsman')['batsman_runs'].sum()
balls= final.groupby('batsman')['batsman_runs'].count()
sr = (runs/balls)*100
print(sr.sort_values(ascending=False).head(3))

'''













