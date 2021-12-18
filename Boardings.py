# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:11:07 2021

@author: chris
"""

from main import attribut2dataframe, GEH, roundup # , cmap1
import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

path = 'C:/Users/chris/proj-lvm_files/EinsteigerVSySDiff2.att'

df = attribut2dataframe(path, False)# [0, 1, 2])

df_temp_count = df[['NAME', 'NEU_EINST_N14']]

df = df[df['B_BAYERN']==1]

print(len(df_temp_count))

print(df_temp_count['NEU_EINST_N14'].isna().sum())

print('================')

# print(df_temp_count)

# print(np.where(pd.isnull(df)))

# todo:, Evtl. Filtern auf Zählwert > ''
# Anscheinend genügt es, wenn B_BAYERN==1, weil für alle STOPS in Bayern Werte vorliegen


df.rename(columns={'NEU_EINST_N14': 'Calibration Count',
                   'PASSBOARD_TSYS(B,AP)': 'Bus',
                   'PASSBOARD_TSYS(F,AP)': 'Long Distance Bus',
                   'PASSBOARD_TSYS(ICE,AP)': 'ICE/IC',
                   'PASSBOARD_TSYS(RB,AP)': 'Regional Train',
                   'PASSBOARD_TSYS(S,AP)': 'Commuter Train',
                   'PASSBOARD_TSYS(SCHIFF,AP)': 'Boat',
                   'PASSBOARD_TSYS(T,AP)': 'Tram',
                   'PASSBOARD_TSYS(U,AP)': 'Underground'
                   }, inplace=True)
df['SPNV'] = df['Regional Train'] + df['Commuter Train']

# todo: GEH value
df['Deviation'] = df['SPNV'] - df['Calibration Count']
df['rel_Deviation'] = ( ( df['SPNV'] - df['Calibration Count'] ) / df['Calibration Count'] ) * 100
df['GEH'] = GEH(df['SPNV'], df['Calibration Count'])



# select specific row and relevant columns for bar plot

top_stations = np.array(df['PASSBOARD(AP)'].nlargest(10).index).tolist()

to_bar_group1 = df.loc[top_stations]



def boardings_plot(out_f, color_f):
    fig, ax2 = plt.subplots()
    
    # see: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
    colormap = plt.cm.get_cmap('Paired', 8)
    
    to_bar_group1.plot.bar(x='NAME', y=['Commuter Train', 'Regional Train', 'ICE/IC', 'Tram', 'Underground', 'Bus', 'Long Distance Bus', 'Boat'],
                           ax=ax2, width=0.45, position=0, color=colormap.colors, stacked=True)
    
    to_bar_group1.plot.bar(x='NAME', y='Calibration Count', ax=ax2, width=0.45, position=1, color=color_f)
    
    # activate for frame SPNV
    # to_bar_group1.plot.bar(x='NAME', y='SPNV', ax=ax2, width=0.1, position=0, edgecolor = "black", linewidth=2.5, fc="none")
    
    
    
    #plt.title('Boardings at Most Frequented Stations')
    
    
    
    plt.ylabel('Passengers [PAX]')
    plt.xlabel('Station Name')
    plt.xticks(fontsize=10)
    # plt.legend(loc='center', bbox_to_anchor=(0.5, -0.5), ncol=3)
    plt.legend(loc='upper right', ncol=3)
    
    ax2.grid(visible=True, which='major', color='#666666', linestyle=':', alpha=0.6)
    
    fig = ax2.get_figure()
    fig.set_size_inches(8, 5, forward=True)
    fig.autofmt_xdate()
    fig.savefig('plots/' + out_f + '.pdf', bbox_inches='tight')
    fig.savefig('plots/' + out_f + '.svg', bbox_inches='tight')
    plt.clf()
    fig.clf()


boardings_plot('barplot_boardings_white', 'white')
boardings_plot('barplot_boardings_grey', 'grey')


## Plot GEH-WEIGHTED deviation between counts and model

fig2, ax3 = plt.subplots()

binwidth = 5
df['GEH'].hist(bins=range(0, roundup(max(df['GEH']), binwidth) + binwidth, binwidth), ax=ax3, label=r'$\sqrt{\frac{2(model-count)^2}{model+count}}$')
#plt.title('Deviation of Counted and Modelled Boardings')
plt.ylabel('Frequency (Total = 1082)')
plt.xlabel('GEH-weighted Deviation')

ax3.legend(loc='upper right')
# ax3.legend(loc='center', bbox_to_anchor=(0.5, -0.25))
ax3.grid(visible=True, which='major', color='#666666', linestyle=':', alpha=0.6)

fig2 = ax3.get_figure()
# fig2.set_size_inches(8, 5, forward=True)
fig2.savefig('plots/histogram_GEH.pdf', bbox_inches='tight')
fig2.savefig('plots/histogram_GEH.svg', bbox_inches='tight')
plt.clf()
fig2.clf()



## Plot ABSOLUTE deviation between counts and model

# set range for symmetrc plot
abs_limit = max(df["Deviation"].max(), abs(df["Deviation"].min()))
fig3, ax4 = plt.subplots()
#fig3.set_size_inches(8, 5, forward=True)
df['Deviation'].hist(bins=100, ax=ax4, label=r'$model - count$')#, range=(-abs_limit/4,abs_limit/4))

ax4.legend(loc='upper right')
#ax4.legend(loc='center', bbox_to_anchor=(0.5, -0.25))

#plt.title('Deviation of Counted and Modelled Boardings')
plt.ylabel('Frequency (Total = 1082)')
plt.xlabel('Absolute Deviation [PAX]')
plt.grid(visible=True, which='major', color='#666666', linestyle=':', alpha=0.6)


fig3 = ax4.get_figure()

fig3.savefig('plots/histogram_abs_deviation.pdf', bbox_inches='tight')
fig3.savefig('plots/histogram_abs_deviation.svg', bbox_inches='tight')
plt.clf()
fig3.clf()



## Plot RELATIVE deviation between counts and model

# set range for symmetrc plot

fig4, ax5 = plt.subplots()
#fig4.set_size_inches(8, 5, forward=True)
df['rel_Deviation'].hist(bins=100, ax=ax5, label=r'$\frac{model-count}{count}$')

ax5.legend(loc='upper right')
#ax4.legend(loc='center', bbox_to_anchor=(0.5, -0.25))

#plt.title('Relative Deviation of Counted and Modelled Boardings')
plt.ylabel('Frequency (Total = 1082)')
plt.xlabel('Relative Deviation [%]')
plt.grid(visible=True, which='major', color='#666666', linestyle=':', alpha=0.6)


fig4 = ax5.get_figure()

fig4.savefig('plots/histogram_rel_deviation.pdf', bbox_inches='tight')
fig4.savefig('plots/histogram_rel_deviation.svg', bbox_inches='tight')
plt.clf()
fig4.clf()


### control stuff

fig2, ax3 = plt.subplots()
df['Calibration Count'].hist(bins=50, ax=ax3)
fig2 = ax3.get_figure()
#plt.title('Empirical Data')
plt.ylabel('Frequency (Total = 1082)')
plt.xlabel('SPNV Counts')
plt.grid(visible=True, which='major', color='#666666', linestyle=':', alpha=0.6)
fig2.savefig('plots/histogram_SPNV_counts.pdf', bbox_inches='tight')
fig2.savefig('plots/histogram_SPNV_counts.svg', bbox_inches='tight')
plt.clf()
fig2.clf()


print(df.nlargest(20,'GEH')[['NAME', 'GEH', 'Calibration Count', 'SPNV']])
print(df.nsmallest(200,'GEH')[['NAME', 'GEH', 'Calibration Count', 'SPNV']])

#print(df.nlargest(20,'rel_Deviation')[['NAME', 'rel_Deviation', 'Calibration Count', 'SPNV']])
#print(df.nsmallest(20,'rel_Deviation')[['NAME', 'rel_Deviation', 'Calibration Count', 'SPNV']])

print(df)
