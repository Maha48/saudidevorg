#￼￼￼￼￼￼￼￼➢ Why Use Lambda Functions? lambda

#  The power of lambda is better shown when you use them as an anonymous function inside
# another function.
# Say you have a function definition that takes one argument, and that argument will be
# multiplied with an unknown number.
def my_fun(n):
    return lambda a: a*n
double=my_fun(2)
print(double(4))#6

def my_fun2(n):
    return lambda a: a*n
double=my_fun2(3)
print(double(4))#12

def my_fun3(n):
    return lambda a: a*n
x=my_fun3(2)
x=my_fun3(3)
print(x(11))#33
print(x(11))#33
