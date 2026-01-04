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

def user_inputs(start:bool=False, stop:bool=False) :
    r"""
    Return a dictionary of variables defined by the user in the interactive
    environment.

    This function is intended for use inside a main script and should be called twice, once before the user inputs, once after.
    Second call will return a dictionnary of the user inputs.

    Returns
    -------
    dict
        A dictionary containing the user's currently defined variables.

    Examples
    --------
    >>> from corelp import user_inputs
    >>> user_inputs()       # First call (initializes and clears import-related variables)
    None
    >>> a = 1               # User defines a variable
    >>> user_inputs()       # Now returns: {'a': 1}
    {'a': 1}
    """
    frame = inspect.currentframe().f_back
    ns = {**frame.f_globals, **frame.f_locals}

    # ---- Filter user variables (ignore internals starting with "_") ----
    ns = {k: v for k, v in ns.items() if not k.startswith("_")}

    # Validate status
    if user_inputs.cache is not None and start :
        user_inputs.cache = None
    if user_inputs.cache is None and stop :
        user_inputs.cache = {}

    # Case when user_inputs is on top : cache = None
    if user_inputs.cache is None :
        user_inputs.cache = ns
        return

    # Case when user_inputs is at bottom : cache = dict
    else :
        updated = { key: value for key, value in ns.items() if key not in user_inputs.cache or user_inputs.cache[key] is not value}
        user_inputs.cache = None
        return updated

user_inputs.cache = None



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)