# coreLP

Author : Lancelot PINCET

Email : lancelot.pincet@free.fr

Date : 2025-08-18

**Gathers core functions for python programmation**

1. New to **coreLP**? Check out the [Beginner Guide](#beginner-guide) to get up and running
2. Want a deeper understanding of key concepts in **coreLP**? Dive into the [User Guide](#user-guide) to have a full understanding of the tool
3. Have a specific question? Consult the [Reference Guide](#reference-guide) to have detailed info on the functions

---

## Beginner guide

To help you getting started with **coreLP**, we'll cover a few important topics :
- [What is coreLP](#description)
- [How to install coreLP](#installation)
- [A quick start with coreLP](#quick-start)
- [How to get help](#getting-help)

### Description
todo_description  

### Installation

**coreLP** uses [uv](https://docs.astral.sh/uv/) from Astral for installation and environment management.
As it is simple and has an all-in-one solution, I highly recommend switching your project to uv if you do not use it yet.

#### 1. Install uv
For installation, I recommend using a package manager like `Winget` or `Scoop` on Windows, and `Homebrew` on Linux and macOS.

For using [Winget](https://winstall.app/apps/astral-sh.uv), write in powershell :
```powershell
winget install --id=astral-sh.uv  -e
```

For using [Scoop](https://scoop.sh/#/apps?q=uv), write in powershell :
```powershell
scoop install main/uv
```

For using Homebrew, write in bash :
```bash
brew install uv
```

If you still want to install uv using standalone installers or other methods, please refer to their [installation website](https://docs.astral.sh/uv/getting-started/installation/)

#### 2. Create a project using uv
To create a project with a dependency on **coreLP**, just type in your console by filling ```PATH_TO_PROJECT``` :
```sh
cd PATH_TO_PROJECT
uv init my_project
cd my_project
```

Then just add your project dependency to **coreLP** :
```sh
uv add coreLP
uv sync
```

Now your virtual environment with **coreLP** should appear in your project folder as *.venv*.
For more informations on how to manage your projects with uv, please refer to their [project guide](https://docs.astral.sh/uv/guides/projects/) and their [project reference page](https://docs.astral.sh/uv/concepts/projects/)

#### 3. Run your scripts with uv
Once your project is set, you can run any scripts inside the project folder with **coreLP** dependency using simple command :
```sh
uv run my_script.py
```

For more information on scripts dependencies with uv, please refer to their [script guide](https://docs.astral.sh/uv/guides/scripts/)

### Quick start

To get a first grasp of coreLP, you will need to know a bit of Python. For a refresher, see the [Python tutorial](https://docs.python.org/3/tutorial/)

#### 1. Imports
To import `coreLP`, just use :
```python
import corelp
```

#### 2. Basics
todo_basics

#### 3. Simple example
```python
todo_example
```

### Getting help

If you encounter problems or have questions:
- Read the [User Guide](#user-guide)
- Check the [Reference Guide](#reference-guide)
- Open an issue on the [GitHub repository](https://github.com/LancelotPincet/coreLP)
- Contact author : lancelot.pincet@free.fr

---

## User Guide

In the following, we will cover in-depth explanations, best practices, and more advanced workflows for coreLP :
- [What are the main concepts in coreLP](#concepts)
- [An overview of coreLP features](#features)
- [Realistic example and tutorials using coreLP](#turorials)

### Concepts
todo_concepts

### Features
todo_features

### Tutorials
todo_tutorials

---

### Reference Guide

To finish, we will cover the classes and functions individualy.

Reference list :

