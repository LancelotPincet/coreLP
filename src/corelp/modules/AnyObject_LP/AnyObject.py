#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : AnyObject

"""
Class that just stores keys as attributes.
"""



# %% Libraries
from corelp import selfkwargs



# %% Class
class AnyObject() :
    '''
    Class that just stores keys as attributes.

    Examples
    --------
    >>> from corelp import AnyObject
    ...
    >>> instance = AnyObject(x=1, y=2)
    >>> instance.x # returns 1
    '''

    # Init
    def __init__(self, **kwargs) :
        selfkwargs(self, kwargs)



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)