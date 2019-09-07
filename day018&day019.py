List1=["Dalal","Rema","Dana"]
List1.append("Nora")
print(List1)#['Dalal', 'Rema', 'Dana', 'Nora']
print(List1.count("Dalal"))#1
list2=List1.copy()
print(list2)#['Dalal', 'Rema', 'Dana', 'Nora']
list2.pop()
print(list2)#['Dalal', 'Rema', 'Dana']

#second question
tuple=("java","python","swift")
if "python" in tuple:
    print("yes,there is")#yes,there is
