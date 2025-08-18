#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : template_date
Description   : template_description
"""



# %% Libraries
from devlp import path
from datetime import datetime
import os
import json



# %% Main function
def main() :
    print('\nRunning add_module :')

    # Ask for script name
    already_exists = True
    while already_exists :
        name = input('     New module name ? >>> ')
        module_path = path.parent / f'libsLP/coreLP/src/corelp/modules/{name}_LP'
        if module_path.exists() :
            print('     This module already exists :/')
        else :
            already_exists = False
    description = input('     what will the module do ? >>> ')
    date = datetime.now().strftime("%Y-%m-%d")

    # Print informations
    print(f'     name : {name}')
    print(f'     description : {description}')
    print(f'     date : {date}')
    os.mkdir(module_path)

    # Write python module
    python_path = path/'libsLP/coreLP/src/corelp/modules/template_module.txt'
    newpython_path = module_path/f'{name}.py'
    with open(python_path, "r") as file :
        string = file.read()
    string = string.replace('template_modulename', name)
    string = string.replace('template_moduledate', date)
    string = string.replace('template_moduledescription', description)
    with open(newpython_path, "w") as file :
        file.write(string)
    with open(module_path / "__init__.py", "w") as file :
        file.write("")
    print('     Module file written [to complete]')

    # Add module to json file
    modjson = {}
    modjson['module'] = f"{name}_LP/{name}"
    modjson['object'] = name
    modjson['description'] = description
    json_path = path.parent / f'libsLP/coreLP/src/corelp/modules.json'
    with open(json_path, "r") as file :
        data = json.load(file)
    data[name] = modjson
    with open(json_path, "w") as file :
        json.dump(data, file)
    print("     Module json updated")

    # End
    print('add_module finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()