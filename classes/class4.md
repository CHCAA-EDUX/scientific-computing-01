# In class - Lesson 4 #
# Exercises #
In groups of 2-3, make the following exercises.
Explain to each other why you answer as you do.

For the design and programming exercises, all group members should be drawing and programming --> learning by doing! You do not learn programming by seeing other people type into a terminal!

## Object Oriented Design ##

0. Decide on a “is a”-relationship you want to work with.
1. Design several classes – at least two subclasses and one superclass.
2. Identify the attributes and methods. Which ones belong in the superclass? And which in the subclass?
3. Create a UML diagram to visualize your classes.

Tip: Keep it simple!

## Conceptuals ##
0. What is the difference between a class and an object?
1. What is the difference between a method and a function?
2. What with wrong in the following code:

```py
class Vehicle():
    def move(self):
    	print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self):
        self.fuel_tank_level = 0.5

    def fill_tank():
        self.fuel_tank_level = 1
        print("Fuel tank is now full")

```
3. What is the conventional entry point where a Python program starts its execution?


## Object Oriented Programming ##

* Implement your OOD from exercise 1.

* Instantiate your subclass (create an object) and show what it can do in an entry point function `main()`.

* Invoke functionality your subclass has inherited from the superclass.

## Implementation

Implement the following UML diagram in Python:

![](https://i.imgur.com/v3AfgwE.png)

## Check your understanding ##

* Draw a UML diagram corresponding to the following code.

* Create an object of the PrincipalInvestigator class.

* Give a bonus and set the mood to Happy =True

``` py
class Person():
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def getSurname(self):
        return self.name.split()[-1]

    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age

    def setMood(self, happy=False):
        if happy:
            self.mood = 'happy'
            print(f"{self.name.split()[0]}: I have no regrets over past mistakes")
        else:
            self.mood = 'angry'
            print(f'{self.name.split()[0]}: #@*%')


class Researcher(Person):
    def __init__(self, pay=10, areas=['research'],  **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.pay = pay
        self.areas = areas

    def giveBonus(self, bonus):
        self.pay = self.pay + bonus

class PrincipalInvestigator(Researcher):
    def giveBonus(self, bonus, painandsuffering=.10):
        Researcher.giveBonus(self, bonus * (1 + painandsuffering))
```


## Object Oriented Design + Programming (continued) ##
If you have finished the above exercises, you can expand your design from exercise 1 and implement your additions to your Python program.
