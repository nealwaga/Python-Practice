x = 5
y = 2.5
z = 7j 
print (type(x))
print (type(y))
print (type(z))


# Type Conversion
a = 8
b = 5.5
c = 9j

#convert from int to float:
e = float(a)

#convert from float to int:
f = int(b)

#convert from int to complex:
g = complex(a)

print (e)
print (f)
print (g)

print (type(e))
print (type(f))
print (type(g))


# Random Number
import random

print (random.randrange(1, 100))