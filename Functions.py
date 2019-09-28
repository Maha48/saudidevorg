#A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a result.
#In Python a function is defined using the def keyword
def  my_function():
    print("Hello")
my_function()#Hello
#Parameters
#Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
def Name_Fun(Fname):
    print("Hi"+Fname)
Name_Fun("Dana")#HiDana
#Default Parameter Value
#If we call the function without parameter, it uses the default value.
def defult_Fun(Country="Saudi"):
    print("Iam From "+Country)
defult_Fun("UAE")#Iam From UAE
defult_Fun("Q8")#Iam From Q8
defult_Fun()#Iam From Saudi



