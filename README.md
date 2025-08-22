# pythonLP

```plaintext
Date          : 2025-09-01
Author        : Lancelot PINCET
GitHub        : https://github.com/LancelotPincet/pythonLP
HTTPS         : https://github.com/LancelotPincet/pythonLP.git
SSH           : git@github.com:LancelotPincet/pythonLP.git
PyPI          : LancelotPincet
```

**Personnal Python code environment of Lancelot PINCET [not public]**

---

## Informations

This repository is a personnal workspace for developpment. If you are not me (Lancelot PINCET), please refer to my public repositories on [GitHub](https://github.com/LancelotPincet/pythonLP) or on [PyPI](https://pypi.org/). If for some reason you find this repository public, please open an isssue.

Here are the follow topics covered in this file :

- [Code sharing informations](#publication)

- [Installation of developpment environment](#installation)

- [Workspace structure definition](#workspace)

- [Description of automation scripts](#devlp-library)

- [Libraries references](#libraries)

- [Scripts references](#scripts)

---

## Publications

In this section we wil cover the code sharing informations :

- [The rights in using my codes with the license](#license)

- [Where to find my public codes](#find-the-codes)

### License

Programs developped here are meant to be at term public and open-source. I chose to protect my intellectual property via an [MIT license](LICENSE). This means everyone can *freely* use my libraries in a personnal, academic or commercial manner, if they **keep my copyright name** at the top of the codes. 

The code can be redistributed, *with or without modifications*, in open or closed projects. However the **MIT license must be conserved**. For example in a commercial closed project, this means the **copyright and license must be visible somewhere**, like in the documentation or credits.

The license also explains that the **code performances are not warrantied**, and you are responsible for how you are using it. For more information on your rights and obligations please refer to [descriptive websites](https://en.wikipedia.org/wiki/MIT_License), or contact author for approvales.

### Find the codes

Public versions of the codes can be found on my public repositories on [GitHub](https://github.com/LancelotPincet/pythonLP) or via [PyPI](https://pypi.org/). Latest developpment versions will be in this repository but are private and will only be shared with coworkers.

---

## Installation

In this section we wil cover how to install the developpment environment :

- [Hardware and Operating System](#operating-system)

- [Package manager](#package-manager)

- [Python project manager](#python-project-manager)

- [Code editor](#code-editor)

- [GitHub configuration](#github-configuration)

- [PyPI configuration](#pypi-configuration)

- [Additionnal softwares](#softwares)

- [Install local pythonLP](#local-pythonlp)

Note that these installation protocoles only apply for the developpment environment. For using the public libraries, please refer to the corresponding *README.md* files

### Operating system

The aim is to program on Windows 11 and Windows 10 with an Nvidia GPU card compatible with *CUDA*. However the codes should be able to run also on Linux and/or on computers without *CUDA*.

### Package manager

For installing softwares on Windows, I am using [Scoop](https://scoop.sh/).

Here is the installation protocole.

**Allow unsigned local scripts:**

In PowerShell opened in **Admin mode**, use command line bellow and answer *Yes*:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Install Scoop:**

In another instance of Powershell opened in **normal mode**, use command line bellow:

```powershell
irm get.scoop.sh | iex
```

You can then change Scoop configuration to create shortcuts in the *Start menu*:  

```powershell
scoop config shortcut true
```

**Add conventionnal buckets:**

Install [Git](https://git-scm.com/) with following command:

```powershell
scoop install git
```

Then you can add conventionnal buckets, typically:

```powershell
scoop bucket add extras
scoop bucket add version
scoop bucket add java
```

Now Scoop should be totally ready and configurated to install the other softwares.

### Python project manager

**pythonLP** uses [uv](https://docs.astral.sh/uv/) from Astral for installation and environment management,
as it is simple and has an all-in-one solution for Python project management.

**Installation is made with Scoop via:**

```powershell
scoop install uv
```

For installing uv using standalone installers or other methods, please refer to their [installation website](https://docs.astral.sh/uv/getting-started/installation/)

**Typicall project initialization and usage are with the following lines:**

```powershell
cd PATH_TO_PROJECT # Go to future project parent path
uv init my_project # Creates project folder with all the files
cd my_project # Go inside the project
uv add lib_name# Add a library by its PyPI name
# ... Add all necessary libraries
uv sync # Will create a virtual environment in the project with dependencies(.venv)
uv run main_script.py # Runs the python script as main, checks dependencies
```

For more informations on how to manage your projects with uv, please refer to their [project guide](https://docs.astral.sh/uv/guides/projects/) and their [project reference page](https://docs.astral.sh/uv/concepts/projects/)

### Code editors

I am mainly using [Cursor](https://cursor.com/?from=home) for programming. It is an editor wrapped around [Visual Studio Code](https://code.visualstudio.com/) with AI agent assistance. However, **pythonLP** is also designed to be easily compatible with [Anaconda's](https://anaconda.org/) tools: *Spyder* and *JupyterLab*.

**Cursor can be installed with [Winget](https://github.com/microsoft/winget-cli) (no Scoop available):** 

```powershell
winget install --id=Anysphere.Cursor -e
```

**pythonLP** folder can than be opened on Cursor via the *pythonLP/pythonLP.code-workspace* file. For now, the other mentioned editors are not really in my daily coding workflow, but can still be used. Be aware that default software can conflict if installing several at the same time.

**Visual Studio Code can be installed with Scoop:**

```powershell
scoop install vscode
```

**Anaconda can be installed with Scoop:**

```powershell
scoop install anaconda3
```

Anaconda folder would then be in the *user>scoop>apps>anaconda3>current* folder, not the basir *user* folder like when installed via the standalone installer.

### GitHub configuration

GitHub can be configured on the computer.

#### SSH key

For automatic connexion to the [LancelotPincet account](https://github.com/LancelotPincet/pythonLP), you should create an SSH key:

```powershell
ssh-keygen -t ed25519 -C "lancelot.pincet@free.fr"
```

Press `Enter` to put the key by default in *~/.ssh/id_ed25519* and press again `Enter`to not put any password.

Then you can print and copy the public key with :

```powershell
cat ~/.ssh/id_ed25519.pub
```

Then go to [GitHub key settings](https://github.com/settings/keys) and add the copied key. Please **leave the .ssh folder in the user folder** (or do a symlink)

#### GitHub CLI

GitHub CLI tool *gh* is used to automate GitHub repository access in command lines.

**You can install with Scoop and authenticate with:**

```powershell
scoop install gh
gh auth login
```

Questions will be asked, answers should be :

1. `GitHub.com`

2. `SSH`

3. `~/.ssh/id_ed25519.pub`

4. `GitHubCLI` (default)

5. `Login with a web browser`

Then login in the browser.

Now GitHub should be configured even for automatic actions.

### PyPI configuration

Libraries in **pythonLP** are designed to be uploaded as open-source tools in the LancelotPincet account in [PyPI](https://pypi.org/). To automate the publishing, you should create a specific token via the [website parameters](https://pypi.org/manage/account/) under *"Add an API token"*.

Copy the token generated and paste it in a file in the user folder under the name *~/LancelotPincet_uv-publish.pypi_token*.

You can do the same protocole on the [TestPyPI website parameters](https://test.pypi.org/manage/account/) and paste it in the file *~/LancelotPincet_uv-publish.testpypi_token*.

Now automated publication using [uv](#python-project-manager) should work fine.

### Additionnal softwares

**pythonLP** has [tools](# automations) to automatically open other softwares often used during coding days. These are not mandatory for the codes to work, but if you want these tools to work to ease the repetitive tasks, you will need the following softwares.

**Nircmd is used to automate user interactions**

```powershell
scoop install nircmd
```

**KeePassXC is used for managing passwords**

```powershell
scoop install keepassxc
```

**Firefox is used to go on internet (work website, music on Youtube, GitHub management, and ChatGPT help)**

```powershell
scoop install firefox
```

**Thunderbird is used to get access to my emails**

```powershell
scoop install thunderbird
```

**Windows Explorer is also used to have easy access and visualize files, typically for the following paths:**

- pythonLP

- libsLP

- .links

- .debug

### Local pythonLP

Once everything is installed, you can now comfortably install the local repository of **pythonLP**.

Open PowerShell and go to directory where you want to save your local copy of the repository:

```powershell
cd PATH_TO_PARENT
```

Then you can clone the repository via *git*:

```powershell
git clone 
```

---

## Workspace

This section describes the **pythonLP workspace**:

- [Structure tree representation](#tree-representation)

- [Description of important folders](#important-folders)

### Tree representation

The workspace can be represented with the following tree-structure :

```plaintext
pythonLP/
├── .debug/                  # Temporary visualization files for debugging (1 subfolder/package module)
├── .git/                    # Git commit history (do not modify by hand)
├── .venv/                   # Python virtual environment generated by uv (do not modify by hand)
├── devLP/                   # The devLP library (for automations only, not accessible by other libs)
│   ├── .icons/              # Icons used in the workspace
│   ├── .lib_links/          # Links to libraries in libsLP automations
│   │   └── <lib_name>/      # One folder per library
│   │       └── *.lnk        # Shortcuts to the library'sindividual automations
│   ├── .links/              # Shortcuts to general automations
│   ├── _template/           # Example text files for automatic file generation
│   ├── src/
│   │   └── devlp/           # devLP library source folder
│   │       ├── __init__.py  # Library initializer
│   │       └── <module>/    # One module per automation
│   │           ├── icon.txt # Compressed icon string information for the module
│   │           ├── *.bat    # Batch file for the module
│   │           └── *.py     # Python source code for the module
│   ├── pyproject.toml       # Project configuration for devLP
│   └── README.md            # Documentation for devLP
│
├── libsLP/                  # Developed libraries
│   └── <library>/           # One folder per library
│
├── scriptsLP/               # Independent script projects
│   └── <script_project>/    # One folder per project
│
├── .gitignore               # Git ignore rules
├── .python-version          # Python version specification
├── LICENSE                  # License file
├── pyproject.toml           # Main project configuration
├── pythonLP.code-workspace  # Workspace configuration
├── README.md                # Project documentation
└── uv.lock                  # Dependency lockfile
```

### Important folders

These are the important folders to understand.

- 

---

## devLP library

This section explains the intricaties behind `devLP` :

- [How to use **devLP**](#use-devlp)

- [What are the important automations](#important-automations)

- [List the other automations](#other-automations)

- [libraries automations](#libraries-automations)

- [scripts automations](#scripts-automations)

### Use devLP

### Important automations

### Other automations

### Libraries automations

### Scripts automations

---

## Libraries

---

## Scripts

---

**Have a wonderful day!**
