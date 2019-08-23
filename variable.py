#variables
x=5
y="python"
print(x)
print(y)
#Variables do not need to be declared with any particular type and can even change type after they have been set.
x=4
x="sally"
print(x)
#String variables can be declared either by using single or double quotes.
x="john"
print(x)
#single quotes
x='john'
print(x)
#A variable can have a short name (like x and y) or a more descriptive name (age, car name, total volume).
"""
Rules for Python variables
• A variable name must start with a
letter or the underscore character.
• A variable name cannot start with a number.
• A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
• Variable names are case-sensitive
(age, Age and AGE are three different variables).
"""

#Assign Value to Multiple Variables
x, y, z ="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

#you can assign the same value to multiple variables in one line.
x=y=z="Orange"
print(x)
print(y)
print(z)

#To combine both text and a variable, Python uses the + character.
x="awesome"
print("Python is "+ x)

#You can also use the + character to add a variable to another variable.
x="Python is "
y="great"
print(x+y)

#For numbers, the + character works as a mathematical operator.
x=2
y=5
print(x+y)

#If you try to combine a string and a number, Python will give you an error.for example
# x=5
# y="error"
# print(x+y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
