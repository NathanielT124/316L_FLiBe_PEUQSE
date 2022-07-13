# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:22:42 2022

@author: NWT

This program uses PEUQSE to obtain realistic parameters with uncertainties to
better fit data obtained from a paper studying the corrosion of 316L stainless
steel 

"""

import sys; sys.path.insert(0, '../../');  import PEUQSE as PEUQSE
import PEUQSE.UserInput as UserInput

if __name__ == "__main__":
    import function_316
    import data_316 
        
    # Provided distances and Cr concetrations in the samples.
    UserInput.responses['responses_abscissa'] = data_316.distances
    UserInput.responses['responses_observed'] = data_316.concentrations
    UserInput.responses['responses_observed_uncertainties'] = data_316.errors
   
    # Labels for x and y axis, as well as parameter names provided.
    UserInput.simulated_response_plot_settings['x_label'] = 'distance (um)'
    UserInput.simulated_response_plot_settings['y_label'] = r'$Concentration (wt\%)$'
    UserInput.model['parameterNamesAndMathTypeExpressionsDict'] = {'a':'d_eff_cr','b':'init_cr_conc','c':'horiz_offset'}
    
    # Provided the prior distribution and uncertainties of the individual parameters.
    UserInput.model['InputParameterPriorValues'] = [4.2E-19, 16.825, -1.5]
    UserInput.model['InputParametersPriorValuesUncertainties'] = [1E-19, 3, 1]
    
    # Optional bound setting lines for finding uninformed parameters.
    # UserInput.model['InputParameterPriorValues_upperBounds'] = [None, None, None, 3] 
    # UserInput.model['InputParameterPriorValues_lowerBounds'] = [None, None, None, -3]
    
    # Guesses are provided, since the posteriors deviate significntly from literature values.
    UserInput.model['InputParameterInitialGuess'] = [3E-19, 17.2125, -1.5] 

    # Provides simulation function for Cr concentration throughout a sample
    UserInput.model['simulateByInputParametersOnlyFunction'] = function_316.simulation_function_wrapper
    # UserInput.model['walkerInitialDistributionSpread'] = 0.25 # [Optional] line to reduce initial distribution if deccesary

    # Reduced sample size needed for EnsembleSliceSampling() due to single-mode data
    UserInput.parameter_estimation_settings['mcmc_length'] = 1000 # 10000 is the default.
    
    # UserInput.parameter_estimation_settings['mcmc_walkerInitialDistribution'] = 'identical'
    #After filinlg the variables of the UserInput, now we make a 'parameter_estimation' object from it.
    PE_object = PEUQSE.parameter_estimation(UserInput)
    
    #Now we can do the mcmc!
    PE_object.doEnsembleSliceSampling()
    #Another option would be PE_object.doEnsembleSliceSampling(), one can also do grid search or an astroidal distribution search.
    
    # Create histograms and reponses only. PE_object.makeSamplingScatterMatrixPlot() does not seem to work
    PE_object.createSimulatedResponsesPlots()
    PE_object.makeHistogramsForEachParameter()

    
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