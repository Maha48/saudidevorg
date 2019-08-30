#Python Logical Operators
#Logical operators are used to combine conditional statements. return  true or False
#and: return True if both statements are true.
x=3
y=2
print(x>y and y<x)#true
#or : return True if one statement is true.
print(x>y or y==x)#true
#not :return False if result is True.
print(x>y)#true


#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
#is
a=["Dana","Najd"]
b=["Dana","Najd"]
c=a
print(a is b)#false
print(a is c)#true
#is not
print(a is not b)#true
print(a is not c)#false


#Python Membership Operators
#in 
print("Dana"in a)#true
print("dana"in a)#false

#not in
print("Dana" not in a)#false
print("dana" not in a)#true
