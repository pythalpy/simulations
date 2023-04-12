
"""
Created on Mon Mar 30 21:53:58 2020

@author: jaanisar
"""

import cantera as ct
import numpy as np

gas1 = ct.Solution('gri30.xml')

print("hi")
print("gas1 is ", gas1)

gas1()

gas1.TP = 1200, 101325

gas1()

# All of these commands will yield the same state and are essentially equivalent
# >>> gas1.TP = 1200, 101325           # temperature, pressure
# >>> gas1.TD = 1200, 0.0204723        # temperature, density
# >>> gas1.HP = 1.32956e7, 101325      # specific enthalpy, pressure
# >>> gas1.UV = 8.34619e6, 1/0.0204723 # specific internal energy, specific volume
# >>> gas1.SP = 85227.6, 101325        # specific entropy, pressure
# >>> gas1.SV = 85227.6, 1/0.0204723   # specific entropy, specific volume

gas1.TPX = 1200, 101325, 'CH4:1, O2:2, N2:7.52'
gas1()