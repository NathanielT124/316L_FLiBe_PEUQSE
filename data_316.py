# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:41:40 2022

@author: NWT

This data file contains the data for chromium concentration with relation to
depth in a sample of 316L stainless steel that was exposed to FLiBe salt in a
static testing apparatus for 3000 hours at 700 C.

Distances are in micrometers and concentrations are in weight percent.

Associated error with uncertainty is also provided.
"""

# Distances in the sample, starting from salt-side surface (0 μ), (Units: μ)
distances = [0,0.386,0.773,1.16,1.55,1.93,2.32,2.71,3.09,3.48,3.86,4.25,4.64,
             5.02,5.41,5.8,6.18,6.57,6.96,7.34,7.73,8.12,8.5,8.89,9.28,9.66,
             10,10.4,10.8,11.2,11.6,12,12.4,12.8,13.1,13.5,13.9,14.3,14.7,15.1,
             15.5,15.8,16.2,16.6,17,17.4,17.8,18.2,18.6,18.9,19.3,19.7,20.1,
             20.5,20.9,21.3,21.6,22,22.4,22.8,23.2,23.6,24,24.3,24.7,25.1,25.5,
             25.9,26.3,26.7,27.1,27.4,27.8,28.2,28.6,29,29.4,29.8,30.1,30.5,
             30.9,31.3,31.7,32.1,32.5,32.9,33.2,33.6,34,34.4,34.8,35.2,35.6,
             35.9,36.3,36.7,37.1,37.5,37.9,38.3,38.6,39,39.4,39.8,40.2,40.6,41,
             41.4,41.7,42.1,42.5,42.9,43.3,43.7,44.1,44.4,44.8,45.2,45.6,46,
             46.4,46.8,47.2,47.5,47.9,48.3,48.7,49.1,49.5,49.9,50.2,50.6,51,
             51.4,51.8,52.2,52.6,52.9]

# Average Cr concetration at depths (Unit: wt%)
concentrations = [5.649085667,7.688482667,8.510341667,9.401538,10.57589767,
                  12.067913,12.71014167,13.15289167,13.552323,13.54302067,
                  14.12042033,14.421831,14.113206,13.92755867,13.987807,
                  13.955479,14.27017933,13.90192533,15.06476,15.580653,
                  15.497984,16.15180933,16.055366,16.43585267,17.11448233,
                  16.69511533,15.860878,15.73229233,15.937999,15.63428433,
                  15.542627,16.74897033,16.76517933,16.62586,16.75892967,
                  17.01214633,16.80456,16.828307,17.191794,16.97519367,
                  17.616016,16.96103433,17.19128967,17.23127833,16.96657133,
                  16.81497933,16.898162,17.13517633,16.88267833,17.19459267,
                  17.79429833,17.517832,17.187431,17.383171,16.990063,
                  16.656632,17.17614133,17.57726133,17.366358,17.87718567,
                  18.01960667,17.87313233,17.671138,18.00169833,18.066511,
                  17.557027,17.40478067,17.20154033,17.153371,17.00175667,
                  17.16058933,17.58217967,17.469499,17.46274767,17.72665433,
                  17.13499133,17.814536,17.25592267,17.514605,17.35129067,
                  17.92936067,17.92258,17.76777733,17.89765067,18.06886433,
                  18.20515767,17.75920233,17.21598467,17.18574067,17.130705,
                  17.29908133,17.43235067,17.48181067,17.53035567,17.54269333,
                  17.65084367,17.011694,17.08063633,17.685826,17.99854367,
                  17.58909533,17.38224233,17.40392533,17.15877733,17.31344433,
                  17.15385733,17.810507,18.15833533,17.84133833,17.04855033,
                  17.10523867,17.43731233,17.934701,18.07312533,17.978267,
                  18.015701,17.793433,17.51338867,17.55325667,17.36785633,
                  17.480741,17.025134,17.23737467,17.70597133,17.901378,
                  17.459247,17.81766767,17.953526,17.860788,18.35224467,
                  18.45511933,18.21138733,18.15116267,18.14145567,17.89169167,
                  17.98771533,17.98240833,18.16675533]

# Error associated with Cr concentration measurements
errors = [0.666174,0.895389667,0.827578333,0.803079333,0.806171333,0.824434,
          0.820237333,0.836283333,0.847239333,0.839054,0.855969,0.860858667,
          0.855350333,0.849727667,0.850466667,0.841316333,0.855300333,
          0.862006333,0.878659667,0.879982667,0.900127333,0.898706333,
          0.895793667,0.911831333,0.933185,0.908587333,0.884389333,0.891548667,
          0.892142,0.887333667,0.879653667,0.912084333,0.916218667,0.916511333,
          0.916177667,0.920143333,0.909378667,0.906207,0.922191333,0.920043,
          0.915121333,0.917206667,0.921774,0.925252667,0.917252333,0.910933667,
          0.906108667,0.901159333,0.918251667,0.921135,0.931752,0.918242,
          0.8941,0.919319,0.897632667,0.898503667,0.923598667,0.920245667,
          0.921018667,0.929814667,0.943488667,0.942165,0.939363333,0.932749,
          0.941704667,0.931125333,0.906600667,0.918645,0.900874,0.903112,
          0.922687,0.919956333,0.902934667,0.914096333,0.915230333,0.893767667,
          0.906621333,0.915818,0.928697,0.911960333,0.929689333,0.922644,
          0.924628667,0.934199,0.931220333,0.937868,0.916700667,0.908828,
          0.913982667,0.906017667,0.921105333,0.922866,0.934375,0.926206333,
          0.941624667,0.948632667,0.910054,0.926095333,0.928867667,0.905881,
          0.906099,0.925699667,0.937748333,0.902570333,0.922179,0.918024333,
          0.946495667,0.942854,0.930755333,0.916368,0.90724,0.907514667,
          0.907156667,0.925218333,0.934412,0.914565,0.924506667,0.925582667,
          0.929534,0.91593,0.937856,0.930840667,0.919908,0.905098333,0.908173,
          0.916052667,0.932029333,0.936590667,0.944733,0.945042333,0.945471333,
          0.930543667,0.924654667,0.922035,0.943556,0.944259,0.942084333,
          0.919133,]

if __name__ == "__main__":
    
    def cr_plot(C0, Dcr, t, Cs):
        calc_conc = []
        for x in distances:
            calc_conc.append( (Cs-C0)*(1-sp.erf(((x*10**(-6)))/
                                                (2*np.sqrt(Dcr*t*3600)))) + C0)
        return calc_conc
    
    print("data_316.py: Running independently.")
    import matplotlib.pyplot as plt
    import math
    import numpy as np
    import scipy.special as sp
    
    # For plotting with various times
    def time_plot(post, t, fig, unc):
        Dcr = post[0]
        C0 =  post[1]
        Cs = post[2]
        
        calc_conc = []
        # Generate simulation data
        for x in distances:
            calc_conc.append( (Cs-C0)*(1-sp.erf(((x*10**(-6)))/
                                                (2*np.sqrt(Dcr*t*3600)))) + C0)
            
        # Show plot
        plt.figure(fig)
        plt.xlim([-2, 55])
        plt.ylim([-1, 20])
        plt.title("700$^\circ$C 316L FLiBe exposure chromium depletion"
                  "(uncertainty = {:})".format(unc))
        plt.ylabel("Concentration (wt%)")
        plt.xlabel("Distance (μm)")
        plt.grid()
        plt.plot(distances, calc_conc)
        
    # For plotting against experimental data and literature function
    def plot_conc(post, t, fig, unc):
         calc_conc = []
    
         # Informed posteriors from PEUQSE simulation
         Dcr = post[0]
         C0 =  post[1]
         Cs = post[2]
    
         # Generate simulation data
         for x in distances:
             calc_conc.append( (Cs-C0)*(1-sp.erf(((x*10**(-6)))/
                                                 (2*np.sqrt(Dcr*t*3600)))) + C0)
         
         # Plot experimental vs simulated    
         plt.figure(fig)
         plt.xlim([-2, 55])
         plt.ylim([-1, 20])
         plt.errorbar(distances, concentrations, errors, elinewidth=.5,
                      capsize=5)
         plt.title("{:d} hr, 700$^\circ$C 316L FLiBe exposure chromium"
                   " depletion (d_eff_unc = {:})".format(t, unc))
         plt.ylabel("Concentration (wt%)")
         plt.xlabel("Distance (μm)")
         plt.grid()
         plt.plot(distances, calc_conc, color = 'k')    
         
         # Plot original literature function
         DeffCr = 4.2e-19
         C0Cr =  1.6825e+01

         calc_orig = cr_plot(C0Cr, DeffCr, t, 0)
             
         plt.plot(distances, calc_orig, color = 'g')
         plt.legend(["Bayesian Estimate", "Zheng 2016","Experimental Values"])
         
    # For plotting with various times
    def unc_plot(post, t, fig, unc):
        Dcr = post[0]
        C0 =  post[1]
        Cs = post[2]
        
        calc_conc = cr_plot(C0, Dcr, t, Cs)
            
        # Show plot
        plt.figure(fig)
        plt.xlim([-2, 55])
        plt.ylim([-1, 20])
        plt.title("700$^\circ$C 316L FLiBe exposure chromium depletion"
                  " (time = {:d} year)".format(int(t/8760)))
        plt.ylabel("Concentration wt.%")
        plt.xlabel("Distance (μm)")
        plt.grid()
        plt.plot(distances, calc_conc)
        
    # PEUQSE parameters for diffusion coefficient, initial chromium
    # concentration, and surface concetrations. Contains parameters for input
    # uncertainties from 0.001 to 10.0.
    post = [
        [-18.37662834,17.17533593,5.8096967], # Unc =  0.001
        [-18.36896044,17.18043372,5.8214373], # Unc =  0.01
        [-18.0852596,17.33055159,6.73997813], # Unc =  0.1
        [-17.95542376,17.40883499,7.17941649],# Unc =  1.0
        [-17.945498,17.41017418,7.20821043]   # Unc = 10.0
        ]
    
    # Uncertainties
    unc = [0.001, 0.01, 0.1, 1.0, 10.0]
    
    # Experimental timescales 1000, 2000, and 3000 hours
    times = [1000, 2000, 3000, 8760, 8760*40]
    
    # Convert from log scale to true value
    for i in range(len(post)):
            post[i][0] = 10**post[i][0]
    
    
    # Generate plots
    fig = 0
    for i in range(0,5):
        plot_conc(post[i], times[2], fig, unc[i])
        fig += 1
        
        # Make plots for different timescales
        for j in range(len(times)):
            time_plot(post[i], times[j], fig, unc[i])
        
        plt.figure(fig)
        plt.legend(["{:d} hours".format(times[0]),"{:d} hours"
                    .format(times[1]), "{:d} hours".format(times[2])
                   ,"{:d} year".format(int(times[3]/8760))
                   ,"{:d} years".format(int(times[4]/8760))])
        fig += 1
    
    
    # Make plots for different uncertainties
    for i in range(0,5,2):
        unc_plot(post[i], times[3], fig, unc[i])

    plt.figure(fig)
    plt.legend(["d_eff_unc = {:}".format(unc[0]),"d_eff_unc = {:}"
                .format(unc[2]), "d_eff_unc = {:}".format(unc[4])])