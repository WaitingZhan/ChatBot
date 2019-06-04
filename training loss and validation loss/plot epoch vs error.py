#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:52:34 2019

@author: weitingzhan
"""



import numpy as np


# Importing the dataset
lines = open('chatbot1 5epoch 0.001.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')



training_error = []
validation_error= []


for line in lines:
    if "Validation Loss Error" in line:
        validation_error.append(float(line[24:29]))
    if "Training Loss Error" in line:
        training_error.append(float(line[54:59]))
        

epoch_training = np.arange(0,5,5/275)
epoch_validation=np.arange(0.5,5.5,0.5)

import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x_train = training_error
x_validation = validation_error
y_train = epoch_training 
y_validation = epoch_validation

# Plot the points using matplotlib
plt.plot(y_train,x_train )
plt.plot(y_validation,x_validation)
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.title('chatbot3 5 layer learning rate =0.001 Error over Epoch')
plt.legend(['Trainig', 'Validation'])
plt.show()





        
    
        
