import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
plt.style.use("seaborn")

df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')    #live data
#local data on df = pd.read_csv('full_data.csv')

countries = ['United States', 'Italy', 'Spain', 'China', 'Pakistan', 'India']
x = np.arange(len(countries))
width = 0.35

filt = df['location'].isin(countries)
mydf = df[filt]

mydf = mydf.sort_values(by=['location', 'total_cases'], ascending=[True, False])

max_cases = []
max_death = []
for i in countries:
    temp_flt = mydf['location'] == i
    temp=mydf.loc[temp_flt]
    max_cases.append(temp.iloc[0, 4])
    max_death.append(temp.iloc[0, 5])

# countries.reverse()
# max_cases.reverse()

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, max_cases, width, label='Total Positive Cases')
rects2 = ax.bar(x + width/2, max_death, width, label='Total deaths')

# fig.autofmt_xdate()
ax.set_title("COVID19 Analysis")
ax.set_ylabel("Number of Population")
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)


plt.tight_layout()
plt.show()