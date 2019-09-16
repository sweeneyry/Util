# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:25:33 2017

@author: sweener

Developer     Date        Comment
R. Sweeney    16/06/17    initial development


PURPOSE: to write 2D data to a file. This function can be used alone, or can 
be used together with append_2D_Data_To_File in order to write 3D data.

INPUT           TYPE                    UNIT            DESCRIPTION
Data            NxM Vector[float]       ---             the data to be written
                                                        to file
Filename        String                  ---             the full path and filename                                                        

OUTPUT          TYPE            UNIT            DESCRIPTION
                                                

"""

import numpy as np

def write_2D_Data_To_File(Data, Filename, Append):
    
    if Append==0:
        # we start by opening a file with the name Filename. The default here is to
        # overwrite if a file exists. 
        with open(Filename, 'w') as file:
        
            numRows = (np.shape(Data))[0]
            
            for i in range(0,numRows):
                thisRow = Data[i,:]
                file.write(np.array2string(thisRow, max_line_width=200, 
                                           separator='\t')[1:-1] +'\n')

    else:
        with open(Filename, 'a') as file:
        
            numRows = (np.shape(Data))[0]

            file.write('\n')
            
            for i in range(0,numRows):
                thisRow = Data[i,:]
                file.write(np.array2string(thisRow, max_line_width=200, 
                                           separator='\t')[1:-1] + '\n')        
    