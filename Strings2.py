#strip()
print("strip() method")
#The strip() method removes any whitespace from the beginning or the end.
a="Hello, world! "#space at the end of the sentence
print(a.strip())#will remove the space at the end of the sentence

#len()
print("len() method")
#The len() method returns the length of a string.
b="Hello, world! "
print(len(b)) #the length of b sentence is :14

#lower()
print("lower() method")
#The lower() method returns the string in lower case.
c="Hello, World!"
print(c.lower()) #strings in lower case: hello, world!

#upper()
print("upper() method")
#The upper() method returns the string in upper case.
d="Hello, World!"
print(d.upper())#strings in upper case:HELLO, WORLD!

#replace()
print("replace() method")
#The replace() method replaces a string with another string.
e="Hello, World!"
print(e.replace('l','o'))#replace each 'l' with 'o' :Heooo, Worod!

#split() 
print("split() method")
#The split() method splits the string into substrings if it finds instances of the separator.
f="Hello, World!"
print(f.split(','))#result: ['Hello', ' World!']