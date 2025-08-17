#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-16
Description   : Clears all outputs from jupyter notebooks (usefull before commiting)
"""



# %% Libraries
from devlp import path
import json
import subprocess



# %% Main function
def main() :
    print('\nRunning clear_notebooks :')

    # List of notebook files
    notebooks = list(path.parent.rglob("*.ipynb"))
    print(f'     found {len(notebooks)} notebooks')

    # Looping on notebooks
    for notebook in notebooks :
        print(f'     - {notebook.stem}: ', end="")
        with open(notebook, encoding="utf-8") as f:
            nb = json.load(f)
        needs_cleaning = False
        for cell in nb.get("cells", []):
            if cell.get("outputs") or cell.get("execution_count") is not None:
                needs_cleaning = True
                break
        if needs_cleaning :
            subprocess.run([
                "jupyter", "nbconvert",
                "--ClearOutputPreprocessor.enabled=True",
                "--inplace", str(notebook)
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print("cleaned")
        else :
            print('ok')

    # End
    print('clear_notebooks finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()