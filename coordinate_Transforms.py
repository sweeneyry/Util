#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:33:00 2020

@author: Ryan
"""

import numpy as np

def rpz_XYZ(rpz):
    '''
    

    Parameters
    ----------
    rpz : 3xN array of R, phi, and Z coordinates
        This function converts from R, phi, and Z 
        to cartesian.

    Returns
    -------
    XYZ.

    '''
    
    if np.shape(rpz)[0] != 3:
        rpz = rpz.T
        
    if np.shape(rpz)[0] != 3:   
        raise ValueError('Input to rpz_XYZ does not start with a dimenion of length 3')

    XYZ = rpz*0.
    XYZ[0,:] = rpz[0,:]*np.cos(rpz[1,:])
    XYZ[1,:] = rpz[0,:]*np.sin(rpz[1,:])
    XYZ[2,:] = rpz[2,:]
    
    return XYZ


def xyz_RPZ(XYZ, PhiOffset = 0., Sign=1.):
    '''
    

    Parameters
    ----------
    XYZ : 3xN array of X, Y, and Z
    PhiOffset: Scalar in radians
    Sign: Scalar, should be +1 or -1

    Returns
    -------
    rpz

    '''
    
    if np.shape(XYZ)[0] != 3:
        raise ValueError('Input to xyz_RPZ does not start with a dimenion of length 3')    

    rpz = XYZ*0.
    rpz[0,:] = np.sqrt(XYZ[0,:]**2 + XYZ[1,:]**2)
    rpz[1,:] = Sign*np.arctan2(XYZ[0,:], XYZ[1,:]) + PhiOffset
    rpz[2,:] = XYZ[2,:]
    
    
    return rpz
