#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets {}.
thisset={}
print(thisset)#{}
thisset={"apple","cherry","banana"}
print(thisset)#{'cherry', 'apple', 'banana'}
#Sets are unordered, so you cannot be sure in which order the items will appear.
thisset={"apple","apple","cherry","banana",1,1,2}
print(thisset)#{1, 2, 'apple', 'cherry', 'banana'}
#You cannot access items in a set by referring to an index, since sets are unordered the items
#Access Items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
    print(x)#1 2 cherry apple banana
print("banana"in thisset)#True
# Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#Add Items
#To add one item to a set use the add() method.
thisset.add("orange")
print(thisset)#{'orange', 1, 2, 'apple', 'banana', 'cherry'}
#To add more than one item to a set use the update() method.

thisset.update(["orange","berry","mango"])
print(thisset)#{1, 2, 'orange', 'apple', 'mango', 'berry', 'cherry', 'banana'}