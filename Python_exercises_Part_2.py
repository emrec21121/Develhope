"""# Iterators - While Loop
i = 1 
while i < 6:
    print("*"*i)
    i = i + 1

# Iterators - For Loop
for i in range(1,6):
    if i%2==0:
        continue
    else:
        print(i*"*")

# Iterators - For Loop2
todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break

# Iterators - For Loop3
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
for item in list1:
    print(item)
for item in tuple1:
    print(item)
for item in set1:
    print(item)
for k,v in dict1.items():
    if v == "land":
        print(f"{k} lives on {v}")
    else:
        continue

# Data Structures

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
print(len(list1), len(tuple1), len(set1), len(dict1))
print(list1[0], tuple1[0])
print(dict1["lion"])
list1[1] = "rabbit"
# tuple1[1] = "rabbit" TypeError: 'tuple' object does not support item assignment
list1 = list1 + ["monkey"]
list1.remove("rabbit")
dict1["fish"] = 0

# Exercise 1 - Functions
def goodbye():
    print("goodbye")

goodbye()

# Exercise 2 - Functions
def goodbye(name):
    print(f"Good bye {name}")

goodbye("Adam")

# Exercise 3 - Functions
import os
user = os.getlogin()
print(user)

# Exercise 4 - Functions 
def greet_family(first_name="John", last_name="Doe"):
    print(f"Hello {first_name} {last_name}!")

greet_family()

family_members = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
for member in family_members:
    greet_family(member[0], member[1])
    
# Exercise 5 - Functions
import random
def random_list_summer(number):
    lst = []
    for i in range(number):
        lst.append(random.randint(-100, 100))
        print(lst)
        sum = 0
        for item in lst:
            sum += item
        print(sum)
random_list_summer(15)

# Exercise 6 - Functions
def fibonacci(number):
    n1 = 0
    n2 = 1
    count = 0
    while count < number:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
fibonacci(5)

# Exercise 7 - Functions
my_list= [*range(5)] 
squares_even = lambda x: x ** 2 if x % 2 == 0 else x
squared_list = list(map(squares_even, my_list))
print(squared_list)
"""
# February 08, 2023

# Classes and Objects 1
class Animal:
    def __init__(self, number_of_legs, does_run):
        self.number_of_legs = number_of_legs
        self.does_run = does_run
    print("Animal object was created")
    def runs(self):
        if self.does_run == True:
            return print("Running started")
        else:
            return print("This animal can't run")

        
panther = Animal(4, True)
panther.runs()

# Classes and Objects 2

class Animal:
    def __init__(self, number_of_legs, does_run):
        self.number_of_legs = number_of_legs
        self.does_run = does_run
    print("Animal object was created")
    def runs(self):
        if self.does_run == True:
            return print("Running started")
        else:
            return print("This animal can't run")

    def count_legs(self):
        print(f'This animal has {self.number_of_legs} legs')
    
    def return_legs(self):
        return (f'This animal has {self.number_of_legs} legs')

cow = Animal(4, True)
cow.count_legs()
print(cow.return_legs())
print(cow.number_of_legs)


# Classes and Objects 3

class Animal:
    def __init__(self, number_of_legs, does_run):
        self.__number_of_legs = number_of_legs
        self.does_run = does_run
    print("Animal object was created")
    def runs(self):
        if self.does_run == True:
            return print("Running started")
        else:
            return print("This animal can't run")
    def count_legs(self):
        print(self.__number_of_legs)
    
    def return_legs(self):
        return self.__number_of_legs

chicken = Animal(2, True)
chicken._Animal__number_of_legs
chicken.count_legs()


# Classes and Objects 4

class Dog(Animal):
    def __init__(self, number_of_legs, does_run, name):
        Animal.__init__(self, number_of_legs, does_run)
        self.name = name
    
    def bark(self):
        print("woof woof")

sparky = Dog(4, True , "Sparky")
print(sparky.name)
sparky.bark()
sparky.count_legs()

# February 15, 2023