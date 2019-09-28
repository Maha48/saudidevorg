#Python Conditions and If statements
#These conditions can be used in several ways, most commonly in "if statements" and loops.
a=2
b=3
if b>a:
    print("b is greater than b ")
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the
#code. Other programming languages often use curly brackets for this purpose.
#The elif keyword is pythons way of saying
#"if the previous conditions were not true, then try this condition".
a=2
b=2
if b>a:
    print("b is greater than b ")
elif a == b:
    print("a and b are equal")
#The else keyword catches anything which isn't caught by the preceding conditions.
a=3
b=2
if b>a:
    print("b is greater than b ")
elif a == b:
    print("a and b are equal")
else: 
    print("a is greater")
#If you have only one statement to execute, you can put it on the same line as the if statement.
a=2
b=3
if b>a:print("b is greater than b ")
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
a=3
b=2
print("A") if a>b else print("B")
#One line if else statement, with 3 conditions
print("A") if a>b else print("=")if a==b else print("B")
#The and keyword is a logical operator, and is used to combine conditional statements
a=1
b=2
c=3
if b>a and c>a:
    print("both condition are true")
#The or keyword is a logical operator, and is used to combine conditional statements
if b>a or c>a:
    print("at aleast one  condition is true")
#You can have if statements inside if statements, this is called nested if statements.
x=10
if x>8:
    print("First ")
    if x > 4:
        print(" above 4")
    else:
        print("but not above 4")





