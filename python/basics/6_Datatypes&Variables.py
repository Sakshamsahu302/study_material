"""There is a dodgy diffrence bw how python and other languages like C,java,etc. deal with variables.
there are integers,floating point numbers,strings and many more but things are not same as in C or C++"""

"""If you want to use list or assciative arrays in C e.g. you'll have to contrue the data type list or associative arrray from scratch
i.e. design memory structure and allocation management.you'll have to implement the necessary search and access method as well"""

"""Python provides power data types like list and associative arrays called 'dict'. """

"""What is a Variable?
A variable is something which can be changed.Variable is reffred to the memory location used by a computer program.In many
programming languages variable is a symbolic name for it's physical location.This memory location contains values like 
numbers,text,or more complicated types. We can use this variable to tell the computer to save some data or retrive some data 
from this physical location."""

"""Variables can be seen as a container to store some certain values.While a program is running, variables are accessed and 
sometimes changed i.e. a new value will be assigned to a variable."""

"""What we have said so far about variables best fits the way variables are implemented in C, C++ or Java.
Variable names have to be declared in these languages before they can be used.

int x;
int y;
Such declarations make sure that the program reserves memory for two variables with the names x and y.
The variable names stand for the memory location. It's like the two empty containers.
These containers are labeled with x and y. Like the two containers, the memory is empty as well.

Putting values into the variables can be realized with assignments.
The way you assign values to variables is nearly the same in all programming languages.
In most cases, the equal "=" sign is used. The value on the right side will be saved in the variable name on the left side.

We will assign the value 42 to both variables and we can see that two numbers are physically saved in the memory

x = 42;
y = 42;

We think that it is easy to understand what happens. If we assign a new value to one of the variables, let's say the value 78 to y:

y = 78;

We have exchanged the content of the memory location of y.

We have seen now that in languages like C, C++ or Java every variable has and must have a unique data type.
E.g., if a variable is of type integer, solely integers can be saved in the variable for the duration of the program.
In those programming languages every variable has to be declared before it can be used.
Declaring a variable means binding it to a data type.
"""

#"""VARIABLES IN PYTHON"""

"""There is no declaration of variables required in Python, which makes it quite easy.
It's not even possible to declare the variables. If there is need for a variable, you should think of a name and
start using it as a variable.

Another remarkable aspect of Python: Not only the value of a variable may change during program execution,
but the type as well. You can assign an integer value to a variable,
use it as an integer for a while and then assign a string to the same variable.""" 

#In the following line of code, we assign the value 42 to a variable:

i = 42

"""The equal "=" sign in the assignment shouldn't be seen as "is equal to". It should be "read" or interpreted as "is set to",
meaning in our example "the variable i is set to 42". Now we will increase the value of this variable by 1:"""

i = i + 1
print(i)

#OUTPUT: 43

"""As we have said above, the type of a variable can change during the execution of a script.
Or, to be precise, a new object, which can be of any type, will be assigned to it. We illustrate this in our following example:"""

i = 42          # data type is implicitly set to integer
i = 42 + 0.11       # data type is changed to float
i = "forty"     # and now it will be a string

"""
When Python executes an assignment like "i = 42", it evaluates the right side of the assignment and recognizes
that it corresponds to the integer number 42.
It creates an object of the integer class to save this data."""
#In other words, Python automatically takes care of the physical representation for the different data types.


#OBJECT REFERENCES

"""
Python variables are references to objects, but the actual data is contained in the objects:
As variables are pointing to objects and objects can be of arbitrary data types, variables cannot have types associated with them.
This is a huge difference from C, C++ or Java, where a variable is associated with a fixed data type.
This association can't be changed as long as the program is running.
"""

#Therefore it is possible to write code like the following in Python:

x = 42
print(x)

"""
OUTPUT:
42
"""

x = "Now x references a string"
print(x)

"""
OUTPUT:
Now x references a string
"""

"""We want to demonstrate something else now. Let's look at the following code:

x = 42
y = x

We created an integer object 42 and assigned it to the variable x.
After this we assigned x to the variable y. This means that both variables reference the same object.

What will happen when we execute
y = 78
after the previous code?

Python will create a new integer object with the content 78 and then the variable y will reference this newly created object

Most probably, we will see further changes to the variables in the flow of our program.
There might be, for example, a string assignment to the variable x.
The previously integer object "42" will be orphaned after this assignment.
It will be removed by Python, because no other variable is referencing it.

"""

"""
You may ask yourself, how can we see or prove that x and y really reference the
same object after the assignment y = x of our previous example?
The identity function id() can be used for this purpose. Every instance (object or variable) has an identity, i.e.,
an integer which is unique within the script or program, i.e., other objects have different identities.
So, let's have a look at our previous example and how the identities will change:"""

x = 42
print(id(x))

"""OUTPUT:140709828470448"""

y = x
print(id(x), id(y))

"""OUTPUT:(140709828470448, 140709828470448)"""

y = 78
print(id(x), id(y))

"""OUTPUT:(140709828470448, 140709828471600)"""


#VALID VARIABLE NAME

"""The naming of variables follows the more general concept of an identifier. A Python identifier is a name used to identify a variable,
function, class, module or other object.

A variable name and an identifier can consist of the uppercase letters "A" through "Z", the lowercase letters "a" through "z",
the underscore _ and, except for the first character, the digits 0 through 9. Python 3.x is based on Unicode.
That is, variable names and identifier names can additionally contain Unicode characters as well.

Identifiers are unlimited in length. Case is significant. The fact that identifier names are case-sensitive can cause problems to some Windows users,
where file names are case-insensitive, for example.

Exceptions from the rules above are the special Python keywords, as they are described in the following paragraph."""


#RULES FOR VALID VARIABLE NAMES
"""
1.Must Start with a Letter or an Underscore:

    The first character must be a letter (a-z, A-Z) or an underscore (_).
    Examples: _variable, myVar

2.Can Contain Letters, Digits, and Underscores:

    After the first character, the name can include letters, digits (0-9), and underscores.
    Examples: variable1, my_var, var_123

3.Cannot Start with a Digit:

    Variable names cannot begin with a number.
    Invalid: 1variable
    Valid: variable1

4.No Spaces Allowed:

    Variable names cannot contain spaces; use underscores instead.
    Invalid: my variable
    Valid: my_variable

5.Case-Sensitive:

    Variable names are case-sensitive, meaning variable, Variable, and VARIABLE are different.
    Examples: myVar, myvar, MYVAR

6.Cannot Be a Reserved Keyword:

    Python keywords (like if, while, for, True, False, etc.) cannot be used as variable names.
    Use help("keywords") in Python to view all reserved keywords.

Additional Considerations

Use Descriptive Names:

1.Choose variable names that clearly describe their purpose.
    Good: student_age, total_cost
    Bad: x, a1

2.Avoid Starting with an Underscore Unless Necessary:

    Variables starting with an underscore are typically reserved for special purposes (e.g., _privateVar).

3.Unicode Support:

    Python 3 supports Unicode characters in variable names.
    Examples: 变量 (Chinese), π (Greek letter), hình_ảnh (Vietnamese).
"""

#Python Keywords

"""No identifier can have the same name as one of the Python keywords, although they are obeying the above naming conventions:

and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in, is, 
lambda, None, nonlocal, not, or, pass, raise, return, True, try, 
while, with, yield 
There is no need to learn them by heart. You can get the list of Python keywords in the interactive shell by using help."""

#Changing Data Types and Storage Locations
"""
Programming means data processing. Data in a Python program is represented by objects. These objects can be

•built-in, i.e., objects provided by Python,

    Type Hierarchy,Here's a general hierarchy of data types:

        1.Basic Types: int, float, bool, complex, str

        2.Collection Types: list, tuple, set, frozenset, dict

        3.Binary Types: bytes, bytearray, memoryview

        4.Special Type: NoneType

•objects from extension libraries,

•created in the application by the programmer.

So we have different "kinds" of objects for different data types.
We will have a look at the different built-in data types in Python.
"""

# Text type
name = "Alice"

# Numeric types
age = 30
height = 5.9
complex_number = 2 + 3j

# Sequence types
fruits = ["apple", "banana"]
coordinates = (10, 20)
range_example = range(5)

# Set types
unique_letters = {"a", "b", "c"}
immutable_set = frozenset(["x", "y", "z"])

# Mapping type
person = {"name": "Alice", "age": 30}

# Boolean type
is_adult = True

# Binary types
binary_data = b"hello"
mutable_binary = bytearray(5)

# None type
nothing = None

#INTEGER DIVISION

"""There are two kinds of division operators:

•"true division" performed by "/"
•"floor division" performed by "//" 

True Division(Returns the whole result):
True division uses the slash (/) character as the operator sign. Most probably it is what you expect "division" to be.
The following examples are hopefully self-explanatory:

10 / 3
OUTPUT:
3.3333333333333335
10.0 / 3.0
OUTPUT:
3.3333333333333335
10.5 / 3.5
OUTPUT:
3.0

Floor Division(Returns only the integer value of the result):
The operator "//" performs floor division, i.e., the dividend is divided by the divisor - like in true division - 
but the floor of the result will be returned. The floor is the largest integer number smaller than the result of the true division.
This number will be turned into a float, if either the dividend or the divisor or both are float values.
If both are integers, the result will be an integer as well. In other words, "//" always truncates towards negative infinity.

Connection to the floor function: In mathematics and computer science, the floor function is the function that takes as input 
a real number x and returns the greatest integer floor ( x ) = ⌊ x ⌋ that is less than or equal to x.

If you are confused now by this rather mathematical and theoretical definition,
the following examples will hopefully clarifiy the matter:

9 // 3
OUTPUT:
3
10 // 3
OUTPUT:
3
11 // 3
OUTPUT:
3
12 // 3
OUTPUT:
4

"""
