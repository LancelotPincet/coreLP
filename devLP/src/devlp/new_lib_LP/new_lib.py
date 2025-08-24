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

    # Function to copy file
    def copy_file(from_path, to_path) :
        string = from_path.read_text()
        string = string.replace('template_name', name)
        string = string.replace('template_lowername', name.lower())
        string = string.replace('template_date', date)
        string = string.replace('template_year', date[:4])
        string = string.replace('template_description', description)
        string = string.replace('template_equals', "="*len(name))
        to_path.write_text(string)
        

    # Filling Readme file
    readme_path = template_path / 'lib_readme.md'
    newreadme_path = lib_path/'README.md'
    copy_file(readme_path, newreadme_path)
    print('     Readme file written [to complete]')

    # Filling Pyproject file
    proj_path = lib_path / 'pyproject.toml'
    with open(proj_path, "r") as file :
        data = toml.load(file)
    data['project']['description'] = description
    data.setdefault("tool.uv", {})["required-environments"] = [
    "sys_platform == 'linux' and platform_machine == 'x86_64'",
    "sys_platform == 'win32' and (platform_machine == 'AMD64' or platform_machine == 'x86_64')",
    ]
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
    copy_file(pyadddependency_path, newpyadddependency_path)

    batadddependency_path = template_path / "lib_batadddependency.txt"
    newbatadddependency_path = dev_path / "add_dependency.bat"
    copy_file(batadddependency_path, newbatadddependency_path)

    print('     uv dependencies added with tools')

    # Adding modules json
    json_path = lib_path / f'src/{name.lower()}/modules.json'
    with open(json_path, "w") as file :
        json.dump({}, file, indent=4, sort_keys=True)
    print('     module json added')

    # Adding init file
    init_path = template_path / 'lib_init.txt'
    newinit_path = lib_path / f'src/{name.lower()}/__init__.py'
    copy_file(init_path, newinit_path)
    print('     module __init__ added')

    # Add scripts
    scripts_path = lib_path / f'src/{name.lower()}/scripts'
    scriptsinit_path = scripts_path / '__init__.py'
    path/'_templates/lib_pyscript.txt'
    os.mkdir(scripts_path)
    scriptsinit_path.write_text("")

    pyscripts_path = template_path / 'lib_pyscript.txt'
    newpyscripts_path = dev_path / 'add_script.py'
    copy_file(pyscripts_path, newpyscripts_path)

    batscripts_path = template_path / 'lib_pbatscript.txt'
    newbatscripts_path = dev_path / 'add_script.bat'
    copy_file(batscripts_path, newbatscripts_path)

    print('     Added tools for adding scripts')

    # Add modules
    modules_path = lib_path / f'src/{name.lower()}/modules'
    modulesinit_path = modules_path / '__init__.py'
    os.mkdir(modules_path)
    modulesinit_path.write_text("")

    pymodules_path = template_path / 'lib_pymodule.txt'
    newpymodules_path = dev_path / 'add_module.py'
    copy_file(pymodules_path, newpymodules_path)

    batmodules_path = template_path / 'lib_pbatmodule.txt'
    newbatmodules_path = dev_path / 'add_module.bat'
    copy_file(batmodules_path, newbatmodules_path)

    print('     Added tools for adding modules')

    # Add tools to push to repo a new version
    pypush_path = template_path / 'lib_pyversion.txt'
    newpypush_path = dev_path / 'upload_newversion.py'
    copy_file(pypush_path, newpypush_path)

    batpush_path = template_path / 'lib_batversion.txt'
    newbatpush_path = dev_path / 'upload_newversion.bat'
    copy_file(batpush_path, newbatpush_path)

    print('     Added tools for creating new version')

    # Add tools to bump minor and major version

    bumpmajor_path = template_path / 'lib_batmajor.txt'
    newbumpmajor_path = dev_path / 'bump_majorversion.bat'
    copy_file(bumpmajor_path, newbumpmajor_path)

    bumpminor_path = template_path / 'lib_batminor.txt'
    newbumpminor_path = dev_path / 'bump_minorversion.bat'
    copy_file(bumpminor_path, newbumpminor_path)

    print('     Added tools for bumping major and minor versions')

    # Add documentation
    doc_path = lib_path / 'docs'
    os.mkdir(doc_path)
    print('     Added documentation folder')

    # Add documentation source
    docsource_path = doc_path / 'source'
    os.mkdir(docsource_path)
    docconf_path = template_path / 'lib_docconf.txt'
    newdocconf_path = docsource_path / 'conf.py'
    copy_file(docconf_path, newdocconf_path)

    docindex_path = template_path / 'lib_docindex.rst'
    newdocindex_path = docsource_path / 'index.rst'
    copy_file(docindex_path, newdocindex_path)

    docbeginner_path = template_path / 'lib_docbeginner.rst'
    newdocbeginner_path = docsource_path / 'beginner_guide.rst'
    copy_file(docbeginner_path, newdocbeginner_path)

    docwhatis_path = template_path / 'lib_docwhatis.rst'
    newdocwhatis_path = docsource_path / 'what_is.rst'
    copy_file(docwhatis_path, newdocwhatis_path)

    docwhatis_path = template_path / 'lib_docwhatis.rst'
    newdocwhatis_path = docsource_path / 'what_is.rst'
    copy_file(docwhatis_path, newdocwhatis_path)

    docinstall_path = template_path / 'lib_docinstall.rst'
    newdocinstall_path = docsource_path / 'install.rst'
    copy_file(docinstall_path, newdocinstall_path)

    docquicky_path = template_path / 'lib_docquicky.rst'
    newdocquicky_path = docsource_path / 'quicky.rst'
    copy_file(docquicky_path, newdocquicky_path)

    docuser_path = template_path / 'lib_docuser.rst'
    newdocuser_path = docsource_path / 'user_guide.rst'
    copy_file(docuser_path, newdocuser_path)

    docconcepts_path = template_path / 'lib_docconcepts.rst'
    newdocconcepts_path = docsource_path / 'concepts.rst'
    copy_file(docconcepts_path, newdocconcepts_path)

    docfeatures_path = template_path / 'lib_docfeatures.rst'
    newdocfeatures_path = docsource_path / 'features.rst'
    copy_file(docfeatures_path, newdocfeatures_path)

    doctutorials_path = template_path / 'lib_doctutorials.rst'
    newdoctutorials_path = docsource_path / 'tutorials.rst'
    copy_file(doctutorials_path, newdoctutorials_path)

    docref_path = template_path / 'lib_docreferences.rst'
    newdocref_path = docsource_path / 'reference_guide.rst'
    copy_file(docref_path, newdocref_path)
 
    docscripts_path = template_path / 'lib_docscripts.rst'
    newdocscripts_path = docsource_path / 'scripts.rst'
    copy_file(docscripts_path, newdocscripts_path)

    docmodules_path = template_path / 'lib_docmodules.rst'
    newdocmodules_path = docsource_path / 'modules.rst'
    copy_file(docmodules_path, newdocmodules_path)

    print('     Added documentations')

    # Add documentation build
    docbuild_path = doc_path / 'build'
    os.mkdir(docbuild_path)

    docmake_path = template_path / 'lib_batdocmake.txt'
    newdocmake_path = docsource_path / 'doc_make.bat'
    copy_file(docmake_path, newdocmake_path)



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