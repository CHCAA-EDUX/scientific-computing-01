# Modules

**Please read this document before class on February 7**

## Read these websites first!

- [W3schools - Python Modules](https://www.w3schools.com/python/python_modules.asp)
- [LearnPython.org - Modules and Packages](https://www.learnpython.org/en/Modules_and_Packages)

## Python vs R
As you just learned, a module is simply a `.py` file which contains a number of functions and variables that can be imported into other scripts. A package is a collection of modules that fall under the same umbrella. You've already used packages in R with the `library()` function. `library()` loads all the functions from all the modules of the package in question into your environment and allows you to use them. Python is a bit more explicit than R, and requires you to specify where your functions come from. For instance, if you want to use the `os` library to print your current working directory you would do the following:

```py
import os
print(os.getcwd())
```

`import os` does the same as `library(..)` does in R, but when callings functions from the package, we need to specify which package the function came from. While this might initially be a bit annoying, you come to appreciate it when reading others' code (or re-reading your own) - it's much easier to understand where functions come from this way.

If you only need to use a single or a few functions from a package or need to use it multiple times, you can load specific functions in the following way. 
```py
from os import getcwd, listdir
cwd = getcwd()
print(listdir(cwd))
```

## Installing packages
Installing packages in Python is as simple as running the following command from the command line:

```
pip install package_name
```

Multiple packages can be installed at the same time by seperating them with a space. For example, the below code will install both the `numpy`, `pandas`, and `spacy` packages.

```
pip install numpy pandas spacy
```

## Virtual Environments
As packages get updated, some of their functions will change. This means that a package or program might require a specific version of a package to function correctly. To ensure that your program uses the correct versions you should use a _virtual environment_.

A virtual environment is essentially a seperate Python installation which you can install packages to. As a rule of thumb, each project you work on should have its own virtual environment to ensure that everything works correctly. 

The basic way to create a virtual environment is by writing the following in a terminal:

```
python3 -m venv name_of_venv
```
This will create a directory called `name_of_venv` which stores your newly created virtual environment. 

To activate it, run the following in the terminal
```
# For MacOS or Unix (UCloud)
source name_of_venv/bin/activate
# for Windows
name_of_venv\Scripts\activate.bat
```

Your terminal should now display the name of the virtual enviroment to the left of where you're writing. Once the terminal has been activated you can install packages using `pip install`. 

To deactivate the environment, run
```
deactivate
```

**Note on virtual environments on UCloud**
- Virtual environments are not as big a deal on UCloud as they are on your own computer (or on servers that are not ephemeral) as all packages that you install will be gone once you shutdown the app. This, however, means that it's a great strategy to write a `requirements.txt`.

Most packages and projects include a file called `requirements.txt` which indicates which packages (and versions) are required for the package to work [(click here for an example)](https://github.com/centre-for-humanities-computing/DaCy/blob/main/requirements.txt). `requirements.txt` does not only make which packages are required transparent, but also makes it easy to install them. Simply run (remember to activate a virtual environment first):

```
pip install -r requirements.txt
```

## Modules: Best practice
### Type Hints
Type hinting is a way to indicate what type a value should be. It can be extremely helpful to add type hints to your functions, so you can quickly get an overview of exactly what arguments the function expects and what type of value it outputs. See the following example:

```py
def greet(name: str) -> str:
    return f"Hello, {name}"
```
The `name: str` syntax indicates the `name` argument should be of type `str`. The `->` syntax indicates that the `greet()` function will return a string. You can use all the types you learned in the first class as type hints (`tuple, list, int, float, str, dict` etc.).

It is important to note that Python does not check whether the input/matches actually the type that is hinted! If you use a function with type hints your editor will shown them as a guide for you, but it is up to you use the correct argument type. Check [this cheatsheet for more on type hints.](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

### Docstrings
Docstrings are short strings that tell you what a script or a function does. Here's an example:

```py
def happy_anniversary(person_1: str, person_2: str, years: int) -> str:
    """Prints a anniversary greeting and returns it as a string

    Args:
        person_1 (str): Name of person 1.
        person_2 (str): Name of person 2.
        years (int): How many years anniversary it is.

    Returns:
        str: The greeting as a string
    """
    greeting = f"Congratulations on {years} together, {person_1} and {person_2}!"
    print(greeting)
    return greeting
```
Docstrings for functions consists of a small description of what the function does at the top, followed by the arguments the function takes and a brief description of their type and content. Try to make it a habit to make docstrings for the bulk of your functions. 

### Descriptive Variable Names
Be kind to yourself: instead of using `x` or other abbreviations and shorthands as variable names, use descriptive names. You can always press `tab` to autocomplete them in your editor. 
