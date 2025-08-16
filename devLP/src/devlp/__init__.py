#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-01
Version       : 0.1.0
Description   : Automation scripts for developpments, should only rely on python stlibs.
"""



# %% imports
import importlib
import os
import shutil
import base64
import zlib
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
path = Path(__file__).absolute().parents[2]



# %% functions

def create_folder(folder) :
    folder = path / folder

    # Erase pre-existing folder
    if folder.exists() :
        def remove_protected(func, directory, info):
            if os.name == "nt":
                os.system(f'attrib -h -s -r "{directory}"')
                if os.path.isdir(directory):
                    shutil.rmtree(directory, onexc=remove_protected)
                else:
                    os.remove(directory)
        shutil.rmtree(folder, onexc=remove_protected)
    
    # Create new folder
    os.mkdir(folder)
    return folder

def get_path(*, title=None, extension=None) :
    root = tk.Tk()
    root.iconbitmap(default=path / '_templates/icon_pythonLP.ico')
    root.withdraw()  # Hide the main Tkinter window

    # Create a file type filter
    if extension is None :
        file_types = [("All files", "*.*")]
    else :
        if extension.startswith('.') :
            extension = extension[1:]
        file_types = [(f"{extension.upper()} files", f"*.{extension}"), ("All files", "*.*")]
    
    # Open the file dialog
    if title is None :
        title = "Select a file"
    file_path = filedialog.askopenfilename(title=title, filetypes=file_types)
    
    return file_path

compress_str = lambda string : base64.b64encode(zlib.compress(base64.b64decode(string))).decode('utf-8')
decompress_str = lambda string : base64.b64encode(zlib.decompress(base64.b64decode(string))).decode('utf-8')



# %% modules lazy imports
_attrs = [
    folder.name[:-3]
    for folder in Path(__file__).absolute().parent.iterdir()
    if folder.is_dir() and folder.name.endswith('_LP')
    ]
_lazy_attrs = {}

def __getattr__(name):
    if name in _lazy_attrs:
        return _lazy_attrs[name]

    for module in _attrs :
        if name == module :
            mod = importlib.import_module(f".{module}_LP.{module}", __name__)
            attr = getattr(mod, "main")
            if attr is None :
                raise AttributeError(f"module {module} has no attribute main")
            _lazy_attrs[name] = attr  # Cache it
            return attr

    raise AttributeError(f"module {__name__} has no attribute {name}")