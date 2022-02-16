# Python Basics 2
**Please read this before class on January 28.**

## Flow Control
Control flow is used to do exactly what the name suggest - control the flow of the program. That is, control flow allows the program to make a decision based on the input, to follow one execution bath instead of another; to repeat; to bypass and so on. 

Coming from R, some of this might seem a bit unusual. Don't worry, it gets to be second nature! We suggest running the code chunks on UCloud to see what exactly they do. Try to write them yourself instead of copy-pasting to get a feel for the syntax. 

### For loops
For loops are one of the most used statements in Python. They allow you to iterate over any *iterable* (such as `lists` or `tuples`) and perform some operation on them.
For loops have the following components:
- the `for` keyword
- a (loop) variable name
- the `in` keyword
- the iterable to loop over
- a `:`
- the `for` clause which is indented in the following lines

Whereas for loops are enclosed by curly brackets `{}`, Python uses indentation to mark the start and end of a for loop (4 spaces or a tab).

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

For loops are especially useful if we need to apply the same operation to a bunch of items. Instead of just printing each element, let's try capitalizing each word and adding to a new list

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

`strings` are iterable, which means you can loop over them to get the individual characters.

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

`if` statements are evaluated if the condition evalutes to `True`
```python
names = ["Ida-Marie", "Kenneth", "Lasse"]
for name in names:
    if name == "Kenneth":
        print(f"Hello, {name})
```

You can include arbitrarily many `if` statements and nest them however you like.

```python
for name in names:
    if name in ["Ida-Marie", "Kenneth"]
        print(f"Hello, {name}")
        if "a" in name
            print("I see your name has an ´a´ in it!")
```

Even though there is an 'a' in Lasse, the `print` statment is not executed as the first condition (`name in ["Ida-Marie", "Kenneth"`) is not `True`.

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


### Continue, Break
Some loops 




## Functions



 ## Exercises

 fizz buzz
 zip