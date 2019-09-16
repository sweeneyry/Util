# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:29:58 2017

@author: sweener
"""
import numpy as np

def curve_Transition(t0, dur, valStart, valEnd, timeArray):
    return 0.5*(valStart-valEnd)*(np.tanh(-(timeArray - t0)/dur) + 1) + valEnd   
