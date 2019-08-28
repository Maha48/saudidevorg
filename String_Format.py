#We can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders { } are.
print("Use the format() method to insert numbers into strings.")
#format()
age=10
txt="My name is Meem, and Iam {} "
print(txt.format(age))#output :My name is Meem, and Iam 10 

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders.
bro=11
sister=12
me=10
family="Iam {} my sister {} and my brother {}"
print(family.format(me,sister,bro))#output:Iam 10 my sister 12 and my brother 11

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
bro=11
sister=12
me=10
family="Iam {1} my sister {0} and my brother {2}"
print(family.format(sister,me,bro))#Iam 10 my sister 12 and my brother 11