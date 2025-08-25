#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : selfkwargs

"""
This function sets all attributes defined in kwargs dictionnary to self instance.
"""



# %% Libraries
from corelp import *



# %% Function
def selfkwargs(**kwargs) :
    '''
    This function sets all attributes defined in kwargs dictionnary to self instance.
    
    Parameters
    ----------
    a : int or float
        TODO.

    Returns
    -------
    b : int or float
        TODO.

    Raises
    ------
    TypeError
        TODO.

    Examples
    --------
    >>> selfkwargs(TODO)
    TODO
    '''

    return None



# %% Class
class selfkwargs() :
    '''
    This function sets all attributes defined in kwargs dictionnary to self instance.
    
    Parameters
    ----------
    a : int or float
        TODO.

    Attributes
    ----------
    _attr : int or float
        TODO.

    Examples
    --------
    >>> selfkwargs(TODO)
    TODO
    '''

    def __init__(self) :
        pass
    
    def method(self) :
        '''
        TODO
    
        Parameters
        ----------
        a : int or float
            TODO.

        Returns
        -------
        b : int or float
            TODO.

        Raises
        ------
        TypeError
            TODO.

        Examples
        --------
        >>> self.method(TODO)
        TODO
        '''

        return None



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)