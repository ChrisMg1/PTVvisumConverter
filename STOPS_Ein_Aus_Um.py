# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:56:25 2021

@author: chris
"""

import matplotlib.pyplot as plt
from main import attribut2dataframe, att_path, pdf_path, svg_path, cmap1
# import numpy as np

act_ver = 'v5p1'

att_file = att_path('C:/Users/chris/proj-lvm_files/STOPS_UAM_', act_ver)

# read STOPS. ACHTUNG!!! Auf Index-Column aufpassen, insb. auch beim Export
df3 = attribut2dataframe(att_file, [2])
df3 = df3[df3['CM_UAM'] == 1]


# remove some dirt...

hbf_aliases = {'Ingolstadt Hbf.': 'Ingolstadt Hbf', 'Augsburg, Hauptbahnhof': 'Augsburg Hbf'}
df3.rename(index=hbf_aliases, inplace=True)


# select columns for sub dataframes
col_transfer_all   = ['UMSTEIGERGES_AP__CM11M000_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M050_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M100_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M150_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M250_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M500_' + act_ver.upper()]
col_board_uam = ['EINSTEIGER-VSYS_UAM200_AP__CM11M000_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M050_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M100_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M150_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M250_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M500_' + act_ver.upper()]
col_board_ice = ['EINSTEIGER-VSYS_ICE_AP__CM11M000_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M050_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M100_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M150_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M250_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M500_' + act_ver.upper()]
col_board_rb = ['EINSTEIGER-VSYS_RB_AP__CM11M000_' + act_ver.upper(), 'EINSTEIGER-VSYS_RB_AP__CM11M050_' + act_ver.upper(), 'EINSTEIGER-VSYS_RB_AP__CM11M100_' + act_ver.upper(), 'EINSTEIGER-VSYS_RB_AP__CM11M150_' + act_ver.upper(), 'EINSTEIGER-VSYS_RB_AP__CM11M250_' + act_ver.upper(), 'EINSTEIGER-VSYS_RB_AP__CM11M500_' + act_ver.upper()]

# iterator
cost_values = ['0', '50', '100', '150', '250', '500']


# create sub-df's for transfers and boarding total UAM/ICE/RB
df_transfer_all = df3[col_transfer_all]
df_board_ice  = df3[col_board_ice]
df_board_uam = df3[col_board_uam]
df_board_rb = df3[col_board_rb]



# rename the column-headers of the sub df's

for i in range(len(cost_values)):
    df_transfer_all.rename(columns={col_transfer_all[i]: cost_values[i]}, inplace=True)
    df_board_ice.rename(columns={col_board_ice[i]: cost_values[i]}, inplace=True)
    df_board_uam.rename(columns={col_board_uam[i]: cost_values[i]}, inplace=True)
    df_board_rb.rename(columns={col_board_rb[i]: cost_values[i]}, inplace=True)
    
df_transfer_all = df_transfer_all.sort_values(by='0', ascending=False)
df_board_ice = df_board_ice.sort_values(by='0', ascending=False)
df_board_uam = df_board_uam.sort_values(by='0', ascending=False)
df_board_rb = df_board_rb.sort_values(by='0', ascending=False)



# transpose the df's to get right format to plot

df_transfer_all_transp = df_transfer_all.transpose()

plt.figure()
df_transfer_all_transp.plot(marker='.', linestyle='dashed')
# plt.title('Total Transfers')
plt.ylabel('Total Transfers [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4, title="Stations with UAM connection")
plt.savefig(svg_path('plots/lineplot_TRANSFER_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_TRANSFER_', act_ver), bbox_inches="tight")
plt.clf()


df_board_uam_transp = df_board_uam.transpose()

plt.figure()
df_board_uam_transp.plot(marker='.', linestyle='dashed')
# plt.title('UAM Boardings')
plt.ylabel('UAM Boarding [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4, title="Stations with UAM connection")
plt.savefig(svg_path('plots/lineplot_UAMboard_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_UAMboard_', act_ver), bbox_inches="tight")
plt.clf()


df_board_ice_transp = df_board_ice.transpose()

plt.figure()
df_board_ice_transp.plot(marker='.', linestyle='dashed')
# plt.title('ICE/IC Boardings')
plt.ylabel('ICE/IC Boarding [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4, title="Stations with UAM connection")
plt.savefig(svg_path('plots/lineplot_ICEboard_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_ICEboard_', act_ver), bbox_inches="tight")
plt.clf()


df_board_rb_transp = df_board_rb.transpose()

plt.figure()
df_board_rb_transp.plot(marker='.', linestyle='dashed')
# plt.title('RE/RB Boardings')
plt.ylabel('RE/RB Boarding [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=4, title="Stations with UAM connection")
plt.savefig(svg_path('plots/lineplot_RBboard_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_RBboard_', act_ver), bbox_inches="tight")
plt.clf()

print(df_board_ice_transp)
print(df_board_ice)
print(df_board_ice.columns)
print(df_board_ice['0'])

