# Change Tuple Values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple. Example:
x = ("Pineapple", "Banana", "Strawberry")
y = list(x)
y[1] = "Mango"
x = tuple(y)
print (x)


# Add Items
thistuple = ("Mercedes", "BMW", "Audi", "Range Rover")
y = list(thistuple)
y.append ("Volvo")
thistuple = tuple(y)
print (thistuple)


# Unpacking a Tuple
clubs = ("Arsenal", "Real Madrid", "LIverpool")
(red, white, yellow) = clubs 
print (red)
print (white)
print (yellow)