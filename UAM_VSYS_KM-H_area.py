import matplotlib.pyplot as plt

from main import attribut2dataframe, idx_aliases, cmap1
import pandas as pd
pd.options.mode.chained_assignment = None

# specify input file
vsys_file = 'C:/Users/chris/proj-lvm_files/VSYS_UAM_KM_H.att'


# read VSYS attribute table
df2 = attribut2dataframe(vsys_file, [0])


# rename index for legend in plot
df2.rename(index=idx_aliases, inplace=True)


# prepare filters
pers_km = ['PERSKM_AP__CM0', 'PERSKM_AP__CM50', 'PERSKM_AP__CM100', 'PERSKM_AP__CM250', 'PERSKM_AP__CM500', 'PERSKM_AP__CM10000']
pers_h  = ['PERSSTD_AP__CM0', 'PERSSTD_AP__CM50', 'PERSSTD_AP__CM100', 'PERSSTD_AP__CM250', 'PERSSTD_AP__CM500', 'PERSSTD_AP__CM10000']


# create sub-df's
df_km = df2[pers_km]
df_h  = df2[pers_h]

df_km.rename(columns={'PERSKM_AP__CM0': '0',
                   'PERSKM_AP__CM50': '50',
                   'PERSKM_AP__CM100': '100',
                   'PERSKM_AP__CM250': '250',
                   'PERSKM_AP__CM500': '500',
                   'PERSKM_AP__CM10000': '10000'
                   }, inplace=True)

df_h.rename(columns={'PERSSTD_AP__CM0': '0',
                    'PERSSTD_AP__CM50': '50', 
                    'PERSSTD_AP__CM100': '100', 
                    'PERSSTD_AP__CM250': '250',
                    'PERSSTD_AP__CM500': '500',
                    'PERSSTD_AP__CM10000': '10000'
                    }, inplace=True)

# print(df_km.columns, df_h.columns)

df_transp_km = df_km.transpose()

# save areaplot for distance

df_transp_km.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=3)
plt.title('Travelled Distance with Public Transport')
plt.ylabel('Total Kilometres [km]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig('plots/areaplot_dist.svg', bbox_inches="tight")
plt.savefig('plots/areaplot_dist.pdf', bbox_inches="tight")
plt.clf()


df_transp_h = df_h.transpose()

# save areaplot for time

df_transp_h.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=3)
plt.title('Travelled Time with Public Transport')
plt.ylabel('Total Time [h]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig('plots/areaplot_time.svg', bbox_inches="tight")
plt.savefig('plots/areaplot_time.pdf', bbox_inches="tight")
plt.clf()

