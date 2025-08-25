#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP

"""
This file allows to test getmodule

getmodule : This function is to be used in a library __init__ file. It creates lazy imports of the module imported and defines __getattr__ and __all__ for this library.
"""



# %% Libraries
from corelp import print, debug
import pytest
from corelp import getmodule
path = debug(__file__)



# %% Instance fixture
@pytest.fixture()
def instance() :
    '''
    Create a new instance at each test function
    '''
    return getmodule()



# %% Returns test
@pytest.mark.parametrize("args, kwargs, expected, message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_returns(args, kwargs, expected, message) -> None :
    '''
    Test getmodule return values
    '''
    assert getmodule(*args, **kwargs) == expected, message



# %% Error test
@pytest.mark.parametrize("args, kwargs, error, error_message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_errors(args, kwargs, error, error_message) -> None :
    '''
    Test getmodule error values
    '''
    with pytest.raises(error, match=error_message) :
        getmodule(*args, **kwargs)



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)