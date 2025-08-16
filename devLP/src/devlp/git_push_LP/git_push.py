#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-16
Version       : 0.1.0
Description   : Auto-commit all changes and pushes into GitHub
"""



# %% Libraries
from devlp import path
import subprocess
import sys



# %% Main function
def main() :
    print('\nRunning git_push :')

    # Git add
    print('     Git add')
    try :
        subprocess.run(["git", "add", "."], cwd=path.parent, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print('     Git add failed :(')
        sys.exit(1)
    
    # Git commit
    print('     Git commit')
    try :
        subprocess.run(["git", "commit", "-m", "auto-commit"], cwd=path.parent, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print('     No changes to commit :P')
        return 

    # Git commit
    print('     Git push')
    try :
        subprocess.run(["git", "push", "origin", "main"], cwd=path.parent, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print('     Git push failed :(')
        sys.exit(1)
    
    print('     pythonLP upload succeeded :D')

    # End
    print('git_push finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()