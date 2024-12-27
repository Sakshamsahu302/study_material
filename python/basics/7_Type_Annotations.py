"""
If you know another programming language such as C or C++, you are used to declaring what data type you are working with. 
For example,

this is how you would declare an integer in C.
int a;

from this moment on, we know that "a" is of type integer. Then we would maybe assign an integer to a.
 a = 3 

However we don't do it like that in Python. Let's go through what we already know.
"""

a = 3
print(type(a))


"""OUTPUT:
<class 'int'>
As a is assigned an integer, it belongs to the integer class itself, without us having to say
"""

a = int() 

"""beforehand. a's data type would change accordingly, when it is assigned values from other data types."""

a = 'hello'
print(type(a))

"""OUTPUT:
<class 'str'>
"""

a = 3.14
print(type(a))

"""OUTPUT:
<class 'float'>
If Python is capable of determining the types itself, why are even type annotations useful?
"""

#Type Annotations: Why
"""
You understand where the type errors stem from.

1.If you are using an IDE, such as Visual Studio Code, typing the type annotations would allow you to access the built-in functions 
easier.

2.When a variable is of no type, you wouldn't be able to automatically access the built-in functions that you intend to use.

3.You would get syntax-highlighting as a warning before you even run your code.

4.Your code will be more readable & understandable. This is especially useful if you are working together with others.

"""

