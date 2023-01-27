# Exercise Variables 1
firstname = 'Mario'

# Exercise Variables 2
age = 25

# Exercise Variables 3
sentence = 'Hello I\'m Mario!'

# Exercise Variables 4
amount = 3.5

# Exercise Variables 5
true1 = True
true2 = True
true3 = True
true_set = {true1, true2, true3}

# Exercise Variables 6
my_first2_Name = 'Mario' # While capitalization and numbers are not illegal in variables, 'my_first_name' or 'my_first_name2' would be better options for this variable name.

# Exercise Variables 7
"""Hi,
my name is
John Doe"""

'python'

# Exercise Variables 8
var1, var2, var3 = "val1", "val2", "val3"
print(var1, var2, var3)

# Exercise Variables 9
a = 12
b = 'Hello'
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# Exercise Variables 10
hello = 'Hello!'
name = 'Jhon Doe'
age = '40'

print(len(hello), len(name), len(age))

# Exercise Variables 11
a = 'hello' #capitalize
a = a.capitalize()
b = 'tom' #uppercase
b = b.upper()
c = 'LAURA' #lowercase
c = c.lower()
question = 'How are you' #change o in e
question = question.replace('o', 'e')
age_question = 'How old are you?' #use the correct method to create a string for each word
age_question = age_question.split(' ')
print(a, b, c, question, age_question)

# Exercise Variables 12
name = 'Mike'
age = 30
hello = f"Hello, {name}. You are {age}"
print(hello)

# Exercise Operators 1
print(False and True) # Should print False

# Exercise Operators 2
print(False or (0 != 0 or True)) # Should print True

# Exercise Operators 3
print(5 % 2)

# Exercise Operators 4
print(not ("testing" == "testing" and "Mario" == "Cool Guy")) # Should print True

# Exercise Operators 5
firstName = "Mario"
lastName = "Rossi"

sentence = firstName + " " + lastName

print(sentence) # Should print "Mario Rossi"

# Exercise Operators 6
brands = ["Adidas", "Nike"]

print("Nike" in brands) # Should print True

# Exercise Operators 7
brands = ["Adidas", "Nike"]

print("Reebok" not in brands) # Should print True

# Exercise Methods 1
print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))

# Exercise Methods 2
num1 = 1.3
num2 = 2.3
num3 = 1j 
num4 = 1.4 
num5 = 1.5
num1 = float(num1)
num2 = int(num2)
num3 = complex(num3)
num4 = round(num4)
num5 = round(num5)
print(num1, num2, num3, num4, num5)
print(type(num1), type(num2), type(num3), type(num4), type(num5))

# Exercise Methods 3
num1 = 1122334455666
num1_str = str(num1)
print(len(num1_str))
num2 = num1_str[2]
num3 = num1_str[2:5]
print(type(num2))
print(type(num3))
string_with_0 = "0" + num1_str
print(string_with_0[:5])
print(string_with_0[5:])
print(string_with_0[-4:-2] + "7")

# Exercise Conditions 1
num1 = 335
num2 = 66

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is not greater than {num2}")

# Exercise Conditions 2
number1 = 66
number2 = 66

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")    
else:
    print(f"{number1} equals to {number2}")

# Exercise Conditions 3
import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")    
else:
    print(f"{number1} equals to {number2}")

# Exercise Conditions 4
import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"{number1}'s absolute value is greater than {number2}'s absolute value")
elif abs(number2) > abs(number1):
    print(f"{number2}'s absolute value is greater than {number1}'s absolute value")    
else:
    print(f"{number1}'s absolute value equals to {number2}'s absolute value")
    