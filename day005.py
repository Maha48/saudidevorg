import string
x,y,z= "apple" , "orange" ,"limon"
basket = x + y + z
print(basket)
print(basket.split('e',3))
n = 5
print([basket[i:i+n] for i in range(0, len(basket), n)])
basket = x +" "+ y+" " + z
print(basket)
print(basket.split())
