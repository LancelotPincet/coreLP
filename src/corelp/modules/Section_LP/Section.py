#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : Section

"""
This class defines decorator instances allowing to create section functions.
"""



# %% Libraries
from corelp import print, folder, selfkwargs, kwargsself
from dataclasses import dataclass, field
import pickle
from pathlib import Path
from functools import wraps
import hashlib
import inspect



# %% Class
@dataclass(slots=True, kw_only=True)
class Section() :
    '''
    This class defines decorator instances allowing to create section functions.
    Saves results into a folder, if another call occurs, can load-back the precalculated data.
    
    Parameters
    ----------
    path : str or Path
        path where to save section folder results.
    new : bool
        True to ignore pre-calculated data and crush them.
    num : int
        Index of section, after one call, adds 1 for next call.

    Examples
    --------
    >>> from corelp import Section
    ...
    >>> section = Section(path=export_path)
    ...
    >>> @section()
    ... def add(a, b=0) :
    ...     testfunc.print('Hello World')
    ...     return a + b
    ...
    >>> testfunc.print('3+0=', add(3)) # First call calculates and save result
    >>> testfunc.print('3+0=', add(3, 0)) # Second call loads back precalculated results
    >>> testfunc.print('1+3=', add(1, 3)) # New call with other parameters : crushed previous results with new ones
    >>> testfunc.print('1+3=', add(1, b=3)) # Second call with these parameters : loads precalculated results
    ...
    >>> @section() # Creates an index of 2
    ... def sub(a, b=0) :
    ...     return a - b
    ...
    >>> @section(num=10) # Creates an index of 10
    ... def mul(a, b=0) :
    ...     return a * b
    ...
    >>> @section() # Creates an index of 11
    ... def div(a, b) :
    ...     return a / b
    '''

    # Attributes
    path : Path | str = None
    new :bool = False
    num :int = 0

    # Init
    def __post_init__(self) :
        if self.path is not None :
            self.path = Path(self.path)

    # Decorator
    def __call__(self, *, new=None, num=None):
        if new is None :
            new = self.new
        if num is None :
            num = self.num
        self.num = num+1

        def decorator(func) :
            name = func.__name__

            @wraps(func)
            def wrapper(*args, **kwargs):
                wrapper.path = self.path / f"{num:03}_{name}"
                print(f'\n#### {num}. {name.replace("_"," ")} section\n')

                # Creating hash
                print('**Call hash:**')
                bound = inspect.signature(func).bind(*args, **kwargs)
                bound.apply_defaults()
                serialized = pickle.dumps(bound.arguments)
                args_hash = hashlib.md5(serialized).hexdigest()
                result_file = wrapper.path / f'{args_hash}.pkl'
                print(f'*{args_hash}*\n')

                # Checking already calculated exists
                if result_file.exists() and not new :
                    print('**Loading from *precalculated* results...**')
                    with open(result_file, 'rb') as f:
                        result = pickle.load(f)
                    print('...loaded\n')

                # New calculations
                else :
                    folder(wrapper.path, warning=False)
                    print('**Calculating results:**')
                    print_status = kwargsself(print)
                    print.file = wrapper.path / f'{name}_log.md'
                    result = func(*args, **kwargs)
                    selfkwargs(print, print_status)
                    print('...calculated\n')
                    print('**Saving results:**')
                    with open(result_file, 'wb') as f:
                        pickle.dump(result, f)
                    print('...saved\n')

                return result
            return wrapper
        return decorator





# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)