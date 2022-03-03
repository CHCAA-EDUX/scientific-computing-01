## Lecture 5: Projects and iterative development

Introduction:
Projects, iterative development, debugging







# min number of word to satisfy the ratio
min_alpha_token = int(doc._.len * ratio)

n_alpha_tokens = 0
for t in doc:
    if t.is_space:
        continue
    # checks if a non-space token contains a alphabetic character
    if contains_alpha_fn(t.text):
        n_alpha_tokens += 1
        if n_alpha_tokens >= min_alpha_token:
            return True
return False


 -->

Project: Comparing genres or authorship attribution

Two groups A and B

A) Loading and Tokenization
- Read in a text
- Tokenize a string
  - split by white space, remove punctuation
  - Optional: Extend tokenization 1:
    - Instead of removing punctuation make it into their own token i.e. "Hello world!" -> "Hello|world|!"
    - Hint: What you can do here it make it into a stepwise approach first split into tokens then into tokens
  - Optional: Extend tokenization 2:
    - What about words such as isn't or it's? Transform them into the constituent words i.e. "isn't" -> "is|not" (instead of "isn|t" or "isn|'|t")
  - Optional: Extend tokenization 3:
    - Make common expression such as "e.g.", "U.K." into tokens. You can do this either using a list of common expressions or maybe using a smarter approach?
- Tokenize the entire text
- Read in all texts from a folder and tokenizer them save to a dict on the form `{"filename": ["token1" ...]}`


B) Word frequncies and Writing
- Create a function which for a list of numbers counts the occurances of each number
- Generalize the function to deal with both list of numbers and strings, Hint: use a dictionary (this might be trivially simple)
- Optional: Find the 50 most frequent object in the list and sort them (hint: sorted)
- from a Dict:
```
input_dict = {"list 1": [11, 11, 11, 12, 13, 41, "5"], "list 2": ["hello","hello", "I", "am", "5", "years", "old"]}
```
create a dataframe of counts:
```
    list_name   11      12      13      41      "5"     "hello"     "I"     "am"        "years"     "old" 
0     "list 1"   3      1       1        1      1           0        0          0           0           0       
1     "list 2"   0      0       0        0      0           2        1          1           1           1
```

Hint:

    Pandas has the `.from_dict` method:
    ```python
    p = {"list1": {"w1": 2, "w2": 3}, "list2": {"w2": 8, "w4": 19}}
    pd.DataFrame.from_dict(p)
    #     list1  list2
    # w1    2.0    NaN
    # w2    3.0    8.0
    # w4    NaN   19.0
    ```
    Where the inner dictionaries of p can be created using your count function.

    Hint 2: How to deal with the NaN:
    You have a couple of options:

    Use the functions specifically for the task:
    ```
    df.fillna(0)
    ```

    Use the more general `.replace` method:
    ```
    import numpy as np
    df.replace(np.nan, 0)
    ```

    Using masking:
    ```
    # set all cases where the isnan is True to be 0
    df[df.isnan()] = 0
    ```

- Write to a csv file

Hint: pandas dataframes have an method for writing to csv. Take a look at the documentation to find it:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#



<!-- 
should include (if not already presented)

str methods: 
.strip, .split

modules:
os, pandas (creating dataframe, writing to csv, the from_dict method)

Functions:
sorted, using lambda methods


requirements.txt?
 -->

sorted([("test", 1), ("atester", 2)], )