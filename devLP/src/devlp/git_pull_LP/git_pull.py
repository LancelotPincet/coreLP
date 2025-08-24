#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-09-01
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Pulls all changes from GitHub
"""



# %% Libraries
from devlp import path
import subprocess
import sys



# %% Main function
def main() :
    print('\nRunning git_pull :')

    # Git pull
    print('     Git pull')
    result = subprocess.run(["git", "pull", "origin", "main"], cwd=path.parent, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr, code = result.stdout.strip(), result.stderr.strip(), result.returncode

    # Check if pull failed
    if code != 0:
        print("     pythonLP pull failed... :(")
        print(stderr)
        sys.exit(code)
    
    # Check if already up to date
    if "Already up to date" in stdout or "Already up-to-date" in stdout:
        print("     pythonLP already up to date. :P")
    else:
        print("     pythonLP download succeeded! :D")

    # End
    print('git_pull finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()