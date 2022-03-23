## Lecture 5: Projects and iterative development

###  Introduction:
- iterative development
- debugging
- Project exercises

## Project: Genre Comparison
For this class, we will work on a larger project in groups. Where larger is still
relatively small, but notably larger than what you have already worked on. 

The project we will be working on is genre comparison. Where we will compare the written
work of Harry Potter with that of the King James bible.

> **Note:** This project is made specifically for it to made it groups, so you can split up the tasks.

## Part A: Loading and Tokenization
In the first part, we will load in the dataset and tokenize it. Tokenization in the act
of splitting a text into their individual token. A token can be thought of as a word,
but can also include e.g. punctuations, subwords and similar.

In this part you should implement the following steps:

- Read in the texts in the folder `data/class5/`

 <br /> 


<details>
  <summary>Hint:</summary>

  Check the reading from class 3.

</details>

<br /> 

- Implement a function which tokenize a string
  - For now you can split by white space and remove punctuations, but if you have the time do check out the optional.

<details>
  <summary>Optional:</summary>

  - Extend tokenization 1:
    - Instead of removing punctuation make it into their own token i.e. "Hello world!" -> "Hello|world|!"
    - Hint: Make it into a stepwise approach first split into tokens then split the punctuation from the tokens.
  - Extend tokenization 2:
    - What about words such as isn't or it's? Transform them into the constituent words i.e. "isn't" -> "is|not" (instead of "isn|t" or "isn|'|t")
  - Extend tokenization 3:
    - Make common expressions such as "e.g.", "U.K." into tokens (i.e. the punctuation should be removed). You can do this either using a list of common expressions or maybe using a smarter approach?

</details>

<br /> 

- Tokenize the two texts
- Read in all texts from a folder and tokenize them save to a dict on the form `{"filename1": ["token1", "token2", ...], "filename2": ...}`

## Part B: Word frequencies
- Create a function which for a list of words counts the occurrences of each word. You should **not** use the `Counter` function, but you can take inspiration from it. Your output should look something like this:
```python
counts = word_counts(["hello","hello", "I", "am", "5", "years", "old"])
print(counts)
{"hello": 2, "I": 1, "am": 1, ...}
```

- Create a dataframe of word counts and the columns are texts. This can be done using Pandas (See example). The output should look like this: 

| Words | Harry Potter | Bible |
| --- | --- | --- |
| Word1 | 2 | 4 | 
| Word2 | 24 | 0 | 
| Word3 | 21 | 512 | 
| ... | ... | ... | 

When using a new package it is always useful to check the [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#) when in need.

<details>
  <summary>Example of using Pandas </summary>

Pandas has the `.from_dict` method:
```python
import pandas as pd
p = {"list1": {"w1": 2, "w2": 3}, "list2": {"w2": 8, "w4": 19}}
pd.DataFrame.from_dict(p)
#     list1  list2
# w1    2.0    NaN
# w2    3.0    8.0
# w4    NaN   19.0
```
Where the inner dictionaries of `p` can be created using your `word_counts` function.

</details>


<details>
  <summary>How to replace NaNs with 0?</summary>

For replacing NAs you have a couple of options:

Use the functions specifically for the task:
```
df.fillna(0)
```

Use the more general `.replace` method:
```
import numpy as np
df.replace(np.nan, 0)
```

Or using masking (similar to what you would see in R):
```
# set all cases where the isnan is True to be 0
df[df.isnan()] = 0
```
</details>



- Write to a csv file (Hint: pandas dataframes have an method for writing to csv. Take a look at the [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#) I am sure you can find it)


## Part C: Improving your code
Go over your code again. Is there anything which can be improved? Starts with steps from the reading, 1) improve readability, 2) add documentation, 3) Generalize the function. By the end the code should be readable by your peers.

## Optional Part D: Analysis
- So now that we have a list of words and their counts which words are the 50 most frequent word? (hint: `sorted`, potentially using the `key` argument)
- What if the differences between the two text: Which words appear in the top 50 in Harry Potter but not in the Bible? 
- What about the rarest word can we see a difference there? 

