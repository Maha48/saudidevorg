#A lambda function can take any number of arguments but can only have one expression.
#The expression is executed, and the result is returned.
#A lambda function that adds 10 to the number passed in as an argument and print the result.
x= lambda a :a+1#a =argument : a+1 = return
print(x(5))#6
 

y= lambda a,b :a+b
print(y(2,3))#5

y= lambda a,b,c :a*b*c
print(y(2,3,4))#24