#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : main

"""
This decorator is to put above your main function for scripts to improve user-friendliness
"""



# %% Libraries
from corelp import *



# %% Function
def main(**kwargs) :
    '''
    This decorator is to put above your main function for scripts to improve user-friendliness
    
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
    >>> main(TODO)
    TODO
    '''

    return None



# %% Class
class main() :
    '''
    This decorator is to put above your main function for scripts to improve user-friendliness
    
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
    >>> main(TODO)
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