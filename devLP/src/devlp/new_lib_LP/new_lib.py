#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-09-01
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Creates a new library
"""



# %% Libraries
from devlp import path
import subprocess
from datetime import datetime
import toml
import json
import os
import shutil
import requests



# %% Main function
def main() :
    print('\nRunning new_lib :')
    template_path = path / '_template'

    # Ask informations
    already_exists = True
    while already_exists :
        name = input('     New library name ? >>> ')
        lib_path = path.parent / f'libsLP/{name}'
        if lib_path.exists() :
            print('     This library already exists locally :/')
        elif requests.get(f"https://pypi.org/pypi/{name}/json").status_code == 200 :
            print('     This library already exists in PyPI :/')
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
    readme_path = template_path / 'lib_readme.md'
    newreadme_path = lib_path/'README.md'
    string = readme_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    string = string.replace('template_description', description)
    newreadme_path.write_text(string)
    print('     Readme file written [to complete]')

    # Filling Pyproject file
    proj_path = lib_path / 'pyproject.toml'
    with open(proj_path, "r") as file :
        data = toml.load(file)
    data['project']['description'] = description
    with open(proj_path, "w") as file :
        toml.dump(data, file)
    print('     Pyproject file filled')

    # Add license
    license_path = path.parent/'LICENSE'
    newlicense_path = lib_path/'LICENSE'
    shutil.copy(license_path, newlicense_path)
    print('     License was added')

    # Add gitignore file
    ignore_path = path.parent / '.gitignore'
    newignore_path = lib_path / ".gitignore"
    shutil.copy(ignore_path, newignore_path)
    print('     Gitignore was added')
    
    # Add dev folder
    dev_path = lib_path / '.dev'
    os.mkdir(dev_path)
    print('     dev folder created')

    # Adding dependencies
    #subprocess.run(["uv", "add", "coreLP"], cwd=lib_path, check=True, stdout=subprocess.PIPE)
    subprocess.run(["uv", "add", "pytest"], cwd=lib_path, check=True, stdout=subprocess.PIPE)
    subprocess.run(["uv", "add", "sphinx"], cwd=lib_path, check=True, stdout=subprocess.PIPE)
    subprocess.run(["uv", "add", "sphinx-rtd-theme"], cwd=lib_path, check=True, stdout=subprocess.PIPE)
    subprocess.run(["uv", "add", "toml"], cwd=lib_path, check=True, stdout=subprocess.PIPE)

    pyadddependency_path = template_path / "lib_pyadddependency.txt"
    newpyadddependency_path = dev_path / "add_dependency.py"
    string = pyadddependency_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newpyadddependency_path.write_text(string)

    batadddependency_path = template_path / "lib_batadddependency.txt"
    newbatadddependency_path = dev_path / "add_dependency.bat"
    string = batadddependency_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newbatadddependency_path.write_text(string)

    print('     uv dependencies added with tools')

    # Adding modules json
    json_path = lib_path / f'src/{name.lower()}/modules.json'
    with open(json_path, "w") as file :
        json.dump({}, file, indent=4, sort_keys=True)
    print('     module json added')

    # Adding init file
    init_path = template_path / 'lib_init.txt'
    newinit_path = lib_path / f'src/{name.lower()}/__init__.py'
    string = init_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    string = string.replace('template_description', description)
    newinit_path.write(string)
    print('     module __init__ added')

    # Add scripts
    scripts_path = lib_path / f'src/{name.lower()}/scripts'
    scriptsinit_path = scripts_path / '__init__.py'
    path/'_templates/lib_pyscript.txt'
    os.mkdir(scripts_path)
    scriptsinit_path.write_text("")

    pyscripts_path = template_path / 'lib_pyscript.txt'
    newpyscripts_path = dev_path / 'add_script.py'
    string = pyscripts_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newpyscripts_path.write_text(string)

    batscripts_path = template_path / 'lib_pbatscript.txt'
    newbatscripts_path = dev_path / 'add_script.bat'
    string = batscripts_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newbatscripts_path.write_text(string)

    print('     Added tools for adding scripts')

    # Add modules
    modules_path = lib_path / f'src/{name.lower()}/modules'
    modulesinit_path = modules_path / '__init__.py'
    os.mkdir(modules_path)
    modulesinit_path.write_text("")

    pymodules_path = template_path / 'lib_pymodule.txt'
    newpymodules_path = dev_path / 'add_module.py'
    string = pymodules_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newpymodules_path.write_text(string)

    batmodules_path = template_path / 'lib_pbatmodule.txt'
    newbatmodules_path = dev_path / 'add_module.bat'
    string = batmodules_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newbatmodules_path.write_text(string)

    print('     Added tools for adding modules')

    # Add tools to push to repo a new version
    pypush_path = template_path / 'lib_pyversion.txt'
    newpypush_path = dev_path / 'upload_newversion.py'
    string = pypush_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newpypush_path.write(string)


    batpush_path = template_path / 'lib_batversion.txt'
    newbatpush_path = dev_path / 'upload_newversion.bat'
    string = batpush_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_date', date)
    newbatpush_path.write(string)

    print('     Added tools for creating new version')

    # Add tools to bump minor and major version
    bumpmajor_path = template_path / 'lib_batmajor.txt'
    newbumpmajor_path = dev_path / 'bump_majorversion.bat'
    bumpminor_path = template_path / 'lib_batminor.txt'
    newbumpminor_path = dev_path / 'bump_minorversion.bat'
    string = bumpmajor_path.read_text()
    newbumpmajor_path.write_text(string)
    string = bumpminor_path.read_text()
    newbumpminor_path.write_text(string)

    print('     Added tools for bumping major and minor versions')

    # Add documentation
    doc_path = lib_path / 'docs'
    docsource_path = doc_path / 'source'
    docbuild_path = doc_path / 'build'
    os.mkdir(doc_path)
    os.mkdir(docsource_path)
    os.mkdir(docbuild_path)

    docconf_path = template_path / 'lib_docconf.txt'
    newdocconf_path = docsource_path / 'conf.py'
    string = docconf_path.read_text()
    string = string.replace('template_name', name)
    string = string.replace('template_lowername', name.lower())
    string = string.replace('template_year', date[:4])
    newdocconf_path.write_text(string)

    

    print('     Added documentations')

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
    print('     Git main push done')
    subprocess.run(["git", "subtree", "push", f"--prefix=libsLP/{name}", name, "main"], cwd=path.parent, check=True, stdout=subprocess.PIPE)
    print('     Git subtree push done')

    # End
    print('new_lib finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()