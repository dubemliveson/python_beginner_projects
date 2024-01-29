# character_name = "John"
# character_age = " "
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")

''' character_name = "Tom"
print("He really liked the name ," + character_name)
print("but didn't like being " + character_age + ".") 
'''

# Working with strings, data types and functions
'''phrase: str = "Giraffe Academy"
phrase: str = "LinkedIn"
# 0123
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("k"))
# print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))
print(phrase.replace("LinkedIn", "LinkedOut"))
'''

# Working with Numbers
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

# Working with inputs
# name = input("Enter your name: ")
# print("Hello " + name + "!")

# char1 = input("Enter a character")
# char2 = input("Enter another character")
# result = char1 + char2

'''
num1 = input("Enter a character")
num2 = input("Enter another character")
result2 = float(num1) + float(num2)

print(result2)
'''

'''
color = input("Enter color: ")
plural_name = input("Enter Plural name: ")
celebrity = input("Favorite Celebrity: ")

print("Roses are " + color)
print(plural_name + " are blue")
print("I love " + celebrity)
'''

'''numbers = [0, 1, 2, 3, 4]
names = ["Toby", "Patricia", "Creed", "Live"]
names.extend("numbers")

print(names)
'''


'''def say_hi(name, age):
    print("Hello " + "I'm " + name + " and I am " + age + " years old")


say_hi("Dubem", "2")
say_hi("ayo", "7")'''


'''def cube(num):
    return num*num*num


result = cube(4)
print(result) '''


is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not male but are tall")
else:
    print("You are not a male and not tall")