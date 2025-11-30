#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-11-30
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : user_inputs

"""
Gets last user inputs dictionnary from global variables.
"""



# %% Libraries
import inspect



# %% Function
_user_inputs = {} # User inputs cache

def user_inputs() :
    r'''
    Gets last user inputs dictionnary from global variables.
    This function should not be used by storing varriable, DO NOT DO THIS : variable = user_inputs()
    Please use directly: function(**user_inputs())
    
    Returns
    -------
    inputs : dict
        Dictionnary corresponding to user inputs.

    Examples
    --------
    >>> from corelp import user_inputs
    ...
    >>> user_inputs() # Initialization [first call to remove imports etc.]
    ...
    >>> # User inputs
    >>> a = 1
    ...
    >>> user_inputs() # Returns {'a': 1}
    '''

    frame = inspect.currentframe().f_back
    current_vars = {**frame.f_globals, **frame.f_locals}
    current_vars = {k: v for k, v in current_vars.items() if not k.startswith("_")}
    inputs = {k: v for k, v in current_vars.items() if k not in _user_inputs or _user_inputs[k] != v}
    _user_inputs.update(inputs)
    return inputs



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)