import os
os.chdir("c:\\Users\\nttdo\\learning.python\\UoL")
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("Dentistry_Jan2021.csv")

#to extract year and month together into another column:
data['Start_year'] = pd.to_datetime(data['Start']).dt.year
data['End_year'] = pd.to_datetime(data['End']).dt.year
data['Start_month'] = pd.DatetimeIndex(data['Start']).month
data['End_month'] = pd.DatetimeIndex(data['End']).month

data['Start-ym'] = pd.to_datetime(data['Start']).dt.to_period('M')
data['End-ym'] = pd.to_datetime(data['End']).dt.to_period('M')

#new_PGRs = data.loc[data['Start_year'] == 2020]
#new_PGRs.groupby(['Mode', 'ESTS', 'End_year', 'Type']).size()

current = data.loc[data['End_year'] > 2020]
#out = current.groupby(['ESTS','Mode', 'Type']).size()

current_out = pd.DataFrame(current.groupby(['Fee status','Mode']).size(),columns=['Count'])
#current_out.to_csv('current.csv')
#current_out = current_out.append(current_out.agg(['sum']))

import matplotlib.pyplot as plt
current_out.plot(kind='bar', color='darkslateblue')
plt.xticks(rotation=90)
plt.gca().yaxis.grid()
#plt.gca().xaxis.grid()
plt.show()
