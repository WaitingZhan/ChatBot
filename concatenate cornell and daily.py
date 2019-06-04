#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:02:40 2019

@author: weitingzhan
"""

# Importing the libraries
import numpy as np
import tensorflow as tf
import re
import time
 
answercornel = open('answerOfCornel.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
answerdialy = open('answerOfDialylogue.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

answerconcatenate=answercornel+answerdialy

with open('answerconcatenate.txt', 'w') as f:
    for item in answerconcatenate:
        f.write("%s\n" % item)


questionscornel = open('questionsOfCornell.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
questionsdialy = open('questionsOfDialylogue.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

questionsconcatenate=questionscornel+questionsdialy

with open('questionsconcatenate.txt', 'w') as f:
    for item in questionsconcatenate:
        f.write("%s\n" % item)
