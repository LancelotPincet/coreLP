#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : getmodule

"""
This function is to be used in a library __init__ file. It creates lazy imports of the module imported and defines __getattr__ and __all__ for this library.
"""



# %% Libraries
from pathlib import Path
import json



# %% Function
def getmodule(file) -> None :
    '''
    This function is to be used in a library __init__ file. It creates lazy imports of the module imported and defines __getattr__ and __all__ for this library.
    
    Parameters
    ----------
    file : str
        __file__ string in the __init__.py file.

    Returns
    -------
    _getattr : function
        Function to replace __init__.py __getattr__ variable.
    _all : list
        list of module names corresponding to __all__.

    Examples
    --------
    # In __init__.py file
    __getattr__, __all__ = getmodule(__file__)
    '''

    # Get paths
    file = Path(file)
    libfolder = file.parent
    modulesjson = libfolder / 'modules.json'
    



    return None



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)