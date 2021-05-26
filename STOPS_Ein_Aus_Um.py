# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:56:25 2021

@author: chris
"""

import matplotlib.pyplot as plt
from main import attribut2dataframe, att_path, pdf_path, svg_path, cmap1
import numpy as np

act_ver = 'v4p2'

att_file = att_path('C:/Users/chris/proj-lvm_files/STOPS_UAM_', act_ver)

# read STOPS. ACHTUNG!!! Auf Index-Column aufpassen, insb. auch beim Export
df3 = attribut2dataframe(att_file, [2])
df3 = df3[df3['CM_UAM'] == 1]


# remove some dirt...

hbf_aliases = {'Ingolstadt Hbf.': 'Ingolstadt Hbf', 'Augsburg, Hauptbahnhof': 'Augsburg Hbf'}
df3.rename(index=hbf_aliases, inplace=True)


# select columns for sub dataframes
col_transit_all   = ['UMSTEIGERGES_AP__CM11M0_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M50_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M100_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M250_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M500_' + act_ver.upper(), 'UMSTEIGERGES_AP__CM11M1000_' + act_ver.upper()]
col_board_uam = ['EINSTEIGER-VSYS_UAM200_AP__CM11M0_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M50_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M100_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M250_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M500_' + act_ver.upper(), 'EINSTEIGER-VSYS_UAM200_AP__CM11M1000_' + act_ver.upper()]
col_board_ice = ['EINSTEIGER-VSYS_ICE_AP__CM11M0_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M50_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M100_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M250_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M500_' + act_ver.upper(), 'EINSTEIGER-VSYS_ICE_AP__CM11M1000_' + act_ver.upper()]

# iterator
cost_values = ['0', '50', '100', '250', '500', '1000']


# create sub-df's for transit and boarding total UAM/ICE
df_transit_all = df3[col_transit_all]
df_board_ice  = df3[col_board_ice]
df_board_uam = df3[col_board_uam]

print(df_board_uam)

# rename the column-headers of the sub df's

for i in range(len(cost_values)):
    df_transit_all.rename(columns={col_transit_all[i]: cost_values[i]}, inplace=True)
    df_board_ice.rename(columns={col_board_ice[i]: cost_values[i]}, inplace=True)
    df_board_uam.rename(columns={col_board_uam[i]: cost_values[i]}, inplace=True)
    
# transpose the df's to get right format to plot
    
df_transit_all_transp = df_transit_all.transpose()

plt.figure()
df_transit_all_transp.plot(marker='.', linestyle='dashed')
plt.title('Transits')
plt.ylabel('Passengers [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path('plots/lineplot_TRANSIT_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_TRANSIT_', act_ver), bbox_inches="tight")
plt.clf()


df_board_ice_transp = df_board_ice.transpose()

plt.figure()
df_board_ice_transp.plot(marker='.', linestyle='dashed')
plt.title('ICE Boardings')
plt.ylabel('Passengers [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path('plots/lineplot_ICEboard_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_ICEboard_', act_ver), bbox_inches="tight")
plt.clf()


df_board_uam_transp = df_board_uam.transpose()

plt.figure()
df_board_uam_transp.plot(marker='.', linestyle='dashed')
plt.title('UAM Boardings')
plt.ylabel('Passengers [PAX/day]')
plt.xlabel('Added Fixed Costs to UAM Fare [€]')
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path('plots/lineplot_UAMboard_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_UAMboard_', act_ver), bbox_inches="tight")
plt.clf()
