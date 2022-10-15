# String Format
# We can combine strings and numbers by using the format() method
age = 22
txt = "My name is Shaz and I am {}."
print (txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.50
myorder = "I want {} pieces of item {} for {} dollars."
print (txt.format(quantity, itemno, price))