#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : print

"""
This function improves python print to give other functionalities.
"""



# %% Libraries

pyprint = print


# %% Class
class Print() :
    '''
    This function improves python print to give other functionalities.
    
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
    pyprint = pyprint

    def __init__(self) :
        pass
    
    def __call__(*args, **kwargs) :
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

        return self.pyprint(*args, **kwargs)

print = Print()

"""

import contextlib
from time import perf_counter

pyprint = print
class prints() :
    verbose = True #True to make prints
    _verbose = True #default verbose value
    file = None #file where to save print log
    mode = 'a' #Mode for log file writting : 'a'=append, 'w'=write
    pyprint = pyprint #printing function from python
    log = [] #last printed string
    do_log = False #True to add strings to self.log list

    _tabulation = 0 #tabulation string
    @property
    def tabulation(self) -> str : #tabulation string
        return self.space*self._tabulation
    @tabulation.setter
    def tabulation(self, value) -> float :
        if isinstance(value,str) :
            value = int(len(value)/self._space)
        self._tabulation = value

    _space = 5 #Spaces per tabulations
    @property
    def space(self) -> str : #space string
        if isinstance(self._space,int) :
            return self._space*' '
        else :
            return self._space
    @space.setter
    def space(self, value) -> float :
        if isinstance(value,str) :
            value = len(value)
        self._space = value

    def __init__(self,verbose:bool=False):
        self.verbose = verbose
        self._verbose = verbose

    def __call__(self,*args:str,verbose:bool=None,**kwargs) -> None :
        '''
        Making prints with tabulations and saves into file

        Parameters
        ----------
        *args : str
            variables to print.
        **kwargs :
            keyword arguments of python print function
        '''

        #Init
        if verbose is not None :
            if not verbose : return None
            elif not prints.verbose : return None
        else :
            if not (self.verbose and prints.verbose) : return None
        string = ''

        #Arguments
        for arg in args :
            string += str(arg)
            string += ' '
        string = string[:-1]

        #Managing multi-lines prints
        split = string.split('\n')
        if len(split) > 1 :
            for value in split:
                self(value,verbose=verbose,**kwargs)
            return None

        #prefix and suffix
        string = self.tabulation + string
        end = '\n'
        if 'end' in kwargs : end = kwargs['end']

        #Printing
        pyprint(string,**kwargs)
        if self.do_log : self.log += [string+end]

        #Saving to file
        if self.file is not None :
            with open(self.file, self.mode, encoding='utf-8') as file :
                if string == '' :
                    file.write(end)
                else :
                    file.write(string+end)

        return None

    #Adding tabulations
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
            self.lasted = toc-tic
        finally:
            pass #exiting
    @classmethod
    def tabulate(cls,num=1):
        if cls.verbose :
            cls._tabulation += num
    def ptab(self): #plus tab
        self.tabulate(+1)
    def mtab(self): #minus tab
        self.tabulate(-1)

    #Muting
    def mute(self) : #mute object
        self.verbose = False
    def unmute(self) : #unmute object
        self.verbose = self._verbose
    @classmethod
    def all_mute(cls) : #mute class
        cls.verbose = False
    @classmethod
    def all_unmute(cls) : #mute class
        cls.verbose = cls._verbose

"""
# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)