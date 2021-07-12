# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:27:48 2021

@author: chris
"""

import matplotlib.pyplot as plt
import pandas as pd
from main import pdf_path, svg_path

act_ver = 'v1'

fare_file = 'C:/Users/chris/proj-lvm_files/lvm_fare_v1.csv'

fare_plot = pd.read_csv(fare_file, sep = ';')

print(fare_plot['fare'])


charges = [(0, 'b'), (50, 'g'), (100, 'r'), (150, 'c'), (250, 'm'), (500, 'y')]
scen = 1

plt.figure()
# fare_plot.plot(marker='.', linestyle='dashed')

plt.plot(fare_plot['tariff points'], fare_plot['fare'], linestyle = '-', color = 'k', label = r'Distance-Depended Fare $F^{dd}$', linewidth=3)


for sur in reversed(charges): 
    plt.axhline(y = sur[0], linestyle = '-', color = sur[1], label = r'UAM Surcharge $F^{fs}$ Scenario ' + str(scen), linewidth=1)
    scen = scen + 1
plt.plot(fare_plot['tariff points'], fare_plot['fare'], linestyle = '-', color = 'k', linewidth=3)
    


# plt.title('Total Transfers')
plt.ylabel('Trip Cost [€]')
plt.xlabel('Tariff Points')
plt.xlim(0,300000)
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.6)
plt.legend(loc='upper left')#' center', bbox_to_anchor=[0.5, -0.15], fancybox=True, shadow=False, ncol=3)
plt.savefig(svg_path('plots/lineplot_FARE_', act_ver), bbox_inches="tight")
plt.savefig(pdf_path('plots/lineplot_FARE_', act_ver), bbox_inches="tight")
plt.clf()