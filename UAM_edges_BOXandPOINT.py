# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:38 2021

@author: chris
"""
import matplotlib.pyplot as plt
from main import attribut2dataframe, att_path, pdf_path, svg_path
import numpy as np

act_ver = 'v4p2'

att_file = att_path('C:/Users/chris/proj-lvm_files/Strecken_UAM_', act_ver)

UAMcap4 = 4 * 24 * 4
UAMcap7 = 4 * 24 * 7


df = attribut2dataframe(att_file, False)#[0, 1, 2])

df = df[df['TSYSSET']=='UAM200']

#print(df)


#rename_dict_V2 = {'CM_UAM_NULLFALL_0EURO_V2': '0', 'CM_UAM_50EURO_V2': '50', 'CM_UAM_100EURO_V2': '100', 'CM_UAM_250EURO_V2': '250', 'CM_UAM_500EURO_V2': '500', 'CM_UAM_10000EURO_V2': '10000', 'LENGTH': 'LENGTH_km'}
# rename_dict_V3 = {'CM_UAM_NULLFALL_0EURO_V3': '0', 'CM_UAM_50EURO_V3': '50', 'CM_UAM_100EURO_V3': '100', 'CM_UAM_250EURO_V3': '250', 'CM_UAM_500EURO_V3': '500', 'CM_UAM_10000EURO_V3': '10000', 'LENGTH': 'LENGTH_km'}
#rename_dict_V3 = {'CM_UAM_NULLFALL_0EURO_V4': '0', 'CM_UAM_50EURO_V4': '50', 'CM_UAM_100EURO_V4': '100', 'CM_UAM_250EURO_V4': '250', 'CM_UAM_500EURO_V4': '500', 'CM_UAM_1000EURO_V4': '1000', 'LENGTH': 'LENGTH_km'}
rename_dict_V4p2 = {'BELPERS-OEV_AP__CM11M0_V4P2': '0', 'BELPERS-OEV_AP__CM11M50_V4P2': '50', 'BELPERS-OEV_AP__CM11M100_V4P2': '100', 
                  'BELPERS-OEV_AP__CM11M250_V4P2': '250', 'BELPERS-OEV_AP__CM11M500_V4P2': '500', 'BELPERS-OEV_AP__CM11M1000_V4P2': '1000', 
                  'LENGTH': 'LENGTH_km'}



df.rename(columns = rename_dict_V4p2, inplace=True)

# if unit is also exported from Visum...:
# df['LENGTH_km'] = df['LENGTH_km'].str[:-2].astype(np.double)

df.sort_values(by='0', ascending=False, inplace=True, kind='quicksort', na_position='last')

# box_cols = ['0', '50', '100', '250', '500', '10000']
box_cols = ['0', '50', '100', '250', '500', '1000']

df.boxplot(column = box_cols, whis=(0, 100))
plt.title('Price-sensitive Occupancy of Drone Connections')
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)

# Line repr. maximum capacity
plt.axhline(y = UAMcap4, color = 'r', linestyle = '-', label = '4-seater')
plt.axhline(y = UAMcap7, color = 'b', linestyle = '-', label = '7-seater')

plt.legend(loc='upper center', title='Maximum Capacity [PAX/day]', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4)


plt.savefig(svg_path('plots/boxplot_PAXvsFARE_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/boxplot_PAXvsFARE_', act_ver), bbox_inches="tight")




plt.clf()


# todo: Weight with something...

new_box_cols = []

for my_col in box_cols:
    new_col_name = my_col + '_w'
    new_col_sum = my_col + '_sum'
    new_box_cols.append(new_col_name)
    # df[new_col_name] = ( (df[my_col] * df['LENGTH_km']) / df['LENGTH_km'].sum() )
    # df[new_col_name] =  (df[my_col] / df['LENGTH_km']) 
    df[new_col_name] =  np.minimum(df[my_col], 500.0) 
    df[new_col_sum] = df[my_col].sum()

df.boxplot(column = new_box_cols, whis=(0, 100) )
plt.title('Price-sensitive Occupancy of Drone Connections')
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
# plt.ylim(0, 750)

# don't plot solange nicht fertig
# plt.savefig('plots/boxplot_weighted_distance_TEMP.svg', bbox_inches="tight")
# plt.savefig('plots/boxplot_weighted_distance_TEMP.pdf', bbox_inches="tight")
plt.clf()


# todo: transpose, not iter...

value_cols = []
edge_names = []

for index, row in df[box_cols].iterrows():
    
    ## use real traffic load (PAX per link) from model ##
    value_cols.append(row.values.tolist())
    
    ## use maximum capacity PAX (~500) instead of real value ##
    # value_cols.append( np.minimum(row.values, 500.0) )
    
    
# todo: Nur einmal iterieren!!


for index, row in df[['NAME']].iterrows():
    # print(row.to_numpy()[0])
    edge_names.append(row.to_numpy()[0])
    

n = len(df.index)

fig, ax0 = plt.subplots(nrows=1)

color=iter(plt.cm.rainbow(np.linspace(0,1,n)))

for data in zip(value_cols, edge_names):
    c=next(color)
    # print(data)
    plt.plot(box_cols, data[0], marker='.', linestyle='dashed', label = data[1], c=c)


plt.title('Price-sensitive Occupancy of Drone Connections')
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path('plots/lineplot_PAXvsFARE_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_PAXvsFARE_', act_ver), bbox_inches="tight")
plt.clf()

#df_max = df.copy()



# print(list(rename_dict_V3.values()))

