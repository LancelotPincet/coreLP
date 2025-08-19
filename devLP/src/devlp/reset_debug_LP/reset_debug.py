#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-19
Description   : Resets debug folder
"""



# %% Libraries
from devlp import path, create_folder



# %% Main function
def main() :
    print('\nRunning reset_debug :')

    create_folder(path.parent / '.debug', parent_is_dev=False)
    print('     Debug folder created')

    # End
    print('reset_debug finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()