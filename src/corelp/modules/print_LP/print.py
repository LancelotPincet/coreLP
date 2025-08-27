#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-27
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : print

"""
This function overrides python built in print function to add functionnalities.
"""



# %% Libraries



# %% Libraries
from corelp import prop
from dataclasses import dataclass
from rich import print as richprint
from rich.console import Console
from rich.theme import Theme
from time import perf_counter
import contextlib
from pathlib import Path
pyprint = print



# %% Class
@dataclass(slots=True, kw_only=True)
class Print() :
    f'''
    This function overrides python built in print function to add functionnalities.

    Call
    ----
    >>> from corelp import print
    >>> mystring = "Hello *world*!\nThis is 1 print **example**"
    ...
    >>> print(mystring)

    Muting
    ------
    verbose : bool
        True to do prints, False to mute all prints
    
    >>> print.verbose = False # Muting
    >>> print(mystring) # Does not print
    >>> print(mystring, verbose=True) # Forces printing even with muting
    >>> print(mystring) # Does not print
    ...
    >>> print.verbose = True # Unmuting
    >>> print(mystring) # Does print
    >>> print(mystring, verbose=False) # Forces no printing even without muting
    >>> print(mystring) # Does print

    Prints
    ------
    pyprint : function
        python built-in print function (to still have access after override).
    richprint : function
        rich library print function.
    print : function
        rich library console print function (for enhancing styles).
    log : function
        rich library console log function (for debugging).

    >>> print.pyprint(mystring) # python print
    >>> print.richprint(mystring) # python print
    >>> print.print(mystring) # rich console print
    >>> print.log(mystring) # rich console log

    Tabulation
    ----------
    ntabs : int
        Number of tabulations.
    nspaces : str
        Number of spaces per tabulation.
    space : str
        String corresponding to one space.
    lasted : float
        Duration of last tab sequence.
    tabulation : property
        Current tabulation.

    >>> print.ptab() # adds tab
    >>> print(mystring) # with one tab
    >>> print.mtab() # removes tab
    >>> print(mystring) # with no tab
    >>> with print.tab() :
    ...     print(mystring) # with one tab, duration of with statement measured in "lasted" attribute
    ... print(mystring) # with no tab
    
    Logging
    -------
    file : Path
        Path to file.

    >>> print.file = "log.txt" # defining log file
    >>> print(mystring) # Also writes into file

    Console
    -------
    console : Console
        Rich library console object to use with printing mode "console".

    >>> print.add_theme({"success" : "green"}) # defining new kind of style
    >>> print(mystring, style="sucess") # Writes in green
    '''

    # Main function
    def __call__(self, *args, verbose=None, ntabs=None, file=None, mode='a', end='\n', **kwargs) :
        # Muting
        verbose = verbose if verbose is not None else self.verbose
        if not verbose :
            return None
        
        # Tabulation
        ntabs = ntabs if ntabs is not None else self.ntabs
        string = self.getstring(*args, end=end)

        # printing action
        self.print(string, **kwargs)

        # Writting to file
        file = file if file is not None else self.file
        if file is not None :
            with open(file, mode) as file :
                file.write(string)



    # MUTING
    verbose = True # True to print



    # PRINT
    @property
    def print(self) :
        return self.console.print
    @property
    def log(self) :
        return self.console.log
    pyprint = pyprint # python print
    richprint = richprint # rich print



    # TABULATIONS

    ntabs : int = 0 # Numbers of tabulations 
    nspaces : int = 5 # Number of spaces per tabulation
    space : str = " " # One space string
    lasted : float = None # duration of last tab sequence [s]

    @property
    def tabulation(self) :
        return int(self.ntabs) * int(self.nspaces) * str(self.space)

    def getstring(self, *args, end="\n") :
        string = self.tabulation
        string = string.join(str(arg) for arg in args)
        string = string.replace('\n', '\n' + self.tabulation)
        string += end
        return string

    def ptab(self) :
        '''
        "plus-tab" : Adds one tabulation
        '''
        self.ntabs += 1

    def mtab(self) :
        '''
        "minus-tab" : Removes one tabulation
        '''
        self.ntabs -= 1
        self.ntabs = max(0, self.ntabs)

    @contextlib.contextmanager
    def tab(self) :
        self.ptab() #entering
        tic = perf_counter()
        try:
            yield #return that gets picked up in the 'as'
        except Exception as e:
            toc = perf_counter()
            self.mtab()
            self.lasted = toc-tic
            self(f'Error, lasted {self.lasted:.3f}s')
            raise e #if error
        else :
            toc = perf_counter()
            self.mtab() #if no error
            self.lasted = toc-tic # duration of last tab
        finally:
            pass #exiting



    # LOGGING

    _file = None
    @property
    def file(self) :
        return self.file
    @file.setter
    def file(self, value) :
        self._file = Path(value)



    # CONSOLE

    theme = {}
    def add_theme(self, dic) :
        self.theme.update(dic)
        self._console = None
    @prop(cache=True)
    def console(self) :
        theme = Theme(self.theme)
        return Console(theme=theme)



# Get instance
print = Print() # Instance to use everywhere


# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)