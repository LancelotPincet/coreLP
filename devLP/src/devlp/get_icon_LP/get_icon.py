#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author        : Lancelot PINCET
Email         : lancelot.pincet@free.fr
Date          : 2025-08-15
Version       : 0.1.0
Description   : Gets compressed icon string to copy-paste to icon.txt
"""



# %% Libraries
from devlp import path, get_path, _attrs, compress_str
import base64
import tkinter as tk



# %% functions
def chose_from_list(options):
    def on_select(event=None):
        choice.set(listbox.get(listbox.curselection()))
        root.quit()

    root = tk.Tk()
    root.iconbitmap(default=path / '_templates/icon_pythonLP.ico')
    root.title('')
    choice = tk.StringVar()

    listbox = tk.Listbox(root, height=10)
    for item in options:
        listbox.insert(tk.END, item)
    listbox.pack(padx=10, pady=10)

    listbox.bind("<Double-1>", on_select)  # double click to choose
    btn = tk.Button(root, text="Select", command=on_select)
    btn.pack(pady=5)

    root.mainloop()
    root.destroy()
    return choice.get()



# %% Main function
def main() :
    print('\nRunning get_icon :')

    # Get icon file
    icon_file = get_path(title='Select icon to compress', extension=".ico")
    print(f'     file : {icon_file}')

    # Get string
    with open(icon_file, "rb") as img:
        # Read the binary data and encode it as a base64 string
        string = base64.b64encode(img.read()).decode('utf-8')
    string = compress_str(string)
    print("     file compressed")

    # Get module list
    mod = chose_from_list(_attrs)
    icon_path = path / f"src/devlp/{mod}_LP/icon.txt"
    with open(icon_path, "w") as file :
        file.write(string)
    print(f"     written string into {mod} icon")

    # End
    print('get_icon finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()