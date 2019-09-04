#Tuples
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets ().
Tuples1=("Dana","Reem","ruba")
print(Tuples1)


Tuples2=()
print(Tuples2)


Tuples3=(3,)#shoud be set , if one element
print(Tuples3)


Tuples4=(1,2,3.4,6.2,7)
print(Tuples4)


Tuples5=(1,"Sara",3,"rana","deem")
print(Tuples5)

#Access Tuple items
#You can access tuple items by referring to the index number, inside square brackets [].
Tuples6=(1,"Sara",3,"rana","deem")
print(Tuples6[1])

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.

# Loop Through a Tuple
#You can loop through the tuple items by using a for loop.

Tuples7=(1,"Sara",3,"rana","deem")
for x in Tuples7:
    print(x)

#Add Items
#Note: you cannot add items to it.Once a tuple is created, tuples are unchangeable.
#Remove Item
#Note: Y ou cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, ➢ but you can delete the tuple completely.
del Tuples1
#print(Tuples1)#NameError: name 'Tuples1' is not defined

print(Tuples7[0:2])
