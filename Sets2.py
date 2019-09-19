#Get the Length of a Set
thisset={"apple","cherry","banana"}
print(len(thisset))#3
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("apple")
print(thisset)#{'cherry', 'banana'}
#If the item to remove does not exist,remove()will raise an error!.
#Remove "banana" by using the discard() method.
thisset.discard("banana")
print(thisset)#{'cherry'}
#If the item to remove does not exist,discard()will NOT raise an error.
#Remove the last item by using the pop() method.
thisset={"apple","cherry","banana"}
x=thisset.pop()
print(x)#cherry
print(thisset)#{'apple', 'banana'}
#Sets are unordered, so when using thepop()method, you will not know which item that gets removed.
#The clear() method empties the set.
thisset.clear()
print(thisset)#set()
#The del keyword will delete the set completely.
thisset={"apple","cherry","banana"}
del thisset
#print(thisset)#NameError: name 'thisset' is not defined
#It is also possible to use the set() constructor to make a set.
thisset=set(("apple","banana","cherry"))
print(thisset)#{'apple', 'cherry', 'banana'}
