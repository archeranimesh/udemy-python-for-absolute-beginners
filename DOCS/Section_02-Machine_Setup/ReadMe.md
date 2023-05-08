# Section 2 | Machine Setup #
## Introduction to Machine Setup ##

We will learn to 

* Install Python
    - On Windows & macOS
    - Install Python 3.8
* Install VSCode
    - Code Editor
    - Configure it to work with Python.
    - Key feature 

## Install and Using Python on Windows ##

* [Python Windows Download](https://www.python.org/downloads/windows/)
    - Select the version you want to install.
    - Download the executable for windows.
    - Install the above exe on your windows machine.
    - In the installation windows, kindly select the "Add Python 3.8 to Path" option
    - Verify the installtion by opening command prompt and typing `python --version`
    - You should get a valid version.

## Install and Using Python on macOS ##

* By default Python is installed on macOS. Just check the version of Python by typing this in Ternimal. 
    * `python --version`
    * if the version is greater than 3, then you are good else install the new python version.
* Since a lot of macOS internal may use the pre-installed version, we may need to install a new version using a tool called `pyenv`.
    * `pyenv` can be installed using a package manager called `homebrew`.
* Installing `homebrew`.
    * Go to [brew.sh](https://brew.sh/)
    * There is a command to install it.
        * `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
* Installing `pyenv`
    * Once `homebrew` is installed.
    * give the command to install `pyenv`
        * `brew install pyenv`
    * Initialize `pyenv` once installation is complete by giving the command.
        * `pyenv init`
        * add the instruction into the `~/.zshrc`
        * Once the instruction is added to the `~/.zshrc` file, run `pyenv install 3.8.2` to install Python 3.8.2 version.
        * Instruct `pyenv` to pick the correct version of python
            * `echo 3.8.2 > ~/.pyenv/version`
        * Close the terminal and restart another session, and check the python version.

## Installing VSCode on windows ##

* visit the website [Visual Studio Code](https://code.visualstudio.com/).
* Download the executable.
* Follow the instruction and Visual Studio would be installed.

## Installing VSCode on macOS ##

* visit the website [Visual Studio Code](https://code.visualstudio.com/).
* Download the package.
* Follow the instruction and Visual Studio would be installed.


## Setup VSCode for Python ##

* Once VSCode is installed on the respective operating system.
* Open VSCode and go the Extensions section
* Search for Python extension. 
* Install the extension.

## Creating Project Folder ##

* While learning new language, it is better to create a folder called **workspace** to store all code.
* create folder inside this **workspace** folder for individual learning.

## VSCode OverView ##

* VSCode is a clear text editor. So there is no extra formatting information.
* VSCode sidebar is divided into these 4 main parts
    * Explorer
    * Search
    * Git
    * Debugging
    * Extension
* VSCode enables use to save, edit and debug the sourcecode.

## Common Installation Issues. ##