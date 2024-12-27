"""Sequences are one of the principal built-in data types besides numerics, mappings, files, instances and exceptions. 
Python provides for six sequence (or sequential) data types:

strings
byte sequences
byte arrays
lists
tuples
range objects

Strings, lists, tuples, bytes and range objects may look like utterly different things, but they still have some underlying 
concepts in common:

The items or elements of strings, lists and tuples are ordered in a defined sequence

The elements can be accessed via indices"""

text = "Lists and Strings can be accessed via indices!"
print(text[0], text[10], text[-1])    

"""OUTPUT:
L S !

Accessing lists:"""

cities = ["Vienna", "London", "Paris", 
          "Berlin", "Zurich", "Hamburg"]

print(cities[0])
print(cities[2])
print(cities[-1])  

"""OUTPUT:
Vienna
Paris
Hamburg
"""

"""Unlike other programming languages Python uses the same syntax and function names to work on sequential data types. 
For example, the length of a string, a list, and a tuple can be determined with a function called len():"""

countries = ["Germany", "Switzerland", "Austria", 
             "France", "Belgium", "Netherlands", 
             "England"]

len(countries)  # the length of the list, i.e. the number of objects

"""
OUTPUT:
7
"""

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
len(fib)

"""
OUTPUT:
10
"""
#Bytes

"""The byte object is a sequence of small integers. The elements of a byte object are in the range 0 to 255, 
corresponding to ASCII characters and they are printed as such."""

s = "Glückliche Fügung"
s_bytes = s.encode('utf-8') 
print(s_bytes)

"""OUTPUT:
b'Gl\xc3\xbcckliche F\xc3\xbcgung'
"""

#Python lists


"""
So far we had already used some lists, and here comes a proper introduction. Lists are related to arrays of programming languages 
like C, C++ or Java, but Python lists are by far more flexible and powerful than "classical" arrays. For example, 
not all the items in a list need to have the same type. Furthermore, lists can grow in a program run, 
while in C the size of an array has to be fixed at compile time.

Generally speaking a list is a collection of objects. To be more precise: A list in Python is an ordered group of items or elements.
It's important to notice that these list elements don't have to be of the same type. 
It can be an arbitrary mixture of elements like numbers, strings, other lists and so on. 
The list type is essential for Python scripts and programs, in other words, you will hardly find any serious Python code without a list.

The main properties of Python lists:

1.They are ordered
2.They contain arbitrary objects
3.Elements of a list can be accessed by an index
4.They are arbitrarily nestable, i.e. they can contain other lists as sublists
5.Variable size
6.They are mutable, i.e. the elements of a list can be changed

"""

#List Notation and Examples

"""List objects are enclosed by square brackets and separated by commas. The following table contains some examples of lists:"""


|      List 	                     |                 Description    |
----------------------------------------------------------------------------------
[]      	                         |    An empty list
__________________________________________________________________________________
[1,1,2,3,5,8]	                     |   A list of integers
__________________________________________________________________________________
[42, "What's the question?", 3.1415] |	 A list of mixed data types
__________________________________________________________________________________                                     
                                     |
["Stuttgart", "Freiburg", "München", |
 "Nürnberg", "Würzburg", "Ulm",      |
 "Friedrichshafen", Zürich", "Wien"] |	 A list of Strings
___________________________________________________________________________________
[["London","England", 7556900],      |
 ["Paris","France",2193031],         |
 ["Bern", "Switzerland", 123466]]    |	 A nested list
__________________________________________________________________________________
                                     |
["High up", ["further down",         |
["and down", ["deep down",           |
"the answer", 42]]]]	             |   A deeply nested list
___________________________________________________________________________________