# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:22:42 2022

@author: NWT
"""

import sys; sys.path.insert(0, '../../');  import PEUQSE as PEUQSE
import PEUQSE.UserInput as UserInput

if __name__ == "__main__":
    import data_316 #Just a simple example. The user can also put the values in directly into the runfile or extract from a csv, for example.
    import function_316 #Simple example.
        
    #Provide the observed X values and Y values and uncertainties -- all should be arrays or lists with nesting like [[1,2,3]] or [[1,2,3,4],[4,5,6,6]]
    UserInput.responses['responses_abscissa'] = data_316.distances
    UserInput.responses['responses_observed'] = data_316.concentrations
    UserInput.responses['responses_observed_uncertainties'] = data_316.errors
   
    #Optional: provide labels for the responses axes and parameter names.
    UserInput.simulated_response_plot_settings['x_label'] = 'distance (um)'
    UserInput.simulated_response_plot_settings['y_label'] = r'$Concentration (wt\%)$'
    UserInput.model['parameterNamesAndMathTypeExpressionsDict'] = {'a':'a','b':'b'}
    
    #Provide the prior distribution and uncertainties of the individual parameters.
    UserInput.model['InputParameterPriorValues'] = [4.2E-19, 16.825, -1.5] # , 0.5] #prior expected values for a and b
    UserInput.model['InputParametersPriorValuesUncertainties'] = [1E-19, 3, 1] #, 2] #required. #If user wants to use a prior with covariance, then this must be a 2D array/ list. To assume no covariance, a 1D
    UserInput.model['InputParameterPriorValues_upperBounds'] = [1E-18, 25, 0] #, 5] 
    UserInput.model['InputParameterPriorValues_lowerBounds'] = [1E-19, 10, -6] # , 0]
    UserInput.model['InputParameterInitialGuess'] = [3E-19, 17.2125, -1.60887] # , .5] #Can optionally change the initial guess to be different from prior means.

    #Provide a function that returns simulated values -- must of the same form as observed values, should be arrays or lists with nesting like [[1,2,3]] or [[1,2,3,4],[4,5,6,6]]
    UserInput.model['simulateByInputParametersOnlyFunction'] = function_316.simulation_function_wrapper #This must simulate with *only* the parameters listed above, and no other arguments.
    # UserInput.model['walkerInitialDistributionSpread. It'] = 0.25

    #mcmc length should typically be on the order of 10,000 per parameter. By default, the burn in will be the first 10% of the mcmc length.
    UserInput.parameter_estimation_settings['mcmc_length'] = 1000 #10000 is the default.
    # UserInput.parameter_estimation_settings['mcmc_walkerInitialDistribution'] = 'identical'
    #After filinlg the variables of the UserInput, now we make a 'parameter_estimation' object from it.
    PE_object = PEUQSE.parameter_estimation(UserInput)
    
    #Now we can do the mcmc!
    PE_object.doEnsembleSliceSampling()
    #Another option would be PE_object.doEnsembleSliceSampling(), one can also do grid search or an astroidal distribution search.
    
    #Finally, create all plots!
    
    PE_object.createAllPlots()
    #The createAllPlots function calls each of the below functions so that the user does not have to.    
    #    PE_object.makeHistogramsForEachParameter()    
    #    PE_object.makeSamplingScatterMatrixPlot()
    #    PE_object.createSimulatedResponsesPlots()

""" 
    #########Optional example of saving and loading PE_objects after running the mcmc.
    #########This feature requires having dill installed (pip install dill, https://pypi.org/project/dill/)
    try:
        import dill
        dillModuleExists = True
    except:
        dillModuleExists = False

    
    #Optionally, one can save a PE_object for later,if the dill module has been installed.
    if dillModuleExists == True: 
        PE_object.save_to_dill("PE_object_00a0")
        #to load a PE_object after some time, first one has to put (any) UserInput to create a PE_object, then to load from file.
        
        
        #Normally, we would do the loading and plotting in another python file, but for this example the syntax is being demonstrated below within the same file.
        PE_object2 = PEUQSE.parameter_estimation(UserInput)
        PE_object2 = PE_object2.load_from_dill("PE_object_00a0")
        PE_object2.createAllPlots()
"""