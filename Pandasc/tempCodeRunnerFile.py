vk = data1[data1['batsman']=='V Kholi']
print(vk.groupby('bowling_team')['batsman_run'].sum().sort_values(ascending=False).head(3))



