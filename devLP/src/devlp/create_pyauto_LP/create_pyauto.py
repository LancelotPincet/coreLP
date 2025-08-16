#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-10
Version       : 0.1.0
Description   : Creates python automation file
"""



# %% Libraries
from devlp import path
from datetime import datetime
import os
import toml



# %% Main function
def main():
    print('\nRunning create_pyauto :')

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

    # Get description
    description = input("Describe what will the file do >>> ")
    if description is None:
        description = ""

    # Get date
    date = datetime.now().strftime("%Y-%m-%d")

    # Create folder
    print(f'     name : {name}')
    print(f'     description : {description}')
    print(f'     date : {date}')
    os.mkdir(folder)

    # Write python file
    py_path = path / f'_templates/pyauto_py.txt'
    newpy_path = folder / f'{name}.py'
    with open(py_path, 'r') as file:
        string = file.read()
    string = string.replace('template_name', name)
    string = string.replace('template_date', date)
    string = string.replace('template_description', description)
    with open(newpy_path, 'w', encoding="utf-8") as file:
        file.write(string)
    print(f'     python file written')

    # Get batch file
    bat_path = path / '_templates/pyauto_bat.txt'
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

    # Add to project
    toml_path = path / 'pyproject.toml'
    with open(toml_path, "r") as f:
        data = toml.load(f)
    data.setdefault("project", {}).setdefault("scripts", {})[name] = f"devlp:{name}"
    with open(toml_path, "w") as f:
        toml.dump(data, f)
    print(f'     {name} was added to devlp')

    # End
    print('create_pyauto finished!\n')



# %% main function run
if __name__ == "__main__":
    main()