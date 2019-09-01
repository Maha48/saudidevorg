#Lists:
# A list is a collection which is ordered and changeable. Allows duplicate members.
# In Python lists are written with square brackets [].
numbers=[1,2,3,4,5]
print(numbers)#[1, 2, 3, 4, 5]

string=["dana","deem","Najd"]
print(string)#['dana', 'deem', 'Najd']

strnum=["dana","deem","Najd",1,2,3]
print(strnum)#['dana', 'deem', 'Najd', 1, 2, 3]

float1=[1.3,2.4,3.6]
print(float1)#[1.3, 2.4, 3.6]

#Access Items
#You access the list items by referring to the index number.
print(string[1])#deem

#Loop Through a List
#You can loop through the list items by using a for loop.
for i in string:
    print(i) #dana  deem   Najd

for i in float1:
    print(i) #1.3  2.4  3.6

#Change Item Value
#To change the value of a specific item, refer to the index number.
string[1]="Deem"
print(string)#['dana', 'Deem', 'Najd']

#The del keyword removes the specified index.
del string[0]
print(string)#['Deem', 'Najd']


#he del keyword can also delete the list completely.
del float1
print(float1)#NameError: name 'float1' is not defined
