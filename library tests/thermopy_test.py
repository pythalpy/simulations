#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:18:59 2020

@author: jaanisar
"""

#from thermopy import units, iapws
from thermopy.units import Enthalpy, Length, Pressure
from thermopy.iapws import Water

h = Enthalpy(100000)
h = h.kJkg
print(h, 'kiloJoules per kilogram')
hb = h.Btulb
print(hb, "Btulb")
hk = h.kcalkg
print(hk, "Kilocalorie per kg (kcalkg)")


#class thermopy.units.Enthalpy
#    h = Enthalpy(1000)


len = Length(1)

print(len, 'meter', "default unit for length")
lenf = len.ft
lenm = len.mm
print("%.2f" % lenf, 'ft')
print("%.2f" % lenm, 'mm' )

p = Pressure(1.0).unit('atm')
print("%.2f" % p, "Pa")
print("%.2f" % p.atm, "atm, pressure")
p2 = p.psi
print("%.2f" % p2, "psi")

wh = Water.heat_capacity(p=1, T=200)
print(wh)