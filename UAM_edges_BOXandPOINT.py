# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:38 2021

@author: chris
"""
import matplotlib.pyplot as plt
from main import attribut2dataframe
import numpy as np

att_file = 'C:/Users/chris/proj-lvm_files/Strecken_UAM.att'
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

print(df[['LENGTH_km', '0', '0_w', '100', '100_w']])

# print(new_box_cols)
# print(list(df.columns))


df.boxplot(column = new_box_cols)
plt.title('Urban Air Mobility Passengers Weighted with Distance')
plt.ylabel('Count: Network Passengers [Pax/day]')
plt.xlabel('Fare: Added Fixed Costs [€]')
plt.savefig('boxplot_weighted_distance_TEMP.png')
plt.clf()

first_row = df['0_w'][:1]

print(first_row, type(first_row))

# plt.plot(x='HELLO', y=first_row)

# print(df[['LENGTH_km', '0', '0_w', '100', '100_w']])

