#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# /// script
# requires-python = ">=template_scriptversion"
# dependencies = [coreLP, coreLP]
# ///

# Date          : 2025-08-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP

"""
just a test
"""



# %% User inputs

# Run execution
import_path = None # r'' # Path to the imported data
export_path = import_path # Path to the exported data
new = False # True to create new result folder at each run

# Other parameters
# TODO



# %% Libraries
from corelp import main, folder, print



# %% Function
@main()
def my_script() :
    '''
    just a test

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
    >>> from template_modulelowerlib import template_modulename
    ...
    >>> template_modulename() # TODO
    '''

    # Initialization
    result = initialization()

    return result



@my_script.section()
def initialization() :
    print("Hello from section")
    return None



# %% Main function run
if __name__ == "__main__":
    my_script()