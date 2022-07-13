# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:27:52 2022

@author: NWT
"""

import numpy as np
import scipy
import sys

#To use PEUQSE, you can have a function, but you also need to make a function wrapper that takes *only* the parameters as a single vector.
def simulationFunction(x,a,b,c):#,d): #here x is a scalar or an array and "a" and "b" are constants for the equation.
    C0Cr = b # 16.825
    horiz_offset = c
    # linear_comp = d
    t = 3000
    x =np.array(x)
    y =  C0Cr*scipy.special.erf(
        ((x-horiz_offset)*10**-6)/(2*(a**(1/2))*t)
        ) # + linear_comp*(x-horiz_offset) # This is the same as d = (t-a)**2 + b
    #print("line 9", y)
    return y



#Now we will make a wrapper for the simulation function, since PEUQSE needs that.
x_values_for_data = []  #This is just initializing the global value to avoid confusion (see below)
#Now to populate the global variable.
import data_316 #I am using an import to show we can use the x_values associated with the observed data. Our wrapper should take only parameters and not x values.
x_values_for_data = data_316.distances
def simulation_function_wrapper(parametersArray):#this has a and b in it.
    global x_values_for_data  #It is a good idea to create a global variable to pass in the x_values for your simulation.
    a_given = parametersArray[0] #a "given" just means this wrapper will simulate using whatever a value it receives.
    b_given = parametersArray[1] #b "given" just means this wrapper will simulate using whatever b value it receives.
    c_given = parametersArray[2]
    # d_given = parametersArray[3]
    
    # try/except block returns None if a function failure is detected, or 

    y = simulationFunction(x_values_for_data, a_given, b_given, c_given) #, d_given)  #an alternatie simpler syntax to unpack the parameters would be: simulationFunction(x_values_for_data, *parametersArray) 
    # print(y)
    y_array = np.array(y)
    nans_in_array = np.isnan(y_array)
    
    if True in nans_in_array:
        # print("NaN detected")
        sys.stdout.flush()
        return None
    else:
        return y


if __name__ == "__main__":
    print("Nathaniel")
    print(simulation_function_wrapper([[1E-19],[17],[1.5]]))
    
    
    