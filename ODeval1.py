# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:26:31 2021

@author: chris
"""

from main import attribut2dataframe
import csv

def create_qgis_line(df_in, path):
    df_2write = df_in
    df_2write['wkt_geom'] = \
        'linestring(' + \
        df_2write['FROMZONE\XCOORD'].astype(str) + ' ' + \
        df_2write['FROMZONE\YCOORD'].astype(str) + ',' + \
        df_2write['TOZONE\XCOORD'].astype(str) + ' ' + \
        df_2write['TOZONE\YCOORD'].astype(str) + \
        ')'
    # print(df_2write.head())
    df_2write.to_csv(path  + 'test3.csv', sep ='\t', index=False, quoting=csv.QUOTE_NONE)
    return None

cmPLOT = False
in_path = 'C:/Users/chris/Documents/LVM_geoprocessing/Nachfrage_aus_Visum/cm_LVM_OD_time_demand_filtered_geq1.att'
out_path = 'C:/Users/chris/Documents/LVM_geoprocessing/Nachfrage_aus_Visum/'

df = attribut2dataframe(in_path, False).rename(columns={'$ODPAIR:FROMZONENO': 'FROMZONENO'})

# add cloumn for beeline speed
df['beeline_speed'] = ( 60 * df['DIRECTDIST'] / df['MATVALUE(309)'])

# add cloumn for ratio PrT-speed and PuT-speed
df['speed_ratio'] = ( df['MATVALUE(309)'] / df['MATVALUE(116)'] )

# filter df
#df = df[ (df['MATVALUE(10000)'] >= 1) ]
        
#df = df[ (df['speed_ratio'] >= 1.5) ]

#df = df[ (df['DIRECTDIST'] >= 250) ]


if (cmPLOT):
    ax1 = df.plot.scatter(x='DIRECTDIST', y='beeline_speed', c='DarkBlue')


print(df)

create_qgis_line(df, out_path)



# linestring(1285265.5213820108 6122740.40263463,1278514.250982746 6122695.812399528)