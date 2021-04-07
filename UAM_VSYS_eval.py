# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:35:17 2021

@author: chris
"""

import matplotlib.pyplot as plt
from main import attribut2dataframe
import numpy as np
import random

import matplotlib.colors as mcolors

number_of_colors = 11
colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = number_of_colors)

vsys_file = 'C:/Users/chris/proj-lvm_files/VSYS_UAM_KM_H.att'


df2 = attribut2dataframe(vsys_file)

# Dictionary to replace german terms
VSYS_aliases = {
  'Bus': 'Bus',
  'Fernbus': 'Long Distance Bus',
  'ÖVFuss': 'Foot',
  'ICE/IC': 'ICE/IC',
  'RB/RE': 'Regional Train',
  'S-Bahn': 'Commuter Train',
  'Seilbahn 30kmh': 'Cable Car',
  'Schiff': 'Boat',
  'Tram': 'Tram',
  'U-Bahn': 'Metro',
  'Urban Air Mobility 200kmh': 'UAM'
}

VSYS_explode = (0,0,0,0,0,0,0,0,0,0,0.25)

# print(df2)
# print(list(df2.columns))


# print(list(df2['NAME']))

test_pie50 = df2['PERSKM_AP__CM50']#.str[:-2].astype(np.double)
test_labels50 = df2['NAME']

print(test_labels50)
test_labels50 = test_labels50.replace(VSYS_aliases)
print(test_labels50)





fig1, ax1 = plt.subplots(1,3)
ax1[0].pie(test_pie50, explode = VSYS_explode, startangle=90)
ax1[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1[0].set_title('subplot 1')
ax1[0].legend(labels=['%s (%1.1f %%)' % (l, s) for l, s in zip(test_labels50, 100*test_pie50 / sum(test_pie50))], loc='best', bbox_to_anchor=(1, 0.4), fontsize=8)

ax1[1].pie(test_pie50, startangle=90)
ax1[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1[1].set_title('subplot 2')
ax1[1].legend(labels=['%s (%1.1f %%)' % (l, s) for l, s in zip(test_labels50, 100*test_pie50 / sum(test_pie50))], loc='best', bbox_to_anchor=(0.5, -0.1), fontsize=8)

ax1[2].pie(test_pie50, startangle=90)
ax1[2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1[2].set_title('subplot 3')
ax1[2].legend(labels=['%s (%1.1f %%)' % (l, s) for l, s in zip(test_labels50, 100*test_pie50 / sum(test_pie50))], loc='best', bbox_to_anchor=(0.5, -0.1), fontsize=8)

# plt.legend(labels=['%s (%1.1f %%)' % (l, s) for l, s in zip(test_labels50, 100*test_pie50 / sum(test_pie50))], loc='best', bbox_to_anchor=(-0.1, -0.1), fontsize=8)
plt.savefig('pie_KM.svg', bbox_inches="tight")
plt.savefig('pie_KM.pdf', bbox_inches="tight")
plt.clf()