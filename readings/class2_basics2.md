# Python Basics 2
**Please read this document before class on January 28.**

[Optional reading on flow control.](https://automatetheboringstuff.com/2e/chapter2/)

[Optional reading on functions.](https://automatetheboringstuff.com/2e/chapter3/)

## Flow Control
Control flow is used to do exactly what the name suggest - control the flow of the program. That is, control flow allows the program to make a decision based on the input, to follow one execution bath instead of another; to repeat; to bypass and so on. 

Coming from R, some of this might seem a bit unusual. Don't worry, it gets to be second nature! We suggest running the code chunks on UCloud to see what exactly they do. Try to write them yourself instead of copy-pasting to get a feel for the syntax. 

### For loops
For loops are one of the most used statements in Python. They allow you to iterate over any *iterable* (such as `lists`, `tuples` or `dicts`) and perform some operation on them.

For loops have the following components:
- the `for` keyword
- a (loop) variable name
- the `in` keyword
- the iterable to loop over
- a `:`
- the `for` clause which is indented in the following lines

Whereas for loops are enclosed by curly brackets, `{}`, in R, Python uses indentation to mark the start and end of a for loop (4 spaces or a tab).

```python
colours = ["red", "green", "blue"]
# for each colour in the list called colours
for colour in colours:
    print(colour)
```

The above code chunk iterates over the items in `colours` sequentially and prints each element. Note that the we can name the elements anything we want (for your own sake, try to keep it meaningful):

```python
# these are all equivalent
for pizza in colours:
    print(pizza)

for i in colours:
    print(i)   
```

Note that we have to be really careful with our indentation, otherwise Python throws an error.
```python
for i in range(10):
print(i)

IndentationError: expected an indented block
```


For loops are especially useful if we need to apply the same operation to a bunch of items. Instead of just printing each element, let's try capitalizing each word and adding to a new list.

```python
# create empty list to store the capitalized colours
shouty_colours = []
for colour in colours:
    upper_string = colour.upper()
    shouty_colours.append(upper_string)

print(shouty_colours)
```

For loops can be nested within for loops to create more complex structures. 

```python
for colour in colours:
    for letter in colour:
        print(letter)
```

`strings` are iterable which means you can loop over them to get the individual characters.

```python
string = "Test"
for letter in string:
    print(letter)
    
> T
> e
> s
> t
```

It can often be handy to keep track of your progress in the loop. Coming from `R` you might think of doing something like this:

```python
i = 0
for colour in colours:
    print(colour, i)
    i += 1
```

Which works fine, but can be error prone (you always forget to increment the counter..). Instead, Python has a built-in function for this, `enumerate`:
```python
for idx, colour in enumerate(shouty_colours):
    print(idx, colour)
```

### While loops
While loops keep iterating until some stopping condition is reached. 
```python
i = 10

while i >= 5:
    print(i)
    i -= 1
    print("still counting...")
```

While loops are not used as frequently as for loops but can be useful if you need to run something until a specific conditions is achieved.


### If, elif, else
#### if
Great, now with loops under our belt we can start to add bifurcations to our program by using `if`, `elif`, and `else` statements.

`if` statements are evaluated if the condition evaluates to `True`
```python
names = ["Ida Marie", "Kenneth", "Lasse"]
for name in names:
    if name == "Kenneth":
        print(f"Hello, {name})
```

Just like with `for` loops, you can include arbitrarily many `if` statements and nest them however you like.

```python
for name in names:
    if name in ["Ida Marie", "Kenneth"]
        print(f"Hello, {name}")
        if "a" in name
            print("I see your name has an ´a´ in it!")
```

Even though there is an 'a' in Lasse, the `print` expression is not executed as the first condition (`name in ["Ida-Marie", "Kenneth"`) is not `True`.

How would you change above expression to also print `I see your name has an 'a' in it` when the name is not "Ida Marie" or "Kenneth"?

#### elif
`elif` behaves very similarly to `if`, but is only evaluated if the preceeding expression is not `True`:

```python
price = 100
if price > 100:
    print("too expensive")
elif price == 100:
    print("just right)
elif price < 100:
    print("too cheap")
```

#### else
`else` is evaluated if all the preceeding expressions are `False``.

```python
if price > 100:
    print("too expensive")
else:
    print("too cheap")
```


### Boolean operators
In the course of flow control we often want to do different things depending on whether some conditions are met. Python has a number of comparison operators for these cases:

| Operator | Meaning |
| - | - |
| `==` | equal to|
| `!=` | not equal to|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

Most of them are self-explanatory, but let's go through some examples of what they evaluate to.

- Integers:
```python
23 == 23
# True
25 == 5
# False
2 != 3
# True
5 != 5 
# False
```

- Strings and floats
```python
"banana" == "banana"
# True
"Apple" == "apple"
# False
False == False
# True
True != False
# True
5.0 == 5
# True
27 == "27"
# False
banana = 25
apple = 13
apple <= 11
# False
banana >= apple
# True
```

Be careful to use `==` when comparing values and not `=`!

Boolean values/expressions (`True`/`False`) can be compared using the Boolean operators `not`, `and`, `or`. They might look a bit daunting and take some getting used to, but they are quite logical once you get the hang of them, and are widely used across all programming languages and programming purposes. 

**Negation, `not`**
| Expression | not `True` | not `False` |
| - | :-: | :-: |
| Evaluates to...  | __F__ | __T__ |

```py
A = True
not A
# False
B = False
not B
# True
not not B
# False
```

**Conjunction, `and`**

For expressions using `and` to be `True` both conditions have to be `True` as shown in the below table.

| Expression | `True` and `True` | `True` and `False` | `False` and `True` | `False` and `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __F__ | __F__ | __F__ |


 
**Disjunction `or`**

For expressions using `or` to be `True`, just one of the conditions need to be `True`.

| Expression | `True` or `True` | `True` or `False` | `False` or `True` | `False` or `False` |
| - | :-: | :-: | :-: | :-: |
| Evaluates to...  | __T__ | __T__ | __T__ | __F__ |




### Continue, Break
To finish the section on flow control, we should mention the two keywords `continue` and `break`. `break` is used to prematurely end a loop (can be both a for or a while loop) and is commonly triggered upon some condition using an `if` statement

```python
num = 0
while num < 5:
    num += 1 
    print(f"num = {num}")
    if num == 3: # condition before exiting a loop
        break
```
What do you think the above code will print before terminating? 
<details>
  <summary>Answer</summary>
  
  ```
  num = 1
  num = 2
  num = 3
  ```
</details>

`continue` skips the succeeding parts of the loop and jumps to the next element in the iterable. As an example, what do you think the below code chunk will print? 

```python
for letter in "Python": 
   if letter == "h":
      continue
   print(f"Current Letter: {letter}")
```

<details>
  <summary>Answer</summary>
  
  ```
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : o
Current Letter : n
  ```
</details>



## Functions
A core principle of programming is that you should not repeat yourself. Functions allow us to define a sequence of operations which we can then call instead of copy-pasting multiple times. Essentially, functions are just a set of actions we group together and give some name. A functions takes the following general form:

```py
def function_name(argument_1, argument_2, argument_n):
    # some code that uses argument_1, 2, n..
    
    # Functions should always end with a return statement
    # this defines the output of the function
    return None
```

To use your function, simply call it with some arguments:
```py
function_name(value_1, value_2, value_n)
```

**Defining a function**
- Start with the keyword `def` (you are about to *def*ine a function).
- Choose a (descriptive!) name for your function.
- Add an opening parenthesis and write names for the arguments your functions needs to take.
    - These are essentially variable names, but are only used inside the function.
    - I.e. they can be entirely different from what you use in the rest of your program.
- Add a closing parenthesis and a :
- Indent your code with 4 spaces or a tab and write whatever code you need to.
- Finish with a `return` statement which defines what the output of your function will be.

If you forget to add a `return` statement, the function will go through all the calculations but will not give you any output. 

### Function example
Let's go through an example function (you will se many more next week). Imagine you are tasked with creating a name list for everyone enrolled at all courses at Aarhus University. The administrator wants all names to title cased and to be sorted alphabetically. One way to do it would be the following:

```py

course1 = ["mary", "Jane", "bob", "zlatan"]
course1_sorted = sorted(course1)
course_1_cased = []
for name in course_1_sorted:
    name_cased = name.title()
    course_1_cased.append(name_cased)

course2 = ["alice", "Bernice"]
...
```

If you are to do this for a lot of courses it very quickly becomes a lot of code. Let's turn the sorting and title casing into a function and call that instead.
```py
def sort_and_title_case(names):
    sorted_names = sorted(names)

    sorted_and_cased_names = []
    for name in sorted_names:
        name_cased = name.title()
        sorted_and_cased_names.append(name_cased)
    return sorted_and_cased_names
```

Now we can simply call the function to get the desired result:
```py
sort_and_title_case(course1)
```

In general, if you find yourself having to do the same thing more than once, it's probably beneficial to turn the thing into a function. 

Notice that I'm using the variable `course1` as input to the function. We defined `sort_and_title_case` to take a single argument, `names`, which we perform some computation on. In this case, `course1` will be translated into the variable `names` inside the function.

There are multiple ways to pass arguments into functions. Above we used the *position* to indicate which variable goes where. Consider this simple function:

```py
def print_2_things(first_thing, second_thing):
    print(first_thing, second_thing)
    return None
```

We can call it in multiple ways (this is just a subset):

```py
first_thing = "banana"
second_thing = "apple"

print_2_things(first_thing, second_thing)
print_2_things(second_thing, first_thing)

print_2_things(first_thing=first_thing, second_thing=second_thing)
print_2_things(first_thing=second_thing, second_thing=first_thing)

print_2_things(second_thing=first_thing, first_thing=second_thing)
print_2_things(second_thing=second_thing, first_thing=first_thing)
```

What do you think each line will print?


<details>
  <summary>Answer</summary>
  
  ```
banana apple
apple banana
banana apple
apple banana
apple banana
banana apple
  ```
</details>


If you want a bit more details on functions, [see this document.](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21/blob/main/lessons/functions.md), or [this one for even more](https://automatetheboringstuff.com/2e/chapter3/).

### Advantages of using functions

I hope you've been convinced by now that functions are pretty neat. Besides the obvious part about not having to copy-paste, functions have a bunch of other advantages:

- Automatic documentation. By collecting related operations into a function it becomes much easier to read the code afterwards. 
- If (when) you find an error in your code, you only have to fix it in one place (the function definition) and it will be fixed everywhere you call the function.
- Your code becomes much cleaner and simpler.
- And last, but not least, it allows you to re-use your code across different projects. More on this next week. 

<!---  not covered: truthy/falsey values (empty lists, empty strings, lists, etc.. --->
