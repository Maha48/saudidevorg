#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a
#reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#there are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict={
    "name":"dana",
    "age":1,
    "year":2019,
}
mydict =thisdict.copy()
print(mydict)
#Another way to make a copy is to use the built-in method dict()
mydict1=dict(thisdict)
print(mydict1)
#A dictionary can also contain many dictionaries, this is called nested dictionaries.
myfamily={
    "child1":{
    "name":"Rana",
    "age":"1"
    },
"child2":{
    "name":"dema",
    "age":2
    },
"child3":{
    "name":"dalal",
    "age":3
    }
}
print(myfamily)
child1={
    "name":"Rana",
    "age":"1"
    }
child2={
    "name":"dema",
    "age":2
}
child3={
    "name":"dalal",
    "age":3
    }
myfamily1={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily1)
#It is also possible to use the dict() constructor to make a new dictionary.
thisdict=dict(name="noor",age="5",year="1999")
print(thisdict)