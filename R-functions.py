# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:01:10 2021

@author: chris
"""

import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(-5,10,0.01)   # start,stop,step
R = np.arange(0,10,0.1) 

beta1 = 0.5
beta2 = 1.0
beta3 = 4.0

x_min = 0
x_max = 10
y_min = 0
y_max = 10



# Kirchoff
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
Kirchhoff_U_b1 = R**(-beta1)
Kirchhoff_U_b2 = R**(-beta2)
Kirchhoff_U_b3 = R**(-beta3)
plt.plot(R, Kirchhoff_U_b1, R, Kirchhoff_U_b2, R, Kirchhoff_U_b3)
plt.xlabel('Resistance')  # string must be enclosed with quotes '  '
plt.ylabel('Utility')
plt.title('Aufteilungsmodell: KIRCHHOFF')
plt.legend(['beta 1', 'beta 2', 'beta 3'])      # legend entries as seperate strings in a list
# plt.show()
plt.savefig('Utility-func-plots/Kirchhoff.png')
plt.clf()


# Logit
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
Logit_U_b1 = np.exp(-beta1 * R)
Logit_U_b2 = np.exp(-beta2 * R)
Logit_U_b3 = np.exp(-beta3 * R)
plt.plot(R, Logit_U_b1, R, Logit_U_b2, R, Logit_U_b3)
plt.xlabel('Resistance')  # string must be enclosed with quotes '  '
plt.ylabel('Utility')
plt.title('Aufteilungsmodell: LOGIT')
plt.legend(['beta 1', 'beta 2', 'beta 3'])      # legend entries as seperate strings in a list
# plt.show()
plt.savefig('Utility-func-plots/Logit.png')
plt.clf()


# BoxCox

tau = 0.5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
BoxCox_U_b1_T = np.exp(-beta1 * (((R**tau)-1) / tau) ) 
BoxCox_U_b2_T = np.exp(-beta2 * (((R**tau)-1) / tau) )
BoxCox_U_b3_T = np.exp(-beta3 * (((R**tau)-1) / tau) )
plt.plot(R, BoxCox_U_b1_T, R, BoxCox_U_b2_T, R, BoxCox_U_b3_T)
plt.xlabel('Resistance')  # string must be enclosed with quotes '  '
plt.ylabel('Utility')
plt.title('Aufteilungsmodell: BOXCOX')
plt.legend(['beta 1', 'beta 2', 'beta 3'])      # legend entries as seperate strings in a list
# plt.show()
plt.savefig('Utility-func-plots/BoxCox.png')
plt.clf()


