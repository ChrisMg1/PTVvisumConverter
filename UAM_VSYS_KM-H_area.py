import matplotlib.pyplot as plt

from main import attribut2dataframe, idx_aliases, cmap1, att_path, pdf_path, svg_path
import pandas as pd
pd.options.mode.chained_assignment = None

# run version of Visum
act_ver = 'v5p1'

# specify input file
vsys_file = att_path('C:/Users/chris/proj-lvm_files/VSYS_UAM_KM_H_C_', act_ver)




# read VSYS attribute table
df2 = attribut2dataframe(vsys_file, [0])


# rename index for legend in plot
df2.rename(index=idx_aliases, inplace=True)


# prepare filters
# pers_km = ['PERSKM_AP__CM0', 'PERSKM_AP__CM50', 'PERSKM_AP__CM100', 'PERSKM_AP__CM250', 'PERSKM_AP__CM500', 'PERSKM_AP__CM10000']
# pers_h  = ['PERSSTD_AP__CM0', 'PERSSTD_AP__CM50', 'PERSSTD_AP__CM100', 'PERSSTD_AP__CM250', 'PERSSTD_AP__CM500', 'PERSSTD_AP__CM10000']

# V4:
#pers_km = ['PERSKM_AP__CM0_V4', 'PERSKM_AP__CM50_V4', 'PERSKM_AP__CM100_V4', 'PERSKM_AP__CM250_V4', 'PERSKM_AP__CM500_V4', 'PERSKM_AP__CM1000_V4']
#pers_h  = ['PERSSTD_AP__CM0_V4', 'PERSSTD_AP__CM50_V4', 'PERSSTD_AP__CM100_V4', 'PERSSTD_AP__CM250_V4', 'PERSSTD_AP__CM500_V4', 'PERSSTD_AP__CM1000_V4']

#pers_cases  = ['LINBEF_AP__CM0_V4', 'LINBEF_AP__CM50_V4', 'LINBEF_AP__CM100_V4', 'LINBEF_AP__CM250_V4', 'LINBEF_AP__CM500_V4', 'LINBEF_AP__CM1000_V4']



pers_cases = ['LINBEF_AP__CM11M000_' + act_ver.upper(), 'LINBEF_AP__CM11M050_' + act_ver.upper(), 'LINBEF_AP__CM11M100_' + act_ver.upper(), 'LINBEF_AP__CM11M150_' + act_ver.upper(), 'LINBEF_AP__CM11M250_' + act_ver.upper(), 'LINBEF_AP__CM11M500_' + act_ver.upper()]
pers_km = ['PERSKM_AP__CM11M000_' + act_ver.upper(), 'PERSKM_AP__CM11M050_' + act_ver.upper(), 'PERSKM_AP__CM11M100_' + act_ver.upper(), 'PERSKM_AP__CM11M150_' + act_ver.upper(), 'PERSKM_AP__CM11M250_' + act_ver.upper(), 'PERSKM_AP__CM11M500_' + act_ver.upper()]
pers_h  = ['PERSSTD_AP__CM11M000_' + act_ver.upper(), 'PERSSTD_AP__CM11M050_' + act_ver.upper(), 'PERSSTD_AP__CM11M100_' + act_ver.upper(), 'PERSSTD_AP__CM11M150_' + act_ver.upper(), 'PERSSTD_AP__CM11M250_' + act_ver.upper(), 'PERSSTD_AP__CM11M500_' + act_ver.upper()]




# create sub-df's
df_km = df2[pers_km]
df_h  = df2[pers_h]
df_cases = df2[pers_cases]

# print(df_h)

df_km.rename(columns={'PERSKM_AP__CM11M000_' + act_ver.upper(): '0',
                   'PERSKM_AP__CM11M050_' + act_ver.upper(): '50',
                   'PERSKM_AP__CM11M100_' + act_ver.upper(): '100',
                   'PERSKM_AP__CM11M150_' + act_ver.upper(): '150',
                   'PERSKM_AP__CM11M250_' + act_ver.upper(): '250',
                   'PERSKM_AP__CM11M500_' + act_ver.upper(): '500'
                   }, inplace=True)

df_h.rename(columns={'PERSSTD_AP__CM11M000_' + act_ver.upper(): '0',
                    'PERSSTD_AP__CM11M050_' + act_ver.upper(): '50', 
                    'PERSSTD_AP__CM11M100_' + act_ver.upper(): '100',
                    'PERSSTD_AP__CM11M150_' + act_ver.upper(): '150', 
                    'PERSSTD_AP__CM11M250_' + act_ver.upper(): '250',
                    'PERSSTD_AP__CM11M500_' + act_ver.upper(): '500'
                    }, inplace=True)


df_cases.rename(columns={'LINBEF_AP__CM11M000_' + act_ver.upper(): '0',
                    'LINBEF_AP__CM11M050_' + act_ver.upper(): '50', 
                    'LINBEF_AP__CM11M100_' + act_ver.upper(): '100',
                    'LINBEF_AP__CM11M150_' + act_ver.upper(): '150', 
                    'LINBEF_AP__CM11M250_' + act_ver.upper(): '250',
                    'LINBEF_AP__CM11M500_' + act_ver.upper(): '500'
                    }, inplace=True)



# Calculations for percentages (in plot)

if True:
    print('TRAVEL TIME')
    df_h_temp = df_h.copy()
    #print(df_h_temp)
    df_h_temp = df_h_temp.drop(['Walk/Bike', 'Aerial Tram'])
    #print(df_h_temp)
    df_h_temp_perc = df_h_temp / df_h_temp.sum() * 100
    print(df_h_temp_perc.round(2))
    print(df_h_temp_perc.round(2).append(df_h_temp_perc.sum(numeric_only=True), ignore_index=True))
    print(df_h_temp.append(df_h_temp.sum(numeric_only=True), ignore_index=True))
    
    print('TRAVEL DISTANCE')
    df_km_temp = df_km.copy()
    #print(df_km_temp)
    df_km_temp = df_km_temp.drop(['Walk/Bike', 'Aerial Tram'])
    #print(df_km_temp)
    df_km_temp_perc = df_km_temp / df_km_temp.sum() * 100
    print(df_km_temp_perc.round(2))
    print(df_km_temp_perc.round(2).append(df_km_temp_perc.sum(numeric_only=True), ignore_index=True))
    print(df_km_temp.append(df_km_temp.sum(numeric_only=True), ignore_index=True))
    
    print('TRAVEL CASES')
    df_cases_temp = df_cases.copy()
    #print(df_cases_temp)
    df_cases_temp = df_cases_temp.drop(['Walk/Bike', 'Aerial Tram'])
    #print(df_cases_temp)
    df_cases_temp_perc = df_cases_temp / df_cases_temp.sum() * 100
    print(df_cases_temp_perc.round(2))
    print(df_cases_temp_perc.round(2).append(df_cases_temp_perc.sum(numeric_only=True), ignore_index=True))
    print(df_cases_temp.append(df_cases_temp.sum(numeric_only=True), ignore_index=True))


df_transp_km = df_km.drop(['Walk/Bike', 'Aerial Tram']).transpose()

# save areaplot for distance

df_transp_km.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=3, title="Mode of Transport")
# plt.title('Travelled Distance with Public Transport')
plt.ylabel('Traveled Distance [PAX km/d]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig(svg_path('C:/Users/chris/plots/areaplot_dist_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('C:/Users/chris/plots/areaplot_dist_', act_ver), bbox_inches="tight")
plt.clf()


df_transp_h = df_h.drop(['Walk/Bike', 'Aerial Tram']).transpose()

# save areaplot for time

df_transp_h.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=3, title="Mode of Transport")
# plt.title('Travelled Time with Public Transport')
plt.ylabel('Traveled Time [PAX h/d]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig(svg_path('C:/Users/chris/plots/areaplot_time_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('C:/Users/chris/plots/areaplot_time_', act_ver), bbox_inches="tight")
plt.clf()



df_transp_cases = df_cases.drop(['Walk/Bike', 'Aerial Tram']).transpose()

# save areaplot for cases

df_transp_cases.plot.area(cmap=cmap1)
plt.legend(loc='center', bbox_to_anchor=(0.5, -0.35), ncol=3, title="Mode of Transport")
#  plt.title('Transport Cases with Public Transport')
plt.ylabel('Transport Cases [PAX/d]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.savefig(svg_path('C:/Users/chris/plots/areaplot_cases_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('C:/Users/chris/plots/areaplot_cases_', act_ver), bbox_inches="tight")
plt.clf()