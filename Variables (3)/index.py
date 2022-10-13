# Output Variables
x = "Python"
y = "is"
z = "awesome"
print (x, y, z)

a = 5
b = 20
print (a + b)


# Global Variables - Variables that are created outside of a function
i = "fun"

def myfunc():
    print ("Python is " + i)

myfunc()


def myfunc():
    global j
    j = "GOAT"
    print ("Cristiano Ronaldo is the " + j)

myfunc()