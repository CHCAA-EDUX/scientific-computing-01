# In class - Lesson 1 #

# Exercises #
In groups of 2-3, make the following exercises.
Explain to each other why you answer as you do. For the programming exercises, all group members should be programming --> learning by doing! You do not learn programming by seeing other people type into a terminal!


## Pair programming I ##

Write a program, `hello.py` that says hello and asks for a name.
You should be able to run your program from the terminal.

**Hint!** To get user input, use the following:

```py
name = input()
```

## 0. Conceptuals ##

0.0: What is the suggested naming practice for Python?

0.1: Why is `harry` a valid variable name and 100 invalid?

0.2: What does it mean that we have 0-based indexing in Python?

0.3: Name three data types.



## 1. Check your understanding ##

1.0: What values do the variables `mass` and `age` have after each of the following statements? Test your answer by executing the lines.

```py
1 mass = 47.5
2 age = 122
3 mass = mass * 2.0
4 age = age - 20
```

1.1: Sorting Out References. Python allows you to assign multiple values to multiple variables in one line by separating the variables and values with commas. What does the following program print out?

```py
first, second = 'Harry', 'Potter'
third, fourth = second, first
print(third, fourth)
```

1.2: Concatenating. Strings can be added to other string types. This is known as concatenation. What does the following program print out?
```py
first, second = 'Harry', 'Potter'
full_name = first + second
print(full_name)
```
How can you add space between the names?

1.3: Seeing Data Types. What are the data types of the following variables?

```py
planet = 'Earth'
apples = 5
distance = 10.5
colours = ['red', 'green', 'blue']
```
What does the following evaluate to:

```py
type(planet) == type(apples)
type(distance) == type(float(apples))
type(colours[0]) == type(planet)
```

## 2. Practice questions ##

2.0: Which of the following are operators, and which are values?

```py
*
'hello'
-88.8
-
/
+
5
```

2.1: Which of the following is a variable, and which is a string?
```py
spam
'spam'
```

2.2: What does the variable `age` contain in the following code

```py
age = 20
age + 1
```

2.3: What does the following three expressions evaluate to

```py
'spam' + 'spamspam'
'spam' * 3
'spamspamspam' / 3
```

## 3. Sequence types ##
### Lists ###
```py
# same types
colours = ["green", "red", "blue"]
# different types - name, age, height
user_data = ["mary", 42, 1.65]
# lists can be embedded (yuck)
big_list = [user_data, colours]
```
3.0 What does the following evaluate to? And why?

```py
big_list == user_data + colours
[user_data, colours] == [colours, user_data]
```

3.1: How can you access the string `"blue"` in the `big_list`? How can you access the first letter of the string `"blue"` in the `big_list`?  Remember that Python uses 0-based indexing.

3.2: Sorting lists. What does the following evaluate to? Why?
```py
sorted(colours)
sorted(user_data)
```

3.3: Append `"purple"` to the list `colours`.

3.4 Remove `"blue"` from the list `colours`.

### Tuples ###
3.5  Tuples are essentially identical to lists but with one important difference, namely that tuples are immutable. What happens when the following lines are executed?

```py
fruit = ("banana", "apple", "orange")
fruit.append("pineapple")
fruit.remove("apple")
```

3.6 Sorting tuples.  What does the following evaluate to? Why?
```py
fruit = ("banana", "apple", "orange")
sorted(fruit)
print(type(sorted(colours)))
```

### Dictionaries ###
3.7: What are the keys in the following dictionary? What are the values?
```py
students = {"ida marie": 27, "mary": 35, "john": 45}
```

3.8: Add a key-value pair: `"harry": 17`

3.9: Remove the key-value pair for `john`.

3.10: Identify all keys and values in the following dictionary.
```py
instructors = {"ida marie":
                {"programming languages" : ['python', 'java', 'swift']},
              "lasse":
                {"programming languages" : ['python', 'r', 'julia']},
              "martin":
                {"programming languages" : ['python', 'r', 'sql']}}
```



## 4. Errors ##
4.0: By now you have probably already seen different error messages in the terminal. But don't panic! Error messages is quite informative and can help us correct errors in our program. What is wrong in the following lines:
```py
colours = ['red', 'green', 'blue']
colours[3]
"rain" + 2
sunshine
new_text = "this is a brand new text'
```
4.1: Make some errors in your program in order to get the following errors:
* NameError
* TypeError
* IndexError
* SyntaxError

There exist several other error types in Python .

## Pair programming II ##

Write a program, `fun_to_learn.py` that:
1. Defines a variable, `my_text`, containing the text: `"it is fun to learn programming"`.

<!-- 2. Prints out this variable.

3. Print out the type of `my_text` variable. -->

2. Get the first letter in your string and save in a new variable, `char`.

3. Compare the type of the `char` and `my_text`variables and print out the boolean answer.

4. Slice out the text `fun to learn` from `my_text` and print this out. Remember that Python uses 0-based indexing, rather than 1-based indexing used in R.

5. Format all print statements with f-strings and add explanatory texts.
