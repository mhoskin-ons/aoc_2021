# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:17:19 2021

@author: Mike
"""
from functools import wraps
from time import time


def create_blank_files(folder='inputs/', 
                       main='_input.txt',
                       test='_test.txt',
                       instances=25):
    """
    Creates empty files in preparation, of specific types and locations. 
    If already existing, has 0 effect

    Parameters
    ----------
    folder : STR, optional
        Path to write to. The default is 'inputs/'.
    main : STR, optional
        Main file suffix. The default is '_input.txt'.
    test : STR, optional
        Optional test suffix. Set to None if not desired. 
        The default is '_test.txt'.
    instances : INT, optional
        Number of instances to create

    Effects
    -------
    Creates instances of files if they don't exist.

    """
    
    for i in range(instances):
        path = folder + "day_" + str(i+1)# + "_input.txt"
        
        main_path = path + main
        open(main_path, 'a').close()
        
        if test:
            test = path + test
            open(test, 'a').close()
            
            
def time_wrap(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print('func:{0}, took: {1} sec'.format(f.__name__, te-ts))
        return result
    return wrap