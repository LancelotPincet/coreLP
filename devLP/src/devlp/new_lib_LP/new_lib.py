#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-16
Description   : Creates a new library
"""



# %% Libraries
from devlp import path
import subprocess
from datetime import datetime
import toml
import json
import os
import shutil



# %% Main function
def main() :
    print('\nRunning new_lib :')

    # Ask informations
    already_exists = True
    while already_exists :
        name = input('     New library name ? >>> ')
        lib_path = path.parent / f'libsLP/{name}'
        if lib_path.exists() :
            print('     This library already exists :/')
        else :
            already_exists = False
    description = input('     what will the library do ? >>> ')
    date = datetime.now().strftime("%Y-%m-%d")

    # Print informations
    print(f'     name : {name}')
    print(f'     description : {description}')
    print(f'     date : {date}')

    # Creating new library folder
    subprocess.run(["uv", "init", "--lib", name], cwd=path.parent / "libsLP", check=True, stdout=subprocess.PIPE)
    print('     uv library initiated')

    # Filling Readme file
    with open(path/'_templates/lib_readme.txt', "r") as file :
        string = file.read()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    string = string.replace('template_description', description)
    with open(lib_path/'README.md', "w") as file :
        file.write(string)
    print('     Readme file written [to complete]')

    # Filling Pyproject file
    with open(lib_path/'pyproject.toml', "r") as file :
        data = toml.load(file)
    data['project']['description'] = description
    with open(lib_path/'pyproject.toml', "w") as file :
        toml.dump(data, file)
    print('     Pyproject file filled')

    # Add license
    shutil.copy(path.parent/'LICENSE', lib_path/'LICENSE')
    print('     License was added')

    # Add gitignore file
    shutil.copy(path.parent / '.gitignore', lib_path / ".gitignore")
    print('     Gitignore was added')
    
    # Adding dependencies
    #subprocess.run(["uv", "add", "pyLP"], cwd=lib_path, check=True, stdout=subprocess.PIPE)
    print('     uv dependencies added')

    # Adding modules json
    with open(lib_path / f'src/{name.lower()}/modules.json', "w") as file :
        json.dump({}, file)
    print('     module json added')

    # Add dev folder
    dev_path = lib_path / '.dev'
    os.mkdir(dev_path)
    print('     dev folder created')

    # Add scripts
    scripts_path = lib_path / f'src/{name.lower()}/scripts'
    os.mkdir(scripts_path)
    shutil.copy(path / '_templates/lib_script.txt', scripts_path / "_template_script.txt")
    with open(scripts_path / '__init__.py', "w") as file :
        file.write("")

    with open(path/'_templates/lib_pyscript.txt', "r") as file :
        string = file.read()
    string = string.replace("template_name", name)
    string = string.replace("template_lowername", name.lower())
    with open(dev_path / 'add_script.py', "w") as file :
        file.write(string)

    with open(path/'_templates/lib_batscript.txt', "r") as file :
        string = file.read()
    string = string.replace("template_name", name)
    string = string.replace("template_lowername", name.lower())
    with open(dev_path / 'add_script.bat', "w") as file :
        file.write(string)

    print('     Added tools for adding scripts')

    # Add modules
    modules_path = lib_path / f'src/{name.lower()}/modules'
    os.mkdir(modules_path)
    shutil.copy(path / '_templates/lib_modules.txt', modules_path / "_template_module.txt")
    with open(modules_path / '__init__.py', "w") as file :
        file.write("")

    with open(path/'_templates/lib_pymodule.txt', "r") as file :
        string = file.read()
    string = string.replace("template_name", name)
    string = string.replace("template_lowername", name.lower())
    with open(dev_path / 'add_module.py', "w") as file :
        file.write(string)

    with open(path/'_templates/lib_batmodule.txt', "r") as file :
        string = file.read()
    string = string.replace("template_name", name)
    string = string.replace("template_lowername", name.lower())
    with open(dev_path / 'add_module.bat', "w") as file :
        file.write(string)

    print('     Added tools for adding modules')

    # Add tools to push to repo a new version
    with open(path/'_templates/lib_batversion.txt', "r") as file :
        string = file.read()
    string = string.replace("template_name", name)
    string = string.replace("template_lowername", name.lower())
    with open(dev_path / 'upload_newversion.bat', "w") as file :
        file.write(string)
    print('Added tools for creating new version')

    # Create a github repo
    subprocess.run(["gh", "repo", "create", name, "--private"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     GitHub repository created')
    subprocess.run(["git", "remote", "add", name, f"git@github.com:LancelotPincet/{name}.git"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git remote added')
    subprocess.run(["git", "add", "."], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git added file')
    subprocess.run(["git", "commit", "-m", f"New library {name} init"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git commit done')
    subprocess.run(["git", "push", "origin", "main"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git push done')
    subprocess.run(["git", "subtree", "push", f"--prefix=libsLP/{name}", name, "main"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git push done')


    # End
    print('new_lib finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()