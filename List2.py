#List2
list1=["A","B","C","D"]
print(list1[1:3])
#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword.
#check if A in the list
if "A" in list1:
    print("Yes , A is in the list")

#Repeat Item in List
#To repeat an item in a list, use the * operator.
repeat=['Deem']*4
print(repeat)

# + Operator in List
#To add 2 lists or more into one list.
list3=list1+repeat
print(list3)

n1=[1,2,3,4,5]
n2=[1.2,2.1,3.1,4.2]
n3=n1+n2
print(n3)