# In Class - Lesson 3

## Exercises

Just like the previous lessons, pair up with a neighbour or two and go through the following exercises. Make sure that all of you code all the exercises! Don't open the hints before trying the exercise yourself. 

0) Create a folder called `class3` to work in during this class. Remember to navigate to it in your terminal.

1) Create a virtual environment called `class3_venv`.

2) Activate the environment and install the `numpy` and `pandas` packages. Keep working in this environment the rest of the class. 

3) Write a script that imports `numpy` under the alias `np` and prints the sum of the following two arrays:

```py
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])
```

<details>
  <summary>Hint</summary>
  
  Look into the [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html) function.
</details>


4) Create a file called `functions.py`. In it, write a function `character_count` that takes a string and counts the number of characters. Create another file, `main.py`. From `main.py`, import `character_count` and apply it to a string.

5) Create a function in `functions.py` called `tokenize` that lowercases a character string and splits it into individual words everytime there is a space. The output should look like the following:

```py
>>> print(tokenize("Hello, my name is Lasse"))
["hello,", "my", "name", "is", "lasse"]
```

6) Create a function called `hit_counter` that takes two lists as input. The function should return how many times an element in `list1` matches an element in `list2`. See below for an example: 

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

7) Make a function called `hit_counter_prop` that returns how large a proportion of the words in `list1` that matches a word in `list2`

```py
>>> list1 = ["hello,", "my", "name", "is", "lasse"]
>>> list2 = ["lasse", "kenneth"]
>>> print(hit_counter_prop(list1, list2))
0.2
```


### Sentiment analysis
You have now created the foundation for a small program that can do _sentiment analysis_, which is the task of assesing the polarity (positive/negative) of a text. Let's turn your code into a working program!


1) Create a folder called `data` in your working directory. Add a file called `text1.txt` in which you paste the content from [this file](https://github.com/CHCAA-EDUX/scientific-computing-01/blob/main/data/text1.txt), and a file called `text2.txt` in which you paste the content from [this file.](https://github.com/CHCAA-EDUX/scientific-computing-01/blob/week3/data/text2.txt) to `data`. Next, create a folder called `src` in your working directory. Create a file called `utils.py` in `src`. Finally, create a file called `sentiment_analysis.py` in your working directory. By now, your folder structure should look something like this: 

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

2) First, move `tokenize`, `hit_counter`, and `hit_counter_prop` to the `utils.py` file. 

3) In `utils.py`, create a function called `get_txt_files` that returns a list of the path to all the files ending in `.txt` in a directory. Import the function in `sentiment_analysis.py` and apply it to the path to your data folder. You should get an output similar to this:


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

4) In `utils.py`, create a function called `read_txt` that takes the path to a `.txt` file as input and returns the text content.

<details>
  <summary>Hint</summary>
  
   Use the `with open()` syntax:
   ```py
   with open('example.txt') as f:
       contents = f.read()
   ``` 
</details>

5) Finally, we need some word lists. Paste the following two variables into `utils.py`

```py
POSITIVE_WORDS = ["best", "love", "great", "joy", "amazing", "amazing"]
NEGATIVE_WORDS = ["sad", "bad", "stupid", "hate", "disappointing", "worst"]
```

> Constants are often named in CAPITAL letters to distinguish them from functions and to signal that they should not be changed.


We are now ready to go!

6) In `sentiment_analysis.py`, import all the functions and variables from `utils.py`.

x) Save the list of files in `data` to a variable using the `get_txt_files` function.

7) Loop over each item in the list and do the following:
  - Read the text.
  - Print the text.
  - Calculate both the positive and the negative score using the two word lists and `hit_counter` or `hit_counter_prop`.
  - Print the results in an intuitive way.
  - (Optional): Save the results to a .csv file.

8) Run your code from the terminal and witness your beautiful creation!

The beauty of making a program like this is that you can simply change the files in the `data` folder, and your program will always work the same. At this point, it would be relatively straightforward to turn the code you have in `sentiment_analysis` into a function that does sentiment analysis of a given text/path/list of either, that you could use for a large variety of projects. 


### Representation af males/females
Let's try to apply the functions we created for a slightly different task: analysing how well-represented males and females are in the first chapter of Harry Potter and the Philosopher's Stone.

1) Create a new script called `gender_representation.py` in the same directory as `sentiment_analysis.py`. Create a folder inside the `data` directory called `gender_data` and create the file `hp_ch1.txt` in which you paste the contents from [this file](https://github.com/CHCAA-EDUX/scientific-computing-01/blob/week3/data/gender_data/hp_ch1.txt). 

2) Make two new word lists: `MALE_WORDS` and `FEMALE_WORDS` which include words that you think are related to each gender (e.g. "he", "him", "she", "her", etc.)

3) Read all the `.txt` files in `gender_data` and analyse the gender representation by writing code in the `gender_representation.py` file. You are free to adapt your functions or create new ones (in `utils.py`) if you want to present the result in a different way or change the analysis. 


### Prime numbers 
Lastly, let's try using the functions to count how many prime numbers there are in a randomly generated list of 10 numbers between 2 and 100. 


1) Create a new script called `prime_analysis.py`. Make a list of all prime numbers between 2 and 100:

```py
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

2) Create a loop that repeats the following process 10 times:
  - Create a list of 10 random numbers between 2 and 100.
  - Count how many of them are primes.
  - Print the result.
  - Save the result.
3) Print the average number of primes over the 10 runs.  


### Extra
There are many ways to improve upon this fairly naive approach. For sentiment analysis, one could score words based on their emotional content (e.g. "content" could be +0.5, whereas "love" could be +2), include more words, improve the tokenizer (remove punctuation?) and so on. Try to come up with a solution that improves upon the sentiment analysis pipeline, and implement it. Out of ideas? Create a function that looks up the word in a dictionary instead of a list, and returns the sum of the values instead of the number of hits. Example below:

```py
>>> SENTIMENT_DICT = {"love": 2, "hate" : -2, "sad" : -1.3, "joy" : 1.5}

>>> sentence = "I just love to be sad"
>>> def dictionary_sentiment(sentence, dict):
        # your code here

>>> print(dictionary_sentiment(sentence, SENTIMENT_DICT))
0.7
```
