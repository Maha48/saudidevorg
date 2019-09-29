#Looping Array Elements
cars=["Ford","Volv","BMW"]
for x in cars:
    print(x)
# Ford
# Volv
# BMW
#You can use the append() method to add an element to an array.
cars.append("Honda")
print(cars)#['Ford', 'Volv', 'BMW', 'Honda']
#Removing Array Elements
#You can use the pop() method to remove an element from the array.
cars.pop(1)
print(cars)#['Ford', 'BMW', 'Honda']
#You can also use the remove() method to remove an element from the array.
cars.remove("BMW")
print(cars)#['Ford', 'Honda']
