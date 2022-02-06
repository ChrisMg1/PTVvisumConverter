# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:11:00 2022

@author: chris
"""

from main import attribut2dataframe


demand_hist_path = 'C:/Users/chris/Documents/LVM_geoprocessing/Nachfrage_aus_Visum/cm_LVM2015_OD_totalDEMANDforHISTOGRAM.att'

demand_hist_df = attribut2dataframe(demand_hist_path, False)

print(demand_hist_df.min())
demand_hist_df2 = demand_hist_df[demand_hist_df['$ODPAIR:MATVALUE(10000)'] > 1.0]
#demand_hist_df2 = demand_hist_df2[demand_hist_df2['$ODPAIR:MATVALUE(10000)'] < 5.0]

print(demand_hist_df2.min())

demand_hist_df2['$ODPAIR:MATVALUE(10000)'].hist(bins=100)