
import pandas as pd
from icecream import ic

df = pd.read_csv("C:\\Users\\Pradeep_Avadhanam\\Workspace\\pythonProject\\dataframes\\data\\nba.csv")
print(df.head())
print(df.Name,df['Team'])
print(df[['Name','Weight','Salary']])
print(df.shape)
print(df.info)
ic(df.to_json(orient='records'))
#Basic Analysis
ic(df.Age.value_counts(dropna=False))
ic(df.Position.value_counts(ascending=True))
#sort
ic(df.sort_values(by=['College','Name']))
#Boolean indexing
ic(df[df.Age == 19])
#string handling
ic(df[df.Name.str.contains('Walter')])
#get count of each positions for team 'Phoenix Suns'
ps = df[df.Team == 'Phoenix Suns']
ic(ps.Position.value_counts())
#Which college won most 'PF' positions of college 'LSU' and sort by 'Names'
lsu = df[(df.Position == 'PF') & (df.College == 'LSU')]
ic(lsu.sort_values(by='Name'))
#Which 5 Names weight is >200
wt = df[df.Weight >= 200]
ic(wt.value_counts().head(5))
#Which team has most 'PF' Number >45 and sort by highest Salary
pos = df[(df.Position == "PF") & (df.Number >= 45)]
ic(pos.sort_values(by='Salary',ascending=False)[['Name','Salary','Number','Position']])

#Indexing
name = df.set_index('Name')
ic(name.head())
(name.sort_index(inplace=True,ascending=False))
ic(name.head())
ic(name.loc['Wilson Chandler'])
ic(df.iloc[1:3])
ic(df.Team.value_counts().sort_index())
ic(df[df.College.isnull()])

#GroupBy
gb = df.groupby('College')
# ic(list(gb))
# for key,value in gb:
#     ic(key)
#     ic(value)

print(df.groupby(['Salary']).agg('count').tail())
print(df.groupby(['Team']).agg({'Age':['min','max','count']}))
print([df.groupby(['Team','Position']).agg({'Position':['count']})])
ic(df.groupby('Team').size())
#unstacking
ps = df.groupby(['Team','Position']).size().unstack('Position',fill_value=0)
ps['Total'] = ps['C'] + ps['PF'] + ps['SF'] + ps['SG'] + ps['PG']
# ps = ps.sort_values('Total', ascending=False)
ps.reset_index(inplace=True)

# for tm in ps.groupby('Team'):
#     print(tm.sort_values('Team', ascending=False))
print(ps)