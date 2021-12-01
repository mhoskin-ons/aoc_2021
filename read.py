# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:21:47 2021

@author: Mike
"""

import os


def get_filepath(instance, folder='inputs/', test=False):
    
    if test:
        version = 'test'
    else:
        version = 'input'
    
    fp = "D:/aoc_2021/{0}day_{1}_{2}.txt".format(folder, instance, version)
    
    return fp

def read_input(instance,
               clean=True,
               strip=True,
               cast_type=None,
               split=None,
               sort=False,
               test=False):

    fp = get_filepath(instance, test=test)
    
    with open(fp) as f:
        
        data = f.readlines()
        
        if clean:
            clean_data = data
            
            if strip:
                clean_data = [d.strip() for d in clean_data]
            
            if cast_type:
                clean_data = [int(d) for d in clean_data]
         
            if split:
                clean_data = [d.split(split) for d in clean_data]
                
            if sort:        
                clean_data.sort()
                
        else:
            clean_data = data
            
            
        return clean_data