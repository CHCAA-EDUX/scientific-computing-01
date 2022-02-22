# In Class - Lesson 3

<!-- prøv at load en pakke der ikke er installeret -> error -> gå i terminal -> pip install -> snak om nice med requirements.txt og venvs.. Giver mindre mening på ucloud, mere lokalt 

hvis hvordan man laver og aktiverer et venv på ucloud


best practice med modules: docstrings, type hints, iterative development (små funktioner)
-->
## Exercises

Just like the previous lessons, pair up with a neighbour or two and go through the following exercises. Make sure that all of you code all the exercises!

1) Create a virtual environment called "class3"

2) Activate the environment and install the `numpy`, `pandas`, and `matplotlib` packages.

3) Write a script that imports `numpy` under the alias `np` and prints the sum of the following two arrays:
```py
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])
```

4) In the file `functions.py`, write a function `character_count` that takes a string and counts the number of characters. Import the function in another file and test the function.

5) In `functions.py`, write a functions that takes a path as argument (as a string) and returns all files ending with `.py` in the path as a list. Import it from another file and test it. Add appropriate type hints to your function. Hint: use the `os` package.




1) Working with modules/libraries
- Know what a module is and how to import and use them in Python
- How to install libraries using `pip`
- Be familiar with virtual environments and understand their use

2) Creating a module
- Know how to create re-usable functions
- Best practice when developing re-usable functions/modules (docstrings, type hints, descriptive variable names)



create a module
<!-- import i R -->
modules: os, time, numpy (pandas)
virtual environments (step by step guide)


