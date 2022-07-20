# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 07:37:49 2022

@author: NWT
This file graphs the value of Deff against the uncertainty provided to PEUQSE
It graphs MAP and MU_AP values, as well as standard deviations
"""
import matplotlib.pyplot as plt
import math

map_values = [-18.37662834,-18.36896044,-18.0852596,-17.95542376,-17.945498]
mu_ap_values = [-18.37667027,-18.36823056,-18.08384853,-17.9557197,-17.95503955]
std_devs = [0.00093476,0.00948315,0.05376846,0.06246781,0.0626771]
for i in range(5):
    map_values[i] = 10**map_values[i]
    mu_ap_values[i] = 10**mu_ap_values[i]

uncertainties = [0.001, 0.01, 0.1, 1.0, 10.0]
literature_values = []
for i in range(5):
    literature_values.append(4.2*10**-19)

# Create a graph of MAP values against uncertainty
plt.figure(0)
plt.plot(uncertainties, map_values, 'ko-')
plt.plot(uncertainties, literature_values, 'g--')
# Axis labels
plt.xlabel("Uncertainty")
plt.ylabel("Diffusion coefficient ($m^2$/s)")
# Axis log scale
plt.xscale("log")
plt.legend(["Bayesian Estimate","Zheng 2016"])
plt.title("Diffusion coefficient vs uncertainty")
plt.grid(True, which="both")
plt.show()

'''
# Create a graph of MU_AP values against uncertainty
plt.figure(1)
plt.plot(uncertainties, mu_ap_values, 'ko-')
plt.plot(uncertainties, literature_values, 'g--')
plt.xlabel("Uncertainty")
# Axis labels
plt.ylabel("Log base10 of diffusion coefficient")
plt.xscale("log")
plt.yscale("log")
plt.legend(["Bayesian Estimate","Zheng 2016"])
plt.title("MU_AP MAP Log base 10 of diffusion coefficient vs uncertainty")
plt.grid(True, which="both")
plt.show()

# Create a graph of standard deviations against uncertainty
plt.figure(2)
plt.plot(uncertainties, std_devs, 'ko-')
plt.xlabel("Uncertainty")
plt.ylabel("Standard deviation")
# Axis labels
plt.xscale("log")
plt.legend(["Bayesian Estimate","Zheng 2016"])
plt.title("Standard deviation of Log base 10 of diffusion coefficient vs uncertainty")
plt.grid(True, which="both")
plt.show()
'''