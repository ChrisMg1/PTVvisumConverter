# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:26:31 2021

@author: chris
"""

from main import attribut2dataframe

path = 'C:/Users/chris/Documents/LVM_geoprocessing/Nachfrage_aus_Visum/cm_LVM_OD_time_demand_filtered_geq1.att'


df = attribut2dataframe(path, False).rename(columns={"$ODPAIR:FROMZONENO": "FROMZONENO"})

df["beeline_speed"] = ( 60 * df["DIRECTDIST"] / df["MATVALUE(309)"])



print(df.head())

print(df.columns)

ax1 = df.plot.scatter(x='DIRECTDIST', y='beeline_speed', c='DarkBlue')
