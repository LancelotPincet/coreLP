#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-16
Version       : 0.1.0
Description   : Makes a symlink of pythonLP into the user folder
"""



# %% Libraries
from devlp import path
from pathlib import Path
import os



# %% Main function
def main() :
    print('\nRunning make_symlink :')

    target = Path.home() / path.parent.name
    try:
        if target.exists() :
            if target.is_symlink() :
                os.remove(target)
                os.symlink(path.parent, target, target_is_directory=True)
                print('     pythonLP symlink recreated in the user folder')
            else :
                print('     pythonLP symlink cannot be created in user folder, a folder with same name already exist')
        else :
            os.symlink(path.parent, target, target_is_directory=True)
            print('     pythonLP symlink created in the user folder')

    # Admin rights
    except OSError :
        print('     Failed making symlink, you may need admin rights (?)')

    # End
    print('make_symlink finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()