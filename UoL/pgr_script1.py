import os
os.chdir("c:\\Users\\nttdo\\learning.python\\UoL")
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("Dentistry_dashboard.csv")

#to extract year and month together into another column:
data['Start_year'] = pd.to_datetime(data['Start']).dt.year
data['End_year'] = pd.to_datetime(data['End']).dt.year
data['Start_month'] = pd.DatetimeIndex(data['Start']).month
data['End_month'] = pd.DatetimeIndex(data['End']).month

data['Start-ym'] = pd.to_datetime(data['Start']).dt.to_period('M')
data['End-ym'] = pd.to_datetime(data['End']).dt.to_period('M')

#d1 = data.groupby('Type').ESTS.value_counts()
#d2 = data.groupby('Fee status').Mode.value_counts()

#import numpy as np
#d3 = data.groupby(['Fee status']).agg(Mode=('Mode',np.count),total=('ESTS',np.count)) #NOT WORKING: says that np has not count

d3 = data.groupby('Fee status',as_index=False)['Mode'].count()
d3 = d3.rename(columns={"Mode": "Total PGRs"})

d4 = data.groupby('Mode').Start_year.value_counts()
d4 = d4.rename(columns={"Mode": "Total PGRs"})

# "More info on groupby: https://jamesrledoux.com/code/group-by-aggregate-pandas\n",
#     "grouped_multiple = df.groupby(['Team', 'Pos']).agg({'Age': ['mean', 'min', 'max']})\n",
#     "grouped_multiple.columns = ['age_mean', 'age_min', 'age_max']\n",
#     "grouped_multiple = grouped_multiple.reset_index()\n",
#     "print(grouped_multiple)\n",
#     "\n",
#     "This is also useful: https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts"

d5 = data.groupby(['Mode', 'ESTS', 'Start_year', 'End_year']).size()

new_PGRs = data.loc[data['Start_year'] == 2020]
new_PGRs.groupby(['Mode', 'ESTS', 'End_year', 'Type']).size()

current = data.loc[data['Start_year'] < 2020]
#out = current.groupby(['ESTS','Mode', 'Type']).size()

current_out = pd.DataFrame(current.groupby(['Fee status','Mode']).size(),columns=['Count'])
#current_out.to_csv('current.csv')
#current_out = current_out.append(current_out.agg(['sum']))


import matplotlib.pyplot as plt
current_out.plot(kind='bar', color='purple')
plt.xticks(rotation=90)
plt.gca().yaxis.grid()
#plt.gca().xaxis.grid()
plt.show()
#see this: https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart/48372659\n",
# for i in range(6): # your number of bars\n",
#     plt.text(x = x_values[i]-0.25, #takes your x values as horizontal positioning argument \n",
#     y = y_values[i]+1, #takes your y values as vertical positioning argument \n",
#     s = data_labels[i], # the labels you want to add to the data\n",
#     size = 9) # font size of datalabels"

