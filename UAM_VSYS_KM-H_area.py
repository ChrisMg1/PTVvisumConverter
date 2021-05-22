import matplotlib.pyplot as plt

from main import attribut2dataframe, idx_aliases, cmap1
import pandas as pd
pd.options.mode.chained_assignment = None

# specify input file
vsys_file = 'C:/Users/chris/proj-lvm_files/VSYS_UAM_KM_H_v4.att'


# read VSYS attribute table
df2 = attribut2dataframe(vsys_file, [0])


# rename index for legend in plot
df2.rename(index=idx_aliases, inplace=True)


# prepare filters
# pers_km = ['PERSKM_AP__CM0', 'PERSKM_AP__CM50', 'PERSKM_AP__CM100', 'PERSKM_AP__CM250', 'PERSKM_AP__CM500', 'PERSKM_AP__CM10000']
# pers_h  = ['PERSSTD_AP__CM0', 'PERSSTD_AP__CM50', 'PERSSTD_AP__CM100', 'PERSSTD_AP__CM250', 'PERSSTD_AP__CM500', 'PERSSTD_AP__CM10000']

# V4:
pers_km = ['PERSKM_AP__CM0_V4', 'PERSKM_AP__CM50_V4', 'PERSKM_AP__CM100_V4', 'PERSKM_AP__CM250_V4', 'PERSKM_AP__CM500_V4', 'PERSKM_AP__CM1000_V4']
pers_h  = ['PERSSTD_AP__CM0_V4', 'PERSSTD_AP__CM50_V4', 'PERSSTD_AP__CM100_V4', 'PERSSTD_AP__CM250_V4', 'PERSSTD_AP__CM500_V4', 'PERSSTD_AP__CM1000_V4']

pers_cases  = ['LINBEF_AP__CM0_V4', 'LINBEF_AP__CM50_V4', 'LINBEF_AP__CM100_V4', 'LINBEF_AP__CM250_V4', 'LINBEF_AP__CM500_V4', 'LINBEF_AP__CM1000_V4']


# create sub-df's
df_km = df2[pers_km]
df_h  = df2[pers_h]

df_cases = df2[pers_cases]

# print(df_h)

df_km.rename(columns={'PERSKM_AP__CM0_V4': '0',
                   'PERSKM_AP__CM50_V4': '50',
                   'PERSKM_AP__CM100_V4': '100',
                   'PERSKM_AP__CM250_V4': '250',
                   'PERSKM_AP__CM500_V4': '500',
                   'PERSKM_AP__CM1000_V4': '1000'
                   }, inplace=True)

df_h.rename(columns={'PERSSTD_AP__CM0_V4': '0',
                    'PERSSTD_AP__CM50_V4': '50', 
                    'PERSSTD_AP__CM100_V4': '100', 
                    'PERSSTD_AP__CM250_V4': '250',
                    'PERSSTD_AP__CM500_V4': '500',
                    'PERSSTD_AP__CM1000_V4': '1000'
                    }, inplace=True)


df_cases.rename(columns={'LINBEF_AP__CM0_V4': '0',
                    'LINBEF_AP__CM50_V4': '50', 
                    'LINBEF_AP__CM100_V4': '100', 
                    'LINBEF_AP__CM250_V4': '250',
                    'LINBEF_AP__CM500_V4': '500',
                    'LINBEF_AP__CM1000_V4': '1000'
                    }, inplace=True)



df_transp_km = df_km.transpose()

# save areaplot for distance

df_transp_km.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=2)
plt.title('Travelled Distance with Public Transport')
plt.ylabel('Total Kilometres [km]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig('plots/areaplot_dist.svg', bbox_inches="tight")
plt.savefig('plots/areaplot_dist.pdf', bbox_inches="tight")
plt.clf()


df_transp_h = df_h.transpose()

# save areaplot for time

df_transp_h.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=2)
plt.title('Travelled Time with Public Transport')
plt.ylabel('Total Time [h]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig('plots/areaplot_time.svg', bbox_inches="tight")
plt.savefig('plots/areaplot_time.pdf', bbox_inches="tight")
plt.clf()


df_transp_cases = df_cases.transpose()

# save areaplot for cases

df_transp_cases.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=2)
plt.title('Transport Cases with Public Transport')
plt.ylabel('Total Cases [PAX]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig('plots/areaplot_cases.svg', bbox_inches="tight")
plt.savefig('plots/areaplot_cases.pdf', bbox_inches="tight")
plt.clf()

print(df_transp_cases.columns)

print(df_transp_cases[['UAM', 'Walk/Bike', 'ICE/IC']])

print(df_transp_h[['UAM', 'Walk/Bike', 'ICE/IC']])
