Fruits=["apple","orange","banana"]
for x in Fruits:
    print(x)#apple orange banana
#The for loop does not require an indexing variable to set beforehand.
#Looping Through a String
for x in"banana":
    print(x)#b a n a n a
#With the break statement we can stop the loop before it has looped through all the items.
Fruits=["apple","orange","banana"]
for x in Fruits:
    print(x)
    if x =="orange":
        break#apple orange

Fruits=["apple","orange","banana"]
for x in Fruits:
    if x =="orange":
        break
    print(x)#apple
#With the continue statement we can stop the current iteration of the loop and continue with the next.
Fruits=["apple","orange","banana"]
for x in Fruits:
    if x =="orange":
        continue
    print(x)#apple banana