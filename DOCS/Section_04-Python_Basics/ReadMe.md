# Section 04 | Python Basics #

## What is Python ##


* Python is a Interpreted, High Level and General Purpose programming language.
* Interpreted and compiled are two type of languages. 
    * Compiled languages are like C, Java, Swift & kotlin
    * Compiled code is first converted to a machine code and then run on the actual hardware.
    * Compiled languages have faster execution.
    * Slow test and write cycle.
    * It targets specific OS.
    * Real time performance is important.
* Interpreted languages are like, Ruby, JavaScript Python
    * We write the code and directly run it, which compiles the code in the background.
    * It is generally slow to execute.
    * Faster write and test cycle.
    * Platform Agnostic
    * Diverse language with small learning curve.
* High level language are those which can be written in English type of form and it complied to machine level code.
* Python can create websites, to simple text scrapping projects. It has a diverse use.

## Python Version ##

* There are 2 main version of Python, Known as 
    * Python 2 and 3
* Python 2 is deprecated on Jan 1, 2020
* Python 3 is the latest.
* Some older project still use Python 2.
* Python Uses Semantic Versioning, like 3.8.2
    * 3 is the major number
    * 8 is the minor changed
    * 2 is the patch release.

## How to run Python ##

* We can use the CLI to run a Python Script.
    * `python test.py`
* Interactive Mode, we can just type `python`, and we will enter the interactive mode.
* Online compilers like [Python Anywhere](https://www.pythonanywhere.com/).

## Hello World ##

* create a file called `hello_world.py`.
    * the script name should have `_` to seperate the words, which is called snake casing.
* Just write `print("Hello, World!")` in the file, and same it.
* in the cli, go to the place where the above file is present, and type `python hello_world.py`

## Comments ##

* Comments are just a reminder in the code about what is the code doing.
* we can make a comment by using `#` character.
* the comments are never executed.

## Variables and Duck Typing ##

* Variable are used to store data in application.
* A variable in Python can be defined as easy as shown below.

```python
age = 10
```

* A variable can start with a letter (A-z) or underscore (_).
* In between, a variable name can contain letters, numbers and underscores.
* No Spl Char.
* Variable Names are case sensitive.

* Variable Types
    * Variables are dynamically typed language, in place of staticly typed language.
    * Statically Typed language are, C, C++, Java, etc.
        * You have to define the type of the variable.
        * You cannot change the type of the variable.
    * Dynammically Typed language are, Ruby, Python, JS
        * No need to define the variable types.
        * Duck Type defines the type of the variable.
        * Common variable types are
            * String
            * Integer
            * Float
            * Boolean

## Variables ##

* We can define Python Variable like this

```python
name = 'Mark'           # Stringe
age = 31                # Integer
is_registered = True    # Boolean
```

* The type if automaically assigned in Python.

## Built In Function ##

* Python provides some functionality right out of the box. 
* These functionality is embedded into built-in function.
* [Official Documentation on Function](https://docs.python.org/3.8/library/functions.html)
* 69 functions as of today.
* Some popular functions are :- 
    * `print()` - O/P text from the application.
    * `int()` - converts a value to an integer.
    * `str()` - converts a value to a string.
    * `bool()` - converts a value to a boolean.
    * `min()` `max()` : finds the lowest/highest number in a list.
    * `round()` : round a value to the nearest whole number.

## PEP-8 GuideLines ##

* PEP-8 is guidelines for formatting the code.
* Without the guidelines, it will be difficult to read the code.
* 4 Spaces per Tab.
* Space around operator.
* Snake case for naming variable.
* ALL uppercase for constants.
* Pascal Case for class name.
* [PeP8 Official Doc](https://peps.python.org/pep-0008/)