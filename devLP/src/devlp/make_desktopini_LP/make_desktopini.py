#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date          : 2025-09-01
Author        : Lancelot PINCET
GitHub        : https://github.com/LancelotPincet
Description   : Makes the desktop.ini file of the folders to open
"""



# %% Libraries
from devlp import path, _attrs
from pathlib import Path
import ctypes
import os



# %% Main function
def main() :
    print('\nRunning make_desktopini :')

    for attr in _attrs :
        if not attr.startswith('open') :
            continue
        print(f'     - {attr}')
        
        # Get folder path
        batpath = path / f'src/devlp/{attr}_LP/{attr}.bat'
        with open(batpath, "r") as file :
            string = file.read()
        folder = string.split('"')[-2]
        folder = folder.replace("%cd%\\", "")
        folder = folder.replace("%cd%", "")
        folder_path = path.parent / folder
        desktop_path = folder_path / f'desktop.ini'
        icon_path = path / f'.icons/{attr}.ico'

        # Get type of folder
        has_lnk = any(file.suffix.lower() == '.lnk' for file in folder_path.iterdir() if file.is_file())
        folder_type = "Pictures" if has_lnk else "Generic"

        # Removes desktop file
        if desktop_path.exists() :
            os.system(f'attrib -h -s -r "{desktop_path}"')
            os.remove(desktop_path)

        # file

        string = f"""
[.ShellClassInfo]
IconResource={icon_path},0
IconFile={icon_path}
IconIndex=0
FolderType={folder_type}
"""

        # Create or overwrite desktop.ini
        with open(desktop_path, "w") as f:
            f.write(string)

        # Set desktop.ini attributes to hidden (+ system for pythonLP)
        os.system(f'attrib +h +s "{desktop_path}"')
    
        # Set folder as read-only (required for custom icon)
        os.system(f'attrib +r "{folder_path}"')

    # Refresh the folder view   
    ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)

    # End
    print('make_desktopini finished!\n')



2# %% Main function run
if __name__ == "__main__":
    main()