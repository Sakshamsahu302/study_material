""" 'Assignment expression Operator'  affectionately known to many as 'The Walrus Operator' """

"""Introduced in python version 3.8, we can still view it as a recent addition to the language"""

"""The purpose of this feature is not a new way to assign objects to variables,but it gives programmers 
a convinient way of assign variables in middle of a expression"""

"""A simple assignment statement can also be replaced by an assignment expression, 
even though it looks clumsy and is definitely not the intended use case of it:"""

x = 5
# can be written as:
(x := 5)  # valid, but not recomended!
# the brackets are crucial
print(x)

"""OUTPUT:
5

You may wonder about the brackets, when you look at the asssignment expression but it is not meant to be the replacement of the
simple 'assignment statement' it's primary role is to be utilized within expressions
The following code shows a proper usecase: """

x=4.56
z=(square:=x**2)-(6.6/square)
print(z)

"""OUTPUT:
20.476194644506

Though you may argue that the following code might be even clearer:"""

x = 4.56
square = x**2
z = square - (6.6 / square)
print(z)

"""OUTPUT:
20.476194644506"""

"""(As we can see walrus operator helped us to reduce one line of code)"""

"""Here's another Python code example that demonstrates a similar scenario. First with the walrus operator:"""

# With the walrus operator
n = int(input("Please give a number: "))
if (square := n ** 2) > 3:
    print("The number is greater than 3.")
    print(f"The square of {n} is {square}.")

"""OUTPUT:
The number is greater than 3.
The square of 42 is 1764."""

#Now without the walrus operator:

n = int(input("Please give a number: "))
square= n ** 2
if square > 3:
    print("The number is greater than 3.")
    print(f"The square of {n} is {square}.")

"""OUTPUT:
The number is greater than 3.
The square of 42 is 1764"""


