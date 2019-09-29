#Passing a List as a Parameter
#You can send any data types of parameter to a function (string, number, list, dictionary etc.),and it will be treated as the same data type inside the function.
def my_fun(food):
    for x in food:
        print(x)
Fruits=["apple","orange","banana"]
my_fun(Fruits)#apple orange banana
#Return Values
#To let a function, return a value, use the return statement.
def my_fun2(x):
    return 5*x
print(my_fun2(3))#15
#Keyword Arguments
def my_fun3(child3, child2,child1):
    print(" the youngest child is" + child3)
my_fun3(child2="Rana",child1="Ruba",child3="Deem")# the youngest child isDeem
#Arbitrary Arguments
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments and can access the items accordingly.
def my_fun4(*kids):
    print(" the youngest child is" + kids[2])
my_fun4("Rana","Ruba","Deem")# the youngest child isDeem
#Recursion
#Python also accepts function recursion, which means a defined function can call itself.
def my_fun5(k):
    if k>0:
        result= k+my_fun5(k-1)#factorial
        print(result)
    else:
        result=0
    return result
my_fun5(4)
