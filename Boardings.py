# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:11:07 2021

@author: chris
"""

from main import attribut2dataframe, GEH # , cmap1
import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/chris/proj-lvm_files/EinsteigerVSySDiff2.att'

df = attribut2dataframe(path, False)# [0, 1, 2])

df = df[df['B_BAYERN']==1]

# todo:, Evtl. Filtern auf Zählwert > ''
# Anscheinend genügt es, wenn B_BAYERN==1, weil für alle STOPS in Bayern Werte vorliegen

print(df)
print(df.columns)

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
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.5), ncol=3)
    
    ax2.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)
    
    fig = ax2.get_figure()
    fig.set_size_inches(8, 5, forward=True)
    fig.autofmt_xdate()
    fig.savefig('plots/' + out_f + '.pdf', bbox_inches='tight')
    fig.savefig('plots/' + out_f + '.svg', bbox_inches='tight')
    plt.clf()
    fig.clf()


boardings_plot('Barplot_Boardings_white', 'white')
boardings_plot('Barplot_Boardings_grey', 'grey')


fig2, ax3 = plt.subplots()
df['GEH'].hist(bins=50, ax=ax3, label=r'$\sqrt{\frac{2(model-count)^2}{model+count}}$')
#plt.title('Deviation of Counted and Modelled Boardings')
plt.ylabel('Frequency')
plt.xlabel('GEH-weighted Deviation')

#ax3.legend(loc='upper right')
ax3.legend(loc='center', bbox_to_anchor=(0.5, -0.25))
ax3.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)

fig2 = ax3.get_figure()
fig2.set_size_inches(8, 5, forward=True)
fig2.savefig('plots/histogram_GEH.pdf', bbox_inches='tight')
fig2.savefig('plots/histogram_GEH.svg', bbox_inches='tight')
plt.clf()
fig2.clf()


abs_limit = max(df["Deviation"].max(), abs(df["Deviation"].min()))
fig3, ax4 = plt.subplots()
fig3.set_size_inches(8, 5, forward=True)
df['Deviation'].hist(bins=50, ax=ax4, range=(-abs_limit,abs_limit), label='model - count')

#ax4.legend(loc='upper right')
ax4.legend(loc='center', bbox_to_anchor=(0.5, -0.25))

#plt.title('Deviation of Counted and Modelled Boardings')
plt.ylabel('Frequency')
plt.xlabel('Absolute Deviation [PAX]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)

fig3 = ax4.get_figure()

fig3.savefig('plots/histogram_abs_deviation.pdf', bbox_inches='tight')
fig3.savefig('plots/histogram_abs_deviation.svg', bbox_inches='tight')
plt.clf()
fig3.clf()


### control stuff

fig2, ax3 = plt.subplots()
df['Calibration Count'].hist(bins=50, ax=ax3)
fig2 = ax3.get_figure()
#plt.title('Empirical Data')
plt.ylabel('Frequency')
plt.xlabel('SPNV Counts')
fig2.savefig('plots/histogram_SPNV_counts.pdf', bbox_inches='tight')
fig2.savefig('plots/histogram_SPNV_counts.svg', bbox_inches='tight')
plt.clf()
fig2.clf()

#print(df.nlargest(10,'GEH')[['NAME', 'GEH']])
print(df.nlargest(10,'Calibration Count')[['NAME', 'Calibration Count']])
print(df.nsmallest(10,'Calibration Count')[['NAME', 'Calibration Count']])


print(df[df['Calibration Count'] == ''].index)

# newer 2p2