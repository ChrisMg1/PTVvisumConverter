# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:34:51 2021

@author: chris
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:01:10 2021

@author: chris
"""

import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(-5,10,0.01)   # start,stop,step
R = np.arange(0,150,0.1) 


beta = 0.2

x_min = 0
x_max = 150
y_min = 0
y_max = 1

def Nutzen(nutzen_alt):
    return nutzen_alt + 0


def P_Kichhoff(Aufwand_Liste):    
    Nenner = 0
    for el in Aufwand_Liste:
        Nenner = Nenner + el ** (-beta)
    return ( Aufwand_Liste[0] ** (-beta) ) / Nenner

def P_Logit(Aufwand_Liste):
    Nenner = 0
    for el in Aufwand_Liste:
        Nenner = Nenner + np.exp(el * (-beta))
    return ( np.exp(Aufwand_Liste[0] * (-beta) )) / Nenner


Test_1 = [5, 10]
Test_2 = [50, 100]
Test_3 = [95, 100]

print('Kirchhoff')
print(Test_1, P_Kichhoff(Test_1))
print(Test_2, P_Kichhoff(Test_2))
print(Test_3, P_Kichhoff(Test_3))


print('Logit')
print(Test_1, P_Logit(Test_1))
print(Test_2, P_Logit(Test_2))
print(Test_3, P_Logit(Test_3))


# Kirchoff
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)





P_20  = np.exp(beta * Nutzen(20))  / (np.exp(beta * Nutzen(20) ) + np.exp(beta * R) )
# P_20  = np.exp(beta * Nutzen(20)) / (np.exp(beta * Nutzen(20)) + np.exp(beta * Nutzen(R)) + np.exp(beta * Nutzen(R)))
P_50  = np.exp(beta * Nutzen(50))  / (np.exp(beta * Nutzen(50) ) + np.exp(beta * R) )
P_80  = np.exp(beta * Nutzen(80))  / (np.exp(beta * Nutzen(80) ) + np.exp(beta * R) )
P_110 = np.exp(beta * Nutzen(110)) / (np.exp(beta * Nutzen(110)) + np.exp(beta * R) )
#P_equ = np.exp(beta * R) / (np.exp(beta * R) + np.exp(beta * R) + np.exp(beta * R))





plt.plot(R, P_20, R, P_50, R, P_80, R, P_110)#, R, P_equ)
plt.xlabel('Aufwand der Alternativen')  # string must be enclosed with quotes '  '
plt.ylabel('P für Alternativen')
plt.title('Aufteilungsmodell: LOGIT')
#plt.legend(['beta 1', 'beta 2', 'beta 3'])      # legend entries as seperate strings in a list
plt.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)
plt.show()

print('ggg')
R=40
print(np.exp(beta * Nutzen(20))  / (np.exp(beta * Nutzen(20) ) + np.exp(beta * R) ))

print(1-P_Logit([20,40]))

#plt.savefig('Utility-func-plots/Kirchhoff.png')
#plt.clf()

