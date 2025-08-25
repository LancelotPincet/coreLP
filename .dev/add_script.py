#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-25
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Create new script for coreLP
"""



# %% Libraries
from devlp import path
from datetime import datetime
import os
import toml
import json



# %% Main function
def main() :
    print('\nRunning add_script :')

    # Ask for script name
    already_exists = True
    while already_exists :
        name = input('     New script name ? >>> ')
        script_path = path.parent / f'libsLP/coreLP/src/corelp/scripts/{name}_LP'
        if script_path.exists() :
            print('     This script already exists :/')
        else :
            already_exists = False
    description = input('     what will the script do ? >>> ')
    date = datetime.now().strftime("%Y-%m-%d")
    with open(path.parent / '.python-version') as file :
        version = file.read()

    # Print informations
    print(f'     name : {name}')
    print(f'     description : {description}')
    print(f'     date : {date}')
    os.mkdir(script_path)

    # Function to copy file
    def copy_file(from_path, to_path) :
        string = from_path.read_text()
        string = string.replace('template_scriptname', name)
        string = string.replace('template_scriptdate', date)
        string = string.replace('template_scriptdescription', description)
        string = string.replace('template_scriptlib', "coreLP")
        string = string.replace('template_scriptlowerlib', "corelp")
        string = string.replace('template_scriptequals', "="*len(name))
        string = string.replace('template_scriptlibequals', "="*len("coreLP"))
        to_path.write_text(string)
        
    # Write python script
    python_path = path / '_templates/lib_script.txt'
    newpython_path = script_path / f'{name}.py'
    copy_file(python_path, newpython_path)
    with open(script_path / "__init__.py", "w") as file :
        file.write("")
    print('     Script file written [to complete]')

    # Add script to project
    toml_path = path.parent / f'libsLP/coreLP/pyproject.toml'
    with open(toml_path, "r") as file:
        data = toml.load(file)
    data.setdefault("project", {}).setdefault("scripts", {})[name] = f"coreLP.scripts.{name}_LP.{name}:{name}"
    with open(toml_path, "w") as file:
        toml.dump(data, file)
    print(f'     Script was added to project')

    # Add script to json file
    scrjson = {}
    scrjson['script'] = f"scripts/{name}_LP/{name}"
    scrjson['object'] = name
    scrjson['description'] = description
    scrjson['date'] = date
    json_path = path.parent / f'libsLP/coreLP/src/corelp/scripts.json'
    with open(json_path, "r") as file :
        data = json.load(file)
    data[name] = scrjson
    with open(json_path, "w") as file :
        json.dump(data, file, indent=4, sort_keys=True)
    print("     Script json updated")

    # Create documentation
    rst_path = path / '_templates/lib_docaddscript.rst'
    newrst_path = path.parent / f'libsLP/coreLP/docs/source/{name}.rst'
    copy_file(rst_path, newrst_path)

    allscripts_path = path.parent / f'libsLP/coreLP/docs/source/scripts.rst'
    with open(allscripts_path, "a") as file :
        file.write(f"    {name}")

    print('     Documentation rst file added')

    # End
    print('add_script finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()