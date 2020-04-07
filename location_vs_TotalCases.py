import pandas as pd 
from matplotlib import pyplot as plt 
plt.style.use("seaborn")

df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')    #live data
#local data on df = pd.read_csv('full_data.csv')

countries = ['United States', 'Italy', 'China', 'Spain', 'Pakistan', 'India']
filt = df['location'].isin(countries)
mydf = df[filt]

mydf = mydf.sort_values(by=['location', 'total_cases'], ascending=[True, False])

max_cases = []
for i in countries:
    temp_flt = mydf['location'] == i
    temp=mydf.loc[temp_flt]
    max_cases.append(temp.iloc[0, 4])
	


countries.reverse()
max_cases.reverse()

ax = (result.div(result.sum(1), axis=0)).plot(kind='bar',figsize=(15,4),width = 0.8,color = colors_list,edgecolor=None)
plt.legend(labels=result.columns,fontsize= 14)
plt.title("Percentage of Respondents' Interest in Data Science Areas",fontsize= 16)

plt.xticks(fontsize=14)
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])

# Add this loop to add the annotations
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate('{:.0%}'.format(height), (x, y + height + 0.01))

# data = [0.01, 0.56, 0.76, 0.77, 0.55, 0.99]
# plt.barh(countries, max_cases)

# plt.gcf().autofmt_xdate()
# plt.title("Country Analysis")
# plt.xlabel("Number of Positive cases")
# plt.tight_layout()
# plt.show()