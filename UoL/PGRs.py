#plot graph based on covid data as vsc data_file
import os
os.chdir("c:\\Users\\nttdo\\learning.python\\UoL")
import pandas as pd
import matplotlib.pyplot as plt 
data = pd.read_csv("data.csv")
#print(data.dtypes)
uk = data.loc[(data.countriesAndTerritories.str.contains("United_Kingdom"))]
plt.plot(uk["year_week"], uk["deaths_weekly"], color='red', label="UK")
be = data.loc[(data.countriesAndTerritories.str.contains("Belgium"))]
plt.plot(be["year_week"], be["deaths_weekly"], color='purple', label="Belgium")

#Fr = data.loc[(data.countriesAndTerritories.str.contains("France"))]
#plt.plot(Fr["year_week"], Fr["deaths_weekly"], color='blue', label="France")
#sw = data.loc[(data.countriesAndTerritories.str.contains("Switzerland"))]
#plt.plot(sw["year_week"], sw["deaths_weekly"], color='green', label="Switzerland")
#usa = data.loc[(data.countriesAndTerritories.str.contains("United_States"))]
#plt.plot(usa["year_week"], usa["deaths_weekly"], color='black', label="USA")
plt.legend() #this needs to be present, otherwise the labels don't show.
####################
#TRYING TO ADJUST THE X AXIS LABELS (TICKS) TO REDUCE THEIR NUMBERS
# To specify the number of ticks on both or any single axes
#plt.locator_params(axis='y', nbins=6)
#plt.locator_params(axis='x', nbins=6) #####did not work for me...

#import numpy as np
#plt.xticks(np.arange(12), uk['year_week']) #what this does is only plot the y data for each of the shown x data. It 
#does not plot the whole data but the corresponding y data for the displayed x-ticks only, which could be useful to know.

# ax.xaxis.set_major_locator(plt.MaxNLocator(6))
#Would set the total number of ticks in the x-axis to 3, and evenly distribute it across the axis.

#plt.locator_params(numticks=12) #this apprently only works when a log scale is used.
#plt.locator_params(nticks=3)
####################
#THIS WORKED!!!!! got from here: https://stackoverflow.com/questions/6682784/reducing-number-of-plot-ticks
N = 3  # 1 tick every 3
xticks_pos, xticks_labels = plt.xticks()  # get all axis ticks
myticks = [i for i,j in enumerate(xticks_pos) if not i%N]  # index of selected ticks
plt.gca().set_xticks(myticks)  # set new X axis ticks
####################
plt.title("Weekly deaths in selected countries.")
plt.ylabel('Number of deaths')
plt.xlabel('Week number')
plt.gcf().autofmt_xdate()
plt.gca().invert_xaxis()
plt.gca().yaxis.grid()
plt.gca().xaxis.grid()
#plt.show()
plt.savefig('fig1.png')