# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:38 2021

@author: chris
"""
import matplotlib.pyplot as plt
from main import attribut2dataframe
import numpy as np
#from cycler import cycler

att_file = 'C:/Users/chris/proj-lvm_files/Strecken_UAM4.att'
# path = 'C:/Users/chris/proj-lvm_files/EinsteigerVSySDiff.att'

df = attribut2dataframe(att_file)

df = df[df['TSYSSET']=='UAM200']





df.rename(columns={'CM_UAM_OHNETICKET': 'No Ticket',
                   'CM_UAM_NULLFALL_0EURO': '0',
                   'CM_UAM_50EURO': '50',
                   'CM_UAM_100EURO': '100',
                   'CM_UAM_500EURO': '500',
                   'CM_UAM_10000EURO': '10000',
                   'LENGTH': 'LENGTH_km'
                   }, inplace=True)
df['LENGTH_km'] = df['LENGTH_km'].str[:-2].astype(np.double)

df.sort_values(by='No Ticket', ascending=False, inplace=True, kind='quicksort', na_position='last')


box_cols = ['No Ticket', '0', '50', '100', '500', '10000']

df.boxplot(column = box_cols)
plt.title('Urban Air Mobility Passengers')
plt.ylabel('Count: Network Passengers [Pax/day]')
plt.xlabel('Fare: Added Fixed Costs [€]')
plt.savefig('boxplot.png')
plt.clf()

print(list(df.columns))

new_box_cols = []

for my_col in box_cols:
    new_col_name = my_col + '_w'
    new_col_sum = my_col + '_sum'
    new_box_cols.append(new_col_name)
    df[new_col_name] = ( (df[my_col] * df['LENGTH_km']) / df['LENGTH_km'].sum() )
    df[new_col_sum] = df[my_col].sum() 




df.boxplot(column = new_box_cols)
plt.title('Urban Air Mobility Passengers Weighted with Distance')
plt.ylabel('Count: Network Passengers [Pax/day]')
plt.xlabel('Fare: Added Fixed Costs [€]')
plt.savefig('boxplot_weighted_distance_TEMP.png')
plt.clf()


value_cols = []
edge_names = []



for index, row in df[box_cols].iterrows():
    # print(row)
    value_cols.append(row.values.tolist())
    
    
# todo: Nur einmal iterieren!!

for index, row in df[['NAME']].iterrows():
    print(row.to_numpy()[0])
    edge_names.append(row.to_numpy()[0])
    

n = len(df.index)

fig, ax0 = plt.subplots(nrows=1)

color=iter(plt.cm.rainbow(np.linspace(0,1,n)))

for data in zip(value_cols, edge_names):
    c=next(color)
    plt.plot(box_cols, data[0], label = data[1], c=c)

# ax0.set_prop_cycle

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=False, ncol=5)  
plt.title('Urban Air Mobility Passengers')
plt.ylabel('Count: Network Passengers [Pax/day]')
plt.xlabel('Fare: Added Fixed Costs [€]')

#print(list(df.columns))
print(edge_names)