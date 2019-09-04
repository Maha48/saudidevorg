#List Methods
#List Length
#To determine how many items a list has, use the len() method.
list1=["Deem","dana","Najd"]
print(len(list1))#3

#Add Items
#To add an item to the end of the list, use the append() method.
list1.append("Nora")
print(list1)#['Deem', 'dana', 'Najd', 'Nora']

# To add an item at the specified index, use the insert() method.
list1.insert(1,"Rana")
print(list1)#['Deem', 'Rana', 'dana', 'Najd', 'Nora']

#Remove Item
#There are several methods to remove items from a list.
#The remove() method removes the specified item
list1.remove("Deem")#if there are more than one Deem just first one removed
print(list1)#['Rana', 'dana', 'Najd', 'Nora']

#The pop() method removes the specified index (or the last item if index is not specified)
list1.pop()
print(list1)#['Rana', 'dana', 'Najd']
list1.pop(0)
print(list1)#['dana', 'Najd']

#The clear() method empties the list
#list1.clear()
#print(list1)#AttributeError: 'list' object has no attribute 'clear'

#Copy list
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a referenceto list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
list2=["Deem","dana","Najd"]
list3=list2.copy()
print(list3)#['Deem', 'dana', 'Najd']

list4=list2
print(list4)#['Deem', 'dana', 'Najd']
list2.pop()
print(list2)#['Deem', 'dana']
print(list4)#['Deem', 'dana']


#Another way to make a copy is to use the built-in method list().
list5=["Nada","dana","Ghada"]
list6=list(list5)
print(list6)#['Nada', 'dana', 'Ghada']

#The list() Constructor
#It is also possible to use the list() constructor to make a new list.
list7=list(("sara","rana","reem"))
print(list7)#['sara', 'rana', 'reem']
list7.reverse()
print(list7)#['reem', 'rana', 'sara']
list7.sort()
print(list7)#['rana', 'reem', 'sara']

