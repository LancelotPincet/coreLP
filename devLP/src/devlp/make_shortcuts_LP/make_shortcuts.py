#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-09-01
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Makes shortcuts for .bat files in devlp
"""



# %% Libraries
from devlp import path, create_folder, decompress_str, lib_list
import base64
import ctypes
import os
from win32com.shell import shell # type: ignore
import win32com.client




# %% Main function
def main() :
    print('\nRunning make_shortcuts :')

    # Get lists of modules
    mod_path = path / "src/devlp"
    bat_list, ico_list = zip(*[
        (mod_path / f"{name.stem[:-3]}_LP/{name.stem[:-3]}.bat",
        mod_path / f"{name.stem[:-3]}_LP/icon.txt")
        for name in mod_path.iterdir()
        if name.is_dir() and str(name).endswith('_LP')
    ])
    
    # Create ico folder and get default icon
    icon_folder = create_folder(".icons")
    lnk_folder = create_folder(".links")
    lib_folder = create_folder(".libs_links")

    # Get default icon string
    with open(path / '_templates/icon_pythonLP.txt', 'r') as file :
        _ico_string = file.read() # default icon

    # Loop on individual modules to create shortcuts
    print('     Making shortcuts :')
    for bat_path, ico_path in zip(bat_list, ico_list) :
        name = bat_path.stem
        icon_path = icon_folder / f'{name}.ico'
        lnk_path = lnk_folder / f'{name}.lnk'
        print(f'     - {name}')

        # Create icon
        with open(ico_path, 'r') as file :
            ico_string = file.read() # for each file
        if len(ico_string) == 0 :
            ico_string = _ico_string
        icon = decompress_str(ico_string)
        with open(str(icon_path), "wb") as icon_file :
            icon_file.write(base64.b64decode(icon.strip()))
        
        # Create shortcut
        Shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = Shell.CreateShortCut(str(lnk_path))
        shortcut.TargetPath = r"C:\Windows\System32\cmd.exe"
        shortcut.Arguments  = f"/c \"{str(bat_path)}\""
        shortcut.WindowStyle = 1 # 1: Normal, 3: Maximized, 7: Minimized
        shortcut.WorkingDirectory = str(path.parent)
        shortcut.IconLocation = str(icon_path)
        shortcut.save()
    
    # Libs shortcuts
    icon_path = path / "_template/icon_pythonLP.ico"
    for lib in lib_list :
        name = lib.name
        print(f'     - {name} library')
        os.mkdir(lib_folder / name)
        folder = lib / ".dev"
        for bat_path in folder.glob("*.bat") :
            lnk_path = lib_folder / f"{name}/{bat_path.stem}.lnk"
                    
            # Create shortcut
            Shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = Shell.CreateShortCut(str(lnk_path))
            shortcut.TargetPath = r"C:\Windows\System32\cmd.exe"
            shortcut.Arguments  = f"/c \"{str(bat_path)}\""
            shortcut.WindowStyle = 1 # 1: Normal, 3: Maximized, 7: Minimized
            shortcut.WorkingDirectory = str(path.parent)
            shortcut.IconLocation = str(icon_path)
            shortcut.save()
    
    # Refresh view
    ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)
    print('     icons refreshed')
    
    # End
    print('make_shortcuts finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()