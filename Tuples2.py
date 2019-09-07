#Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword.
fruit=("apple","banana","cherry")
if "apple" in fruit:
    print("yes, there is")#yes, there is
#Repeat Item
#To repeat an item in a tuple, use the * operator.
repeat=("python")*5
print(repeat)#pythonpythonpythonpythonpython
repeat=("python",)*5
print(repeat)#('python', 'python', 'python', 'python', 'python')
#+ Operator in Tuple
add=fruit+repeat
print(add)#('apple', 'banana', 'cherry', 'python', 'python', 'python', 'python', 'python')
x=(3,4,5)
x=x+(1,2,3)
print(x)#(3, 4, 5, 1, 2, 3)
#Tuple Length
#To determine how many items a tuple has, use the len() method.
print(len(x))#6
#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.

fruit=tuple(("apple","banana","cherry"))
print(fruit)#('apple', 'banana', 'cherry')
list1=["sara","dana",1,2]
tuple1=tuple(list1)
print(tuple1)#('sara', 'dana', 1, 2)
#count(),index()
count=(11,2,4,1,4,1,52,12,4)
print(count.count(1))#2
print(count.index(1))#3
