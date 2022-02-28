# In Class - Lesson 2

# Exercises

Make the following exercises in groups of 2-3 people in the same way as last week. That is, discuss and explain your answers, and everyone should be programming. 


## Control Flow


1) Write a program that prints the numbers 1 to 10 using a for loop. 

2) Write a program that prints the numbers 1 to 10 using a while loop.

3) Consider this code:

```py
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```
Which of the following would be printed if you were to run this code? 
- A
- B
- C
- B and C

4) What are the two values of the Boolean data type? How do you write them?

5) What are the three Boolean operators?

6) What do the following expressions evaluate to?

```py
(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

(True and True) and (True == False)
```

7) Write code that prints "Hello" if 1 is stored in the `spam` variable, prints "Howdy" if 2 is stored in `spam`, and prints "Greetings!" if anything else is stored in spam.

8) What is an infinite loop and what keys can you press if your program is stuck in one (hint: google)?

9) What is the difference between break and continue statements? 

10) Write a loop that counts the number of vowels in a character string.
11) Test it on a few individual words and full sentences.
12) When done, compare your solution to your neighbor's pair. 

<details>
  <summary>Hint</summary>
  
  Use the `range` function.
</details>

 

## Functions
1) Consider the below code chunk. What will we see if we execute it?

```py
def add(a, b):
    print(a + b)

A = add(7, 3)
print(A)
```

2) If the variable `s` refers to a string, then `s[0]` is the string’s first character and `s[-1]` is its last. Write a function called `outer()` that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

```py
print(outer("helium"))
# "hm"
```

3) What is the difference between a function a function call?

4) When does the code in a function execute: during function definiton or function call?

5) Write a function that calculates the average of all the numbers in a list

6) Write a program that prints all the numbers from 0 to 7 except 3 and 6 using a for loop and the `range` function.

7) Write a function that takes a string and prints the number of digits and the number of letters and formats it like below:

```py
digit_letter_counter("1337 Python")
# Letters: 6
# Digits: 4
```


## Fizz Buzz
Fizz buzz is a classic programming assingment (so don't cheat by googling it..) the task is the following:

1) Write a function that takes an integer as input and returns "Fizz" if the integer is divisible by 3, "Buzz" if the integer is divisible by 5, "FizzBuzz" if the integer is divisible by both 3 and 5, or the integer as a string if none of the other conditions are met.

<details>
  <summary>Hint</summary>
  
  Use the modulo `%%` operator.
</details>

 2) Test your function on all numbers from 1 to 50 using a for loop.

 3) Create a function that prints the Fizz Buzz solution to the numbers in a given range and returns the solutions as a list. See below:


 ```py
def fizz_buzz_range_solver(start_number, end_number):
    # do stuff

print(fizz_buzz_range_solver(2, 4))
# "2", 
# "Fizz", 
# "4"
# ["2", "Fizz", "4"]
 ```

 4) Raise an error if the user specifies an illegal range (e.g. (4, 2)).

 5) Make your function return a dictionary with the integer as key and "Fizz"/"Buzz".. as value, e.g. `{2: "2", 3: "Fizz"}`.

