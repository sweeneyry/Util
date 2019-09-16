# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:47:33 2019

@author: Ryan
"""

def my_Heaviside(X):
    
    if X <= 0.:
        return 0.
    else:
        return 1.