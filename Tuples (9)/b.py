# Change Tuple Values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple. Example:
x = ("Pineapple", "Banana", "Strawberry")
y = list(x)
y[1] = "Mango"
x = tuple(y)
print (x)


# Add Items
thistuple = ("Mercedes", "BMW", "Audi", "Range Rover")
y = ("VolksWagen")
thistuple += y
print (thistuple)