#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-09-02
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : coreLP
# Module        : Path

"""
This function is a wrapper around the pathlib.Path and returns a compatible Path with a windows path copied inside Linux (for WSL)
"""



# %% Libraries
from pathlib import Path as PathlibPath
import os



# %% Detect if running inside WSL
def _is_linux() -> bool:
    """True if linux."""
    if os.name == "posix":
        return True
    if os.name == "nt":
        return False
    raise ValueError(f"Unknown os.name: {os.name}")

def _is_wsl() -> bool:
    """True if running inside WSL."""
    if not _is_linux():
        return False
    try:
        with open("/proc/version", "r") as f:
            return "microsoft" in f.read().lower()
    except FileNotFoundError:
        return False

IS_LINUX = _is_linux()
IS_WSL = _is_wsl()


# %% Function
def Path(path, *args, **kwargs) :
    '''
    This function is a wrapper around the pathlib.Path and returns a compatible Path (Windows, Linux, WSL)
    
    Parameters
    ----------
    path : str of pathlib.Path
        path string to convert to Path.

    Returns
    -------
    path : pathlib.Path
        compatible Path.

    Examples
    --------
    >>> Path("C:\\Users\\Name\\Documents")
    PosixPath('/mnt/c/Users/Name/Documents')   # under WSL
    >>> Path("/home/user/project")
    PosixPath('/home/user/project')            # under Linux
    >>> Path("C:\\Users\\Name\\Documents")
    WindowsPath('C:/Users/Name/Documents')     # under Windows
    '''

    # Conversion in string
    pathstring = str(path).replace("\\", "/")

    # Windows case
    if not IS_LINUX:
        if ":" in pathstring: # from windows
            return PathlibPath(pathstring, *args, **kwargs)
        if pathstring.startswith("/mnt/"): # Windows WSL path
            pathstring = pathstring.replace("/mnt/", "")
            pathstring = pathstring[0].upper() + ":" + pathstring[1:]
            return PathlibPath(pathstring, *args, **kwargs)
        else : # from WSL
            pathstring = f"//wsl.localhost/Ubuntu/{pathstring}"
            return PathlibPath(pathstring, *args, **kwargs)

    # If not in WSL → no touching
    if not IS_WSL:
        return PathlibPath(pathstring, *args, **kwargs)

    # WSL windows path
    if pathstring.startswith("//wsl.localhost/Ubuntu"):
        pathstring = pathstring.replace("//wsl.localhost/Ubuntu", "")
        return PathlibPath(pathstring, *args, **kwargs)

    # Detection of UNC Windows paths (\\server\share)
    if pathstring.startswith("//"):
        unc_path = pathstring.lstrip("/")
        pathstring = f"/mnt/unc/{unc_path}"
        return PathlibPath(pathstring, *args, **kwargs)

    # Conversion of paths Windows with disk (C:/Users/...)
    if ":" in pathstring:
        drive, rest = pathstring.split(":", 1)
        pathstring = f"/mnt/{drive.lower()}{rest}"
        return PathlibPath(pathstring, *args, **kwargs)

    # Else → already a native/relative Linux path
    return PathlibPath(pathstring, *args, **kwargs)
    


# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)