#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-15
Version       : 0.1.0
Description   : Creates a bat file for developpment automation
"""



# %% Libraries
from devlp import path
import os



# %% Main function
def main() :
    print('\nRunning create_batauto :')

    # Get name
    file_exists = True
    while file_exists:
        name = input("Insert name of new automation file >>> ")
        if name == "" :  # if empty
            print("Error : Automation file creation name empty.")
            continue
        folder = path / f'src/devlp/{name}_LP'
        file_exists = folder.exists()
        if file_exists:
            print(f"Error : Folder \"{folder}\" already exists.")
    print(f'     name : {name}')

    # Create folder
    os.mkdir(folder)

    # Get batch file
    bat_path = path / '_templates/batauto_bat.txt'
    newbat_path = path / f'src/devlp/{name}_LP/{name}.bat'
    with open(bat_path, 'r') as file:
        string = file.read()
    string = string.replace('template_name', name)
    with open(newbat_path, 'w', encoding="utf-8") as file :
        file.write(string)
    print(f'     batch file written')

    # Add icon file
    icon_path = folder / 'icon.txt'
    with open(icon_path, 'w', encoding="utf-8") as file:
        file.write("")
    print(f'     icon file written')

    # End
    print('create_batauto finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()