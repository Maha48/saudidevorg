#Integers:
#int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
print("Integers")
x=int(1) 
y=int(2.5) 
z=int("3") 
print(x)#result 1
print(y)#result 2
print(z)#result 3

#Floats:
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
print("Floats")
a=float(1)
b=float(2.5)
c=float("3")
d=float("4.5")
print(a)#result 1.0
print(b)#result 2.5
print(c)#result 3.0
print(d)#result 4.5

#Strings:
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
print("Strings")
e=str(1)
f=str(2.5)
g=str("3")
h=str("s1")
print(e)#result "1"
print("number one"+e)#here we can add number to text after casting integer to string
print(f)#result 2.5
print(g)#result 3
print(h)#result s1
