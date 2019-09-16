# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:51:56 2017

@author: sweener

Developer     Date        Comment
R. Sweeney    26/01/17    initial development

PURPOSE: given a directory and filename of an Excel sheet (fullFileName), 
read all columns and rows into a 2D array.
"""

from openpyxl import load_workbook

def read_XLSheet_To_Array(FullFileName, SheetName):
    
    
    
    #load the workbook
    workBook = load_workbook(filename=FullFileName, read_only=True)
    
    workSheet = workBook[SheetName]
    return workSheet
    


