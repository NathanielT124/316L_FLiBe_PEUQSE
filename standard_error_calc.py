# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:54:04 2022

@author: NWT

This program estimates the uncertainty associated with the diffusion 
coefficient for Cr from weight loss data.
"""
from scipy.stats import sem
import math
import numpy as np


si = True

####################################Uncertainties##############################

# Estmated uncertainty for a Vernier caliper
unc_lwh = 0.001 # cm

# Surface area calculation
l = 13E-1 # cm
w = 7E-1 # cm
h = 1E-1 # cm
So = 2*l*w + 2*w*h + 2*l*h # cm^2

if si:
    So = So*10**-4 # m^2
    unc_lwh = unc_lwh*10**-2 # m^2

# Surface area uncertainty
unc_So = math.sqrt(((2*l*w)*math.sqrt(((unc_lwh/l)**2 + (unc_lwh/w)**2)))**2
                 + ((2*w*h)*math.sqrt(((unc_lwh/w)**2 + (unc_lwh/h)**2)))**2
                 + ((2*l*h)*math.sqrt(((unc_lwh/l)**2 + (unc_lwh/h)**2)))**2)

if si:
    print("Surface area:\t\t{:f} ± {:f} m^2\n"
      .format(So, unc_So), )
else:
    print("Surface area:\t\t{:.3f} ± {:.3f} cm^2\n"
      .format(So, unc_So), )

# Starting concentration
Co = 16.825 # wt.%

# Guess for concentration uncertainty
unc_Co = 1.0 # wt.%

# time
t_3 = 3000 # hr
t_2 = 2000 # hr
t_1 = 1000 # hr

if si:
    t_3 *= 3600 # s
    t_2 *= 3600 # s
    t_1 *= 3600 # s
    
####################################3000 Hours#################################
# Weight loss (mg/cm^2) values estimated from graphs provided in Dr. Zheng's
# paper

weight_loss_3 = [0.456, 0.5499] # mg/cm^2

# Standard error calculated
unc_DW_3 = sem(weight_loss_3)*10**-2 # mg/cm^2

# Mean value of weight loss
DW_3= sum(weight_loss_3)/len(weight_loss_3) # mg/cm^2

if si:
    unc_DW_3 = unc_DW_3 * 10 ** -2 # kg/m^2
    DW_3 = DW_3 * 10 ** -2 # kg/m^2

# Conversion to absolute weight
DWa_3 = DW_3 * So # mg (kg if si = True)

# Propogated Error of absolute weight
unc_DWa_3 = DW_3 * math.sqrt((unc_DW_3/DW_3)**2 + (unc_So/So)**2)**2

if si:
    print("Weight loss for {:d} seconds:\t{:} ± {:} kg"
          .format(t_3, DWa_3, unc_DWa_3))
else:
    print("Weight loss for {:d} hours:\t{:.3f} ± {:.3f} mg"
          .format(t_3, DWa_3, unc_DWa_3))

# Diffusion coefficient
Deff_3 = ((DWa_3)**2*math.pi)/(4*So**2*Co**2*t_3)

# Diffusion coefficient uncertainty
unc_Deff_3 = Deff_3*math.sqrt(2*(unc_DWa_3/DWa_3)**2 + 2*(unc_So/So)**2 + 2*(unc_Co/Co)**2)

if si:
    print("Deff for {:d} seconds:\t{:} ± {:} m^2/s\n"
          .format(t_3, Deff_3, unc_Deff_3))
else:
    print("Deff for {:d} hours:\t{:} ± {:} m^2/s\n"
          .format(t_3, Deff_3, unc_Deff_3))

####################################2000 Hours#################################
# Weight loss (mg/cm^2) values estimated from graphs provided in Dr. Zheng's
# paper
weight_loss_2 = [0.38333, 0.35] # mg/cm^2

# Standard error calculated
unc_DW_2 = sem(weight_loss_2)*10**-2 # mg/cm^2
if si:
    unc_DW_2 = unc_DW_2 * 10 ** -2 # kg/m^2

# Mean value of weight loss
DW_2 = sum(weight_loss_2)/len(weight_loss_2) # mg/cm^2
if si:
    DW_2 = DW_2 * 10 ** -2 # kg/m^2

if si:
    t_2 = t_2 * 3600 # s

# Conversion to absolute weight
DWa_2 = DW_2 * So # mg (kg if si = True)

# Propogated Error of absolute weight
unc_DWa_2 = DW_2*math.sqrt((unc_DW_2/DW_2)**2 + (unc_So/So)**2)**2

if si:
    print("Weight loss for {:d} seconds:\t{:} ± {:} kg"
          .format(t_2, DWa_2, unc_DWa_2))
else:
    print("Weight loss for {:d} hours:\t{:.3f} ± {:.3f} mg"
          .format(t_2, DWa_2, unc_DWa_2))

# Diffusion coefficient
Deff_2 = ((DWa_2)**2*math.pi)/(4*So**2*Co**2*t_2)

# Diffusion coefficient uncertainty
unc_Deff_2 = Deff_2*math.sqrt(2*(unc_DWa_2/DWa_2)**2 + 2*(unc_So/So)**2 + 2*(unc_Co/Co)**2)

if si:
    print("Deff for {:d} seconds:\t{:} ± {:} m^2/s\n"
          .format(t_2, Deff_2, unc_Deff_2))
else:
    print("Deff for {:d} hours:\t{:} ± {:} m^2/s\n"
          .format(t_2, Deff_2, unc_Deff_2))

####################################1000 Hours#################################
# Weight loss (mg/cm^2) values estimated from graphs provided in Dr. Zheng's
# paper
weight_loss_1 = [0.1749, .2125]

# Standard error calculated
unc_DW_1 = sem(weight_loss_1) 
if si:
    unc_DW_1 = unc_DW_2 * 10 ** -2 # kg/m^2

# Mean value of weight loss
DW_1 = sum(weight_loss_1)/len(weight_loss_1) # mg/cm^2
if si:
    DW_1 = DW_1 * 10 ** -2 # kg/m^2

if si:
    t_1 = t_1 * 3600 # s

# Conversion to absolute weight
DWa_1 = DW_1 * So # mg (kg if si = True)

# Propogated Error of absolute weight
unc_DWa_1 = DW_1*math.sqrt((unc_DW_1/DW_1)**2 + (unc_So/So)**2)**2

if si:
    print("Weight loss for {:d} seconds:\t{:} ± {:} kg"
          .format(t_1, DWa_1, unc_DWa_1))
else:
    print("Weight loss for {:d} hours:\t{:.3f} ± {:.3f} mg"
          .format(t_1, DWa_1, unc_DWa_1))

# Diffusion coefficient
Deff_1 = ((DWa_1)**2*math.pi)/(4*So**2*Co**2*t_2)

# Diffusion coefficient uncertainty
unc_Deff_1 = Deff_1*math.sqrt(2*(unc_DWa_1/DWa_1)**2 + 2*(unc_So/So)**2 + 2*(unc_Co/Co)**2)

if si:
    print("Deff for {:d} seconds:\t{:} ± {:} m^2/s\n"
          .format(t_2, Deff_1, unc_Deff_1))
else:
    print("Deff for {:d} hours:\t{:} ± {:} m^2/s\n"
          .format(t_2, Deff_1, unc_Deff_1))
    
##########################Diffusion Coefficient Average########################

Deff_arr = [Deff_1, Deff_2, Deff_3]

Deff = sum(Deff_arr)/len(Deff_arr)
print("Diffusion Coefficient:\t{:} m^2/s".format(Deff))

# Standard error calculated
std_err_Deff = sem(Deff_arr)
