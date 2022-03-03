# In Class - Lesson 3

## Exercises

Just like the previous lessons, pair up with a neighbour or two and go through the following exercises. Make sure that all of you code all the exercises! Don't open the hints before trying the exercise yourself. 

0) Create a folder called `class3` to work in during this class. Remember to navigate to it in your terminal.

1) Create a virtual environment called `class3_venv`.

2) Activate the environment and install the `numpy` and `pandas` packages.

3) Write a script that imports `numpy` under the alias `np` and prints the sum of the following two arrays:

```py
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])
```

<details>
  <summary>Hint</summary>
  
  Look into the [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html) function.
</details>


4) In the file `functions.py`, write a function `character_count` that takes a string and counts the number of characters. Import the function in another file in the same directory and test the function.

x) Create a function called `tokenize` that lowercases a character string and splits it into individual words everytime there is a space. The output should look like the following:

```py
>>> print(tokenize("Hello, my name is Lasse"))
["hello,", "my", "name", "is", "lasse"]
```

x) Create a function called `hit_counter` that takes two lists as input. The function should return how many times an element in `list1` matches an element in `list2`. See below for an example: 

```py
>>> list1 = ["hello,", "my", "name", "is", "lasse"]
>>> list2 = ["lasse", "kenneth"]
>>> print(hit_counter(list1, list2))
1

>>> list3 = ["hello,", "is", "my", "name", "is", "lasse"]
>>> list2 = ["lasse", "is"]
>>> print(hit_counter(list3, list2))
3
```

x) Make a function called `hit_counter_prop` that returns how large a proportion of the words in `list1` that matches a word in `list2`

```py
>>> list1 = ["hello,", "my", "name", "is", "lasse"]
>>> list2 = ["lasse", "kenneth"]
>>> print(hit_counter_prop(list1, list2))
0.2
```


### Sentiment analysis
You have now created the foundation for a small program that can do _sentiment analysis_, which is the task of assesing the polarity (positive/negative) of a text. Let's turn your code into a working program!


1) Create a folder called `data` in your working directory. Add a file called `text1.txt` in which you paste the content from [this file](), and a file called `text2.txt` in which you paste the content from [this file.]() to `data`. Next, create a folder called `src` in your working directory. Create a file called `utils.py` in `src`. Finally, create a file called `sentiment_analysis.py` in your working directory. By now, your folder structure should look something like this:

```
scientific-computing-01
 └───class3
      └── sentiment_analysis.py
      │
      └───data
      │    └──text1.txt
      │    └──text2.txt
      │ 
      └───src
           └──utils.py      
```

> `src`, pronounced as "source" often contains the "source code" of a project. That is, the meat of the program, the functions, classes etc. often live in `src` (or in subdirectories).

We now have a skeleton for our project. Time to add some meat to the `.py` files. 

x) First, move `tokenize`, `hit_counter`, and `hit_counter_prop` to the `utils.py` file. 

x) In `utils.py`, create a function called `get_txt_files` that returns a list of all the files ending in `.txt` in a directory. Import the function in `sentiment_analysis.py` and apply it to the path to your data folder. You should get an output similar to this: 

```py
>>> path_to_data_folder = "/work/scientific-computing-01/class3/data"
>>> get_txt_files(path_to_data_folder)
["/work/scientific-computing-01/class3/data/text1.txt", "/work/scientific-computing-01/class3/data/text2.txt"]
```

<details>
  <summary>Hint</summary>
  
   - If you have problems importing, remember to create a `__init__.py` file in `data`. 
   - Check out the [glob.glob](https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/) method and use the `*.txt` ending.  
</details>

x) In `utils.py`, create a function called `read_txt` that takes the path to a `.txt` file as input and returns the text content.

<details>
  <summary>Hint</summary>
  
   Use the `with open()` syntax:
   ```py
   with open('example.txt') as f:
       contents = f.read()
   ``` 
</details>

x) Finally, we need some word lists. Paste the following two variables into `utils.py`

```py
POSITIVE_WORDS = ["best", "love", "great", "joy", "amazing", "amazing"]
NEGATIVE_WORDS = ["sad", "bad", "stupid", "hate", "disappointing", "worst"]
```

> Constants are often named in CAPITAL letters to distinguish them from functions and to signal that they should be changed.


We are now ready to go!

x) In `sentiment_analysis.py`, import all the functions from `utils.py`

1) get the list of files in `data`
2) loop over each item (path) in the list
3) read the text
4) calculate both the positive and negative score
5) print the results

Realize that you can simply add more files to `data` and your program will magically work on them.


### Winter or summer
Do pretty much the same but find if the text if about winter or summer (or something else..)


This is very naive approach with a limited vocabulary. How might you improve it? 