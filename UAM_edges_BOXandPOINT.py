# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:38 2021

@author: chris
"""
import matplotlib.pyplot as plt
from main import attribut2dataframe, att_path, pdf_path, svg_path
import numpy as np

act_ver = 'v5p1'

att_file = att_path('C:/Users/chris/proj-lvm_files/Strecken_UAM_', act_ver)

UAMcap4 = 4 * 24 * 4
UAMcap7 = 4 * 24 * 7


df = attribut2dataframe(att_file, False)#[0, 1, 2])

df = df[df['TSYSSET']=='UAM200']

rename_dict = {'BELPERS-OEV_AP__CM11M000_' + act_ver.upper(): '0', 'BELPERS-OEV_AP__CM11M050_' + act_ver.upper(): '50', 
                    'BELPERS-OEV_AP__CM11M100_' + act_ver.upper(): '100', 'BELPERS-OEV_AP__CM11M150_' + act_ver.upper(): '150', 
                    'BELPERS-OEV_AP__CM11M250_' + act_ver.upper(): '250', 'BELPERS-OEV_AP__CM11M500_' + act_ver.upper(): '500', 
                    'LENGTH': 'LENGTH_km'}


df.rename(columns = rename_dict, inplace=True)

# if unit is also exported from Visum...:
if False:
    df['LENGTH_km'] = df['LENGTH_km'].str[:-2].astype(np.double)

df.sort_values(by='0', ascending=False, inplace=True, kind='quicksort', na_position='last')

box_cols = ['0', '50', '100', '150', '250', '500']


#print(df.columns)

df.boxplot(column = box_cols, whis=(0, 100))
plt.title('Price-sensitive Occupancy of Drone Connections')
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)

# Line repr. maximum capacity
plt.axhline(y = UAMcap4, color = 'r', linestyle = '-', label = '4-seater')
plt.axhline(y = UAMcap7, color = 'b', linestyle = '-', label = '7-seater')

plt.legend(loc='upper right', title='Maximum Capacity [PAX/day]')#, bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4)

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
    df[new_col_name] =  np.minimum(df[my_col], UAMcap7) 
    df[new_col_sum] = df[my_col].sum()

df.boxplot(column = new_box_cols, whis=(0, 100) )
# plt.title('Price-sensitive Occupancy of Drone Connections')
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.ylim(0, UAMcap7 * 1.3)

# don't plot solange nicht fertig

plt.savefig(svg_path('plots/boxplot_PAXvsFARE_MAX_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/boxplot_PAXvsFARE_MAX_', act_ver), bbox_inches="tight")

plt.clf()


# todo: transpose, not iter...

value_cols = []
edge_names = []

for index, row in df[box_cols].iterrows():
    
    type = 'max' # 'real' | 'max'
    
    ## use real traffic load (PAX per link) from model ##
    if type == 'real':
        value_cols.append(row.values.tolist())
        line_path = 'plots/lineplot_PAXvsFARE_'
    
    ## use maximum capacity PAX (~UAMcap7) instead of real value ##
    elif type == 'max':
        value_cols.append(np.minimum(row.values, UAMcap7))
        line_path = 'plots/lineplot_PAXvsFARE_MAX_'
    
    
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

if type == 'max':
    plt.ylim(0, UAMcap7 * 1.3)


# plt.title('Price-sensitive Occupancy of Drone Connections') # Title in Paper, not in plot
plt.ylabel('Passengers on UAM Links [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)

# Legend only on first plot (same colors with limited access)
if type == 'real':
    plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path(line_path, act_ver), bbox_inches="tight")
plt.savefig(pdf_path(line_path, act_ver), bbox_inches="tight")
plt.clf()




# Histogram : Distribution on UAM lengths

fig, ax0 = plt.subplots(nrows=1)
df['LENGTH_km'].hist(ax=ax0, label = 'UAM Links')
plt.axvline(x=300, color='r', linestyle='dashed', linewidth=2, label = 'Max. UAM Range')
plt.legend(loc='upper right')
plt.ylabel('UAM Links (Total = 150)')
plt.xlabel('Length [km]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)
plt.savefig(svg_path('plots/histogram_UAMlen_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/histogram_UAMlen_', act_ver), bbox_inches="tight")
plt.clf()






#df_max = df.copy()



# print(list(rename_dict_V3.values()))



