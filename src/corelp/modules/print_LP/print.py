#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-27
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : print

"""
This function improves python print to give other functionalities.
"""



# %% Libraries
from corelp import prop
from dataclasses import dataclass



# %% Class
@dataclass(slots=True, kw_only=True)
class print() :
    '''
    This function improves python print to give other functionalities.
    It is a class instance, which prints things if called
    But other methods are available like tabulation, writting to a file, writting to a progressbar
    
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
    >>> print(TODO)
    TODO
    '''

    # Attributes
    # myattr : str = ""
    # mylist : list[str] = field(default_factory=list)
    # _mycal : str = field(init=False, repr=False) 
    name : str = None



    # Init
    def __post_init__(self) :
        pass



    # Properties
    @prop(init=False)
    def myprop(self) :
        return ""
    @myprop.setter
    def mypropr(self, value) :
        return ""



    # Methods
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