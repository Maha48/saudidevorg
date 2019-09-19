# Check if Key Exists
thisdict={
    "name":"dana",
    "age":1,
    "year":2019,
}
if "name" in thisdict:
    print("yes, there is")
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(thisdict))
#Adding Items
thisdict["color"]="red"
print(thisdict)
#Removing Items
thisdict.pop("age")
print(thisdict)
#The popitem() method removes the last inserted item.
thisdict.popitem()
print(thisdict)
#the del keyword removes the item with the specified key name.
del thisdict['name']
print(thisdict)
#The clear() keyword empties the dictionary.
thisdict.clear()
print(thisdict)