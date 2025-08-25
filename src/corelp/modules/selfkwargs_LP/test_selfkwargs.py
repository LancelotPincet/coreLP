#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP

"""
This file allows to test selfkwargs

selfkwargs : This function sets all attributes defined in kwargs dictionnary to self instance.
"""



# %% Libraries
from corelp import print
import pytest
from corelp import selfkwargs



# %% Instance fixture
@pytest.fixture()
def instance() :
    '''
    Create a new instance at each test function
    '''
    return selfkwargs()



# %% Returns test
@pytest.mark.parametrize("args, kwargs, expected, message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_returns(args, kwargs, expected, message) -> None :
    '''
    Test selfkwargs return values
    '''
    assert selfkwargs(*args, **kwargs) == expected, message



# %% Error test
@pytest.mark.parametrize("args, kwargs, error, error_message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_errors(args, kwargs, error, error_message) -> None :
    '''
    Test selfkwargs error values
    '''
    with pytest.raises(error, match=error_message) :
        selfkwargs(*args, **kwargs)



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)