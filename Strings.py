#String literals in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello"
print("Hello")
print('Hello')

#Assign String to a Variable
a="Hi"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes.
#You can use three double quotes (""") Or three single quotes (''').

b= """ Hello world
    learn python 
    python is great"""
print(b)

#Strings are Arrays
#Strings in Python are arrays of bytes representing Unicode characters.
#Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
#the first character has the position 0
c="Hello, world!"
print(c[1])
#Substring. Get the characters from position 2 to position 5 (not included)
print(c[2:5])#result: llo
print(c[-1])#get last index result: !
