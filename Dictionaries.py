#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets {}, and they have keys and values.
thisdict={
    "name":"dana",
    "age":1,
    "year":2019,
}
print(thisdict)#{'name': 'dana', 'age': 1, 'year': 2019}
#You can access the items of a dictionary by referring to its key name, inside square brackets [].
x=thisdict["age"]
print(x)#1
#There is also a method called get() that will give you the same result.
x=thisdict.get("age")
print(x)#1
#You can change the value of a specific item by referring to its key name.
thisdict["year"]=12
print(thisdict)#{'name': 'dana', 'age': 1, 'year': 12}
for x in thisdict:
    print(x)#name age year
#Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])#dana 1 12
#You can also use the values() function to return values of a dictionary.
for x in thisdict.values():
    print(x)#dana 1 12
print(thisdict.values())#dict_values(['dana', 1, 12])
#Loop through both keys and values, by using the items() function.
for x,y  in thisdict.items():
    print(x,y)#name dana age 1 year 12
print(thisdict.items())#dict_items([('name', 'dana'), ('age', 1), ('year', 12)])

