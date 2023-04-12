#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:11:59 2021

@author: jaanisar
"""
#import thermopy
#from thermopy import nasa9polynomials as nasa9
#db = nasa9.Database()
#uf6 = db.set_compound('uf6(cr)')
#print(uf6)


import thermopy
from thermopy import nasa9polynomials as nasa9
db = nasa9.Database()
li = db.set_compound('Li')
temp = thermopy.constants.C2K(130)


print(li, '- Heat capacity -', li.heat_capacity(temp))
print(li, '- Enthalpy -', li.enthalpy(temp))
print(li, '- Entropy -', li.entropy(temp))
print(li, '- Gibbs Energy -', li.gibbs_energy(temp))
print(li, '- Molecular Weight -', li.molecular_weight)
print(li, '- Reference -', li.reference)
print(li, '- IUPAC NAME -', li.iupac_name)
print(li, '- INP Name -', li.inp_name)

print(li, '- Enthalpy of Formation -', li.enthalpy_of_formation)
print(li, '- Condensed, bool -', li.condensed)
#lithium;bromide: LiBr - 39.6593057506


lico = db.set_compound('O')
print(lico, '- Heat capacity -', lico.heat_capacity(temp))

co = db.set_compound('LiCo')
print(co, '- Heat capacity -', co.heat_capacity(temp))
