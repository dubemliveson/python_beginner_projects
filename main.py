# Concatenating strings together (Day 1)
""" character_name = "John"
character_age = " "
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")


character_name = "Tom"
print("He really liked the name ," + character_name)
print("but didn't like being " + character_age + ".")
"""

# Working with strings, data types and functions (Day 1)
'''phrase: str = "Giraffe Academy"
phrase: str = "LinkedIn"

print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("k"))
# print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))
print(phrase.replace("LinkedIn", "LinkedOut"))
'''

# Working with Numbers (Day 2)
'''
print(2.08997)
print(3 + 4.5)
print(3 + (4.5 + 5))
print(10 % 3)

from math import *
my_num = -5
print(my_num)
print(str(my_num) + " is my favorite number")
print(abs(my_num))
print(pow(4, 2))
print(max(4, 9))
print(round(3.7))
print(floor(3.7))
print(sqrt(36))
'''

# Working with inputs (Day 3)
""" 
name = input("Enter your name: ")
print("Hello " + name + "!")


num1 = input("Enter a number")
num2 = input("Enter another number")
result2 = float(num1) + float(num2)

print(result2)
"""

# Creating a madlibs using input function (Day 3)
'''
color = input("Enter color: ")
plural_name = input("Enter Plural name: ")
celebrity = input("Favorite Celebrity: ")

print("Roses are " + color)
print(plural_name + " are blue")
print("I love " + celebrity)
'''

# Using Functions in Lists (Day 4)
'''
numbers = [0, 1, 2, 3, 4]
names = ["Toby", "Patricia", "Creed", "Live"]
names.extend("numbers")

print(names)

consumables = tuple(["apples", "cherry", "fluid", "cherry"])
index = consumables.index("cherry")
print(consumables)
'''

# Watching Tutorial Videos but couldn't code (Day 5)

# Using functions and Calling functions (Day 6)
'''def say_hi(name, age):
    print("Hello " + "I'm " + name + " and I am " + age + " years old")


say_hi("Dubem", "2")
say_hi("ayo", "7")'''

'''def cube(num):
    return num*num*num


result = cube(4)
print(result) '''

# Using If Statements && Elif Statements (Day 6)
'''
is_male = False)
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not male but are tall")
else:
    print("You are not a male and not tall") '''

# Using If Comparisons to print max number (Day 7)
'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(5000, 300, 4))
'''

# Build a simple calculator using If Statements (Day 7)
"""num1 = float(input("Enter first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator") """

'''
monthConversions = {
    0 : "January",
    "Feb": "February",
    3 : "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
}

print(monthConversions.get(3,"Not a valid key"))
'''

'''
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")'''


