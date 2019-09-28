#The range() Function
for x in range(4):
    print(x)#0123
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6
for x in range(2,6):
    print(x)#2345
print("done")
#the range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter:range(2, 30, 3)
for x in range(2,22,3):
    print(x)#2 5 8 11 14 17 20
#Else in For Loop
for x in range(4):
    print(x)
else:
    print("Finished")#0123 Finished
#Nested Loops
Fruits=["apple","orange","banana"]
Fruits2=["cherry","berry","mint"]
for x in Fruits:
    for y in Fruits2:
        print (x,y)#apple cherry apple berry apple mint orange cherry orange berry orange mint banana cherry banana berry banana mint