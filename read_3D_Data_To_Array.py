# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:29:13 2017

@author: sweener

Developer     Date        Comment
R. Sweeney    16/06/17    initial development
R. Sweeney    01/05/19    changed the initial numRows from 100001 back to 10001.
                          this had been changed sometime ago, but broke the 
                          z_Effective.py function. 


PURPOSE: read the file written by write_2D_Data_To_File

INPUT           TYPE                    UNIT            DESCRIPTION
Filename        String                  ---             the full path and filename                                                        

OUTPUT          TYPE            UNIT            DESCRIPTION
                                                

"""

import numpy as np

def read_3D_Data_To_Array(Filename):

    numLines = sum(1 for line in open(Filename, 'r'))
    numCols = 0
    numRows = 10001 # this default, if the file has more rows, will crash
    numSlices = 1
    data = []
    currentRow = 0
    currentSlice = 0
    
    firstRow = 1
    
    with open(Filename, 'r') as file:
        
        for line in file:
            # do something with the line
            row = list(map(float, line.split()))
            rowSize = np.size(row)
            
            # THE FOLLOWING ASSUMES THE FIRST ROW IS NOT EMPTY!!!
            if firstRow:
                numCols = rowSize
                print('rowSize', rowSize)
                data = np.zeros([numRows, numCols,numSlices])
                firstRow = 0
            
            if rowSize ==0:
                # this is an empty line break between slices
               
              
                # if the numSlices=1 then this is the first slice iteration
                if numSlices ==1:
                    numRows = currentRow
                    numSlices = int(np.round(numLines/numRows))
                    tempData = data
                    data = np.zeros([numRows, numCols, numSlices])
                    data[:,:,0] = tempData[0:numRows, :, 0]
                    
                
                currentSlice+=1
                currentRow=0
            elif rowSize == numCols: 
                # this is a usual row of data
                npArray = np.asarray(row)
                data[currentRow,:, currentSlice] = npArray
                currentRow+=1
            else:
                raise NameError('Unexpected number of elements in row')

                
    if np.all([numRows == 10001, numSlices==1]):
        numRows = currentRow
        tempData = data
        data = np.zeros([numRows, numCols, numSlices])
        data[:,:,0] = tempData[0:numRows, :, 0]  
                      
    return data[0:numRows+1, 0:numCols+1, 0:numSlices+1], numRows, numCols, numSlices
    
#filename ='C:/Users/sweener/Documents/Work/ADAS/ne_ADAS405_96_2keV_1e14.txt'
#data, numRows, numCols, numSlices = read_3D_Data_To_Array(filename)   
    
    
    
    
    