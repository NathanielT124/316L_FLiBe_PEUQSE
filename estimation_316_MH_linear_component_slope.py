# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:48:47 2022

@author: NWT
"""


import data_316

responses = [ 0.        ,  2.51489026,  4.95126385,  7.22581012,  9.29236595,
        11.04839287, 12.5674306 , 13.80136491, 14.74755127, 15.48629522,
        16.01542566, 16.40138232, 16.66511288, 16.83556269, 16.94778629,
        17.01690041, 17.05720457, 17.08115805, 17.09445374, 17.10144928,
        17.10520237, 17.10707992, 17.10797119, 17.10840285, 17.10859748,
        17.10868083, 17.1087142 , 17.10873112, 17.10873762, 17.10874003,
        17.10874089, 17.10874119, 17.10874129, 17.10874132, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133, 17.10874133, 17.10874133,
        17.10874133, 17.10874133, 17.10874133]

differences = []

for i in range(int(len(responses)/2), len(responses)):
    differences.append(data_316.concentrations[i] - responses[i])
    
print(sum(differences)/len(differences))