"""
Lists and dictionaries are indispensable components of Python programming, 
making Python a powerful and extremely useful programming language."""

#Example 

person = {
    'name': 'Anna Schmidt',
    'age': 28,
    'city': 'Berlin',
    'email': 'anna@example.de'
}

"""In Python, a dictionary is a data structure that stores key-value pairs. 
Let's take a closer look at our example dictionary to explain the essential details:

1-A dictionary is wrapped in curly brackets {}.

2-A dictionary contains keys and values.

3-The keys in our dictionary are strings and are positined in front of the colons. 

4-The keys of our example dictionary are 'name', 'age', 'city', and 'email'.

5-Each key is associated with a corresponding value separated by a colon ':' : 'Anna Schmidt' is the value 
associated with the key 'name', 28 with 'age', 'Berlin' with 'city', and 'anna@example.de' with 'email'.

6-We call a key-value pair like 'name': 'Anna Schmidt' an item. So a dictionary contains an arbitrary sequence of 
  'key:value' pairs separated by commas.

Dictionaries are useful for organizing data in a way that allows quick and easy access based on specific keys.
    
In the code snippet below, we demonstrate how to retrieve specific pieces of information from our dictionary, 
such as the 'name' or 'age', from the dictionary:"""

# Retrieving values
name = person['name']
age = person['age']

print("Name:", name)
print("Age:", age)

# OUTPUT:
"""Name: Anna Schmidt
Age: 28"""



"""To retrieve a value from a dictionary, we use the dictionary's name followed by square brackets containing the key"""

"""Now, we'll illustrate how dictionaries can be modified because they are mutable. 
Let's consider a scenario where Anna relocates from Berlin to Freiburg, 
renowned as one of Germany's most picturesque cities, 
known for its favorable weather compared to other regions in the country.
"""
# Anna moves to Freiburg
person['city'] = 'Freiburg'

# Updated information
print(person)

'''OUTPUT:
{'name': 'Anna Schmidt', 'age': 28, 'city': 'Freiburg', 'email': 'anna@example.de'}'''

"""Like lists, they can be easily changed, can be shrunk and grown ad libitum at run time. 
They shrink and grow without the necessity of making copies. Dictionaries can be contained in lists and vice versa.

Let's add Anna's gender and her favorite hobbies, which include reading, music, and programming 
(as she's a beginner in Python), to the existing dictionary:

"""
person['sex'] = 'female'
person['favorite_hobbies'] = ['reading', 'music', 'programming']

print(person)

"""OUTPUT:
{'name': 'Anna Schmidt',
 'age': 28,
 'city': 'Freiburg',
 'email': 'anna@example.de',
 'favorite_hobbies': ['reading', 'music', 'programming'],
 'sex': 'female'}

Now, we remove again the gender information from the dictionary:"""

# Deleting gender information
del person['sex']
print(person)

"""OUTPUT:
{'name': 'Anna Schmidt', 'age': 28, 'city': 'Freiburg', 'email': 'anna@example.de', 
'favorite_hobbies': ['reading', 'music', 'programming']}
"""

#Associative Arrays

"""More theoretically, we can say that dictionaries are the Python implementation of an abstract data type, 
known in computer science as an associative array. Associative arrays consist - 
like dictionaries of (key, value) pairs, such that each possible key appears at most once in the collection. 
Any key of the dictionary is associated (or mapped) to a value. 
The values of a dictionary can be any type of Python data. So, dictionaries are unordered key-value-pairs. 
Dictionaries are implemented as hash tables, 
and that is the reason why they are known as "Hashes" in the programming language Perl.

Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. 
Dictionaries belong to the built-in mapping type, but so far, they are the sole representative of this kind!"""

#Dictionary and Lists

"""But what's the difference between lists and dictionaries?

A list is a sequence of objects where the order matters. You can access list elements directly by their position in this order. Similarly, dictionaries are also ordered, but unlike lists, you can't access elements by their position. We can also say that contrary to lists that the order of a dictionary is not important. The order of items in a dictionary is determined by the sequence in which they were added. If we print a dictionary, we can see this ordering.

Let's demonstrate this with the following dictionary:"""

city_population = {
    'Berlin': (3769495, 'Germany'),
    'Paris': (2161000, 'France'),
    'Vienna': (1921641, 'Austria'),
    'Hamburg': (1841179, 'Germany'),
    'Amsterdam': (872680, 'Netherlands'),
    'Rotterdam': (651446, 'Netherlands'),}

#We will add now the German cities "München" (Munich) and "Köln' (Cologne) to our dictionary:

city_population['Munich'] = (1471508, 'Germany')
city_population['Cologne'] = (1085664, 'Germany')
print(city_population)

"""OUTPUT:
{'Berlin': (3769495, 'Germany'), 'Paris': (2161000, 'France'), 'Vienna': (1921641, 'Austria'), 
'Hamburg': (1841179, 'Germany'), 'Amsterdam': (872680, 'Netherlands'), 'Rotterdam': (651446, 'Netherlands')
, 'Munich': (1471508, 'Germany'), 'Cologne': (1085664, 'Germany')}"""

"""We can see that the cities "München" (Munich) and "Köln' (Cologne) had been added to the end of the dictionary 
    as expected. The order of the items in the dictionary is determined by the sequence in which they were added.
"""

#Convert Dictionaries to Lists

"""If you have worked for a while with Python, nearly inevitably the moment will come, 
when you want or have to convert lists into dictionaries or vice versa. It wouldn't be too hard to write a 
function doing this. But Python wouldn't be Python, if it didn't provide such functionalities. 
We can convert the previously defined dictionary into a list with the following expression:"""

city_population_list = list(city_population.items())
print(city_population_list)


"""OUTPUT:
[('Berlin', (3769495, 'Germany')),
 ('Paris', (2161000, 'France')),
 ('Vienna', (1921641, 'Austria')),
 ('Hamburg', (1841179, 'Germany')),
 ('Amsterdam', (872680, 'Netherlands')),
 ('Rotterdam', (651446, 'Netherlands')),
  ('Munich', (1471508, 'Germany')),
 ('Cologne', (1085664, 'Germany'))]"""

"""This list holds the identical information as the dictionary city_population. 
However, retrieving this data differs significantly. What if you want to get the population of Amsterdam? 
It's extremely easy with the dictionary:
"""

print(city_population['Amsterdam'][0])

"""OUTPUT:
872680

It's a lot more complicated in the list representation. We're limited to accessing indices rather than city names. 
Consequently, we must iterate over the list and inspect all the tuples to determine if the first entry corresponds to 
the city of Amsterdam."""

# Given list of tuples
city_population_list = [
    ('Berlin', (3769495, 'Germany')),
    ('Paris', (2161000, 'France')),
    ('Vienna', (1921641, 'Austria')),
    ('Hamburg', (1841179, 'Germany')),
    ('Amsterdam', (872680, 'Netherlands')),
    ('Rotterdam', (651446, 'Netherlands')),
    ('Stuttgart', (634830, 'Germany')),
    ('Zurich', (415215, 'Switzerland')),
    ('Graz', (290571, 'Austria')),
    ('Strasbourg', (280966, 'France')),
    ('Freiburg', (230241, 'Germany')),
    ('Geneva', (201818, 'Switzerland')),
    ('Basel', (178128, 'Switzerland')),
    ('Salzburg', (155031, 'Austria')),
    ('Luxembourg City', (124528, 'Luxembourg')),
    ('Metz', (117619, 'France')),
    ('Munich', (1471508, 'Germany')),
    ('Cologne', (1085664, 'Germany'))
]

# Prompting the user for a city name
city_name = input("Enter a city name: ")

# Finding the population of the city
population = None
for city, (pop, _) in city_population_list:
    if city_name.lower() == city.lower():
        population = pop
        break

# Displaying the population if found, or a message if not found
if population is not None:
    print(f"The population of {city_name} is {population}")
else:
    print(f"Population data for {city_name} is not available.")

"""OUTPUT:
The population of Amsterdam is 872680

In this aspect, the dictionary method outperforms the list approach by enabling swifter data access. 
In a dictionary, you can directly retrieve the population of a city using its name as the key, 
which is much quicker compared to searching through a list to find the population. 
Think of it like looking up a word in a dictionary versus flipping through the pages of a book to find it. 
The dictionary provides instant access, while the list requires more time to search through.

The efficiency of this algorithm depends on the size of the city_population_list. 
Since it iterates through the entire list linearly to find the population of a given city, 
the time complexity is O(n), where n is the number of cities in the list.

For a small number of cities, this approach is acceptable. 
However, as the number of cities grows larger, the linear search becomes less efficient, 
especially if the city being searched for is towards the end of the list or if the list contains a large number of cities.

In scenarios where performance is critical or when dealing with a large dataset, 
a more efficient approach would be to use a dictionary instead of a list, 
where the keys are the city names. This would allow constant-time (O(1)) lookups, 
providing faster access to population data.

"""
#items() Method in Python

"""Definition: The items() method is used with dictionaries to return a view object of the dictionary's key-value pairs.

Syntax:"""

print(city_population.items())

"""Returns: A dict_items object, which is an iterable containing tuples of (key, value)."""

#Convert to List:

print(list(city_population.items()))

"""Use Case: Useful for looping through both keys and values in a dictionary:"""

for key, value in city_population.items():
    print(key, value)

"""If we apply the method items() to a dictionary, we don't get a list back, as it used to be the case in Python 2, 
but a so-called items view. The items view can be turned into a list by applying the list function. 
We have no information loss by turning a dictionary into an item view or an items list, i.e. 
it is possible to recreate the original dictionary from the view created by items().

Accessing dictionary items via a method like items() provides a more efficient approach compared to creating 
lists directly due to several reasons:

1) Lazy Evaluation: The items() method doesn't generate the entire list of key-value pairs upfront. Instead, 
it returns a view object that generates items on-the-fly as needed. This lazy evaluation saves memory and processing time, 
especially when dealing with large dictionaries where creating a complete list of items upfront may be resource-intensive.

2) Memory Efficiency: Generating a list of items directly requires storing all key-value pairs in memory simultaneously, 
which can be inefficient for large dictionaries. In contrast, using items() provides a memory-efficient solution as it 
generates items dynamically without storing the entire list in memory at once.

3) Time Complexity: While both approaches have similar time complexity for iterating over all items (O(n), 
where n is the number of items in the dictionary), using items() may provide better performance in certain scenarios. 
For example, if only a subset of items is needed, items() allows for efficient iteration over only the required items 
without iterating over the entire dictionary.

Overall, using methods like items() for accessing dictionary items provides a more efficient and memory-friendly approach, 
especially for large dictionaries or scenarios where lazy evaluation and selective item retrieval are beneficial.

"""

#keys()

"""The keys() method returns a view object that displays a list of all keys in the dictionary. 
This allows you to iterate over or access the keys directly without needing to create a separate list of keys."""

city_info_dict = {'Stuttgart': (207.35, 634830), 'Karlsruhe': (173.46, 313092), 'Mannheim': (144.96, 309370), 
                  'Freiburg': (153.07, 230241), 'Heidelberg': (108.83, 160355), 'Heilbronn': (99.88, 125960)}

# Using keys() to access the keys of the dictionary
city_names = city_info_dict.keys()

print("City Names:")
for city in city_names:
    print(city)

"""While the keys() method is available in Python dictionaries, it's less commonly used because iterating over a 
dictionary directly implicitly iterates over its keys. 
Here's an example demonstrating this:"""

city_info_dict = {'Zurich': (87.88, 434008), 'Geneva': (15.93, 201818), 'Basel': (23.91, 178015), 'Lausanne': (41.38, 146372), 'Bern': (51.62, 133798), 'Lucerne': (37.04, 82106), 'St. Gallen': (39.85, 75834)}

# Iterating over the dictionary directly, which implicitly iterates over keys
print("City Names:")
for city in city_info_dict:
    print(city)

"""OUTPUT:
City Names:
Zurich
Geneva
Basel
Lausanne
Bern
Lucerne
St. Gallen"""



#values()

"""We can also iterate directly over the values of a dictionary:"""

# Iterating over the values of the dictionary using values() method
print("City Data (Area, Population):")
for area, population in city_info_dict.values():
    print("Area:", area, "sq. km, Population:", population)

"""OUTPUT:
City Data (Area, Population):
Area: 87.88 sq. km, Population: 434008
Area: 15.93 sq. km, Population: 201818
Area: 23.91 sq. km, Population: 178015
Area: 41.38 sq. km, Population: 146372
Area: 51.62 sq. km, Population: 133798
Area: 37.04 sq. km, Population: 82106
Area: 39.85 sq. km, Population: 75834"""

#Incrementally Creating a Dictionary
"""So, it's possible to create a dictionary incrementally by starting with an empty dictionary. 
We haven't mentioned so far, how to define an empty one. It can be done by using an empty pair of brackets. 
The following defines an empty dictionary called city:"""

city_population = {}
print(city_population) # Output: {}

city_population['Berlin'] = (3769495, 'Germany')
city_population['Stuttgart'] = (634830, 'Germany')

print(city_population) # Output: {'Berlin': (3769495, 'Germany), 'Stuttgart': (634830, 'Germany)}



#Closer Look at Keys and Values

"""Looking at our first examples with the cities and their population, you might have gotten the wrong impression 
hat the values in the dictionaries have to be different. The values can be the same, 
as you can see in the following example. 
In honour to the patron saint of Python "Monty Python", we'll have now some special food dictionaries. 
What's Python without "bacon", "egg" and "spam"?"""

food = {"bacon": "yes", "egg": "yes", "spam": "no" }
print(food)

#OUTPUT:{'bacon': 'yes', 'egg': 'yes', 'spam': 'no'}

"""Keys of a dictionary are unique. In casse a keys is defined multiple times, the value of the last "wins":"""

food = {"bacon" : "yes", "spam" : "yes", "egg" : "yes", "spam" : "no" }
print(food)

#OUTPUT:{'bacon': 'yes', 'spam': 'no', 'egg': 'yes'}

#Our next example is a simple English-German dictionary:

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print(en_de)
print(en_de["red"])

"""OUTPUT:
{'red': 'rot', 'green': 'grün', 'blue': 'blau', 'yellow': 'gelb'}
rot"""

"""What about having another language dictionary, let's say German-French?

Now it's even possible to translate from English to French, 
even though we don't have an English-French-dictionary.""" 


# de_fr[en_de["red"]]  gives us the French word for "red", i.e. "rouge":

de_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}
en_de = {"red": "rot", "green": "grün", "blue": "blau", "yellow": "gelb"}
print(en_de)

#OUTPUT:{'red': 'rot', 'green': 'grün', 'blue': 'blau', 'yellow': 'gelb'}

print(en_de["red"])

#OUTPUT:rot

de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print("The French word for red is: " + de_fr[en_de["red"]])

"""OUTPUT:
The French word for red is: rouge
We can use arbitrary types as values in a dictionary, but there is a restriction for the keys. 


Only immutable data types can be used as keys, i.e. no lists or dictionaries can be used: 
If you use a mutable data type as a key, you get an error message:"""

#dic = {[1,2,3]: "abc"}

"""OUTPUT:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[39], line 1
----> 1 dic = {[1,2,3]: "abc"}

TypeError: unhashable type: 'list'


Tuple as keys are okay, 
as you can see in the following example:"""

dic = {(1, 2, 3): "abc", 3.1415: "abc"}
print(dic)

#OUTPUT:{(1, 2, 3): 'abc', 3.1415: 'abc'}



#pop() Method in Python

"""Lists can serve as stacks, with the pop() method used to extract an element from the stack. 
This functionality is straightforward for lists. However, considering dictionaries, 
does it make sense to have a pop() method? Unlike lists, dictionaries are not sequential data structures; 
they lack indexing. Consequently, the pop() method behaves differently with dictionaries.

In dictionaries, the pop() method is used to remove a specific key-value pair from the dictionary and return 
the corresponding value. 

Here's how it works:

1) You specify the key of the item you want to remove as an argument to the pop() method. 
2) The pop() method then searches for this key in the dictionary. 
3) If the key is found, the corresponding key-value pair is removed from the dictionary, 
and the value associated with the key is returned. 4) If the key is not found, a KeyError is raised.

Here's an example to illustrate:"""

capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam", "Switzerland":"Bern"}
capital = capitals.pop("Austria")
print(capital)

#OUTPUT:Vienna

print(capitals)

#OUTPUT:{'Germany': 'Berlin', 'Netherlands': 'Amsterdam', 'Switzerland': 'Bern'}


"""If we try to find out the capital of France in the previous example, we raise a KeyError. 
To prevent these errors, there is an elegant way. The method pop() has an optional second parameter, 
which can be used as a default value, if key is not in the dictionary:"""

capital = capitals.pop("France", "Paris")
print(capital)

#OUTPUT:Paris

capital = capitals.pop("Germany", "München")
print(capital)

#OUTPUT:Berlin


#popitem() Method in Python

"""popitem() is a method of dict, which doesn't take any parameter and removes and returns a (key,value) pair as a 2-tuple. 
If popitem() is applied on an empty dictionary, a KeyError will be raised.

Pairs are returned in LIFO (last-in, first-out) order."""

capitals = {"Springfield": "Illinois", 
            "Augusta": "Maine", 
            "Boston": "Massachusetts", 
            "Lansing": "Michigan", 
            "Albany": "New York", 
            "Olympia": "Washington", 
            "Toronto": "Ontario"}
(city, state) = capitals.popitem()
print((city, state))

#OUTPUT:('Toronto', 'Ontario')

print(capitals.popitem())

#OUTPUT:('Olympia', 'Washington')

print(capitals.popitem())

#help(dict.popitem)

"""OUTPUT:
Help on method_descriptor:

popitem(self, /)
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty."""

print(capitals.popitem())

#OUTPUT:('Albany', 'New York')

print(capitals.popitem())

#OUTPUT:('Lansing', 'Michigan')


#Accessing Non-existing Keys

#If you try to access a key which doesn't exist, you will get an error message:

locations = {"Stuttgart": "Baden-Württemberg", 
             "Hamburg": "Hamburg", 
             "München": "Bayern", 
             "Köln": "Nordrhein-Westfalen"}


#print(locations["Saarbrücken"])

"""
OUTPUT:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[10], line 5
      1 locations = {"Stuttgart": "Baden-Württemberg", 
      2              "Hamburg": "Hamburg", 
      3              "München": "Bayern", 
      4              "Köln": "Nordrhein-Westfalen"}
----> 5 locations["Saarbrücken"]

KeyError: 'Saarbrücken'
To prevent getting an exception we can check first, if the city is in:"""

location = "Saarbrücken"

if location in locations:
    print(locations[location])
else:
    print(f"{location} is not a key of locations!")

#OUTPUT:Saarbrücken is not a key of locations!

"""
Another method to access the values via the key consists in using the get() method. get() is not raising an error, 
if an index doesn't exist. In this case it will return None. 
It's also possible to set a default value, which will be returned, if an index doesn't exist:"""

print(locations.get("Saarbrücken")) # return None

#Another example:

proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
print(proj_language["proj1"])

#OUTPUT:'Python'

print(proj_language.get("proj2"))

#OUTPUT:'Perl'

proj_language.get("proj4")
print(proj_language.get("proj4")) 

#OUTPUT:None

# setting a default value:

print(proj_language.get("proj4", "Python"))

#OUTPUT:'Python'


#Important Methods

"""A dictionary can be copied with the method copy():"""

words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words)

"""This copy is a shallow copy, not a deep copy. If a value is a complex data type like a list, 
for example, in-place changes in this object have effects on the copy as well:
"""

trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

trainings2 = trainings.copy()

trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings2)

"""If we check the output, we can see that the title of course2 has been changed not only in the dictionary training but 
in trainings2 as well.

Everything works the way you expect it, if you assign a new value, i.e. a new object, to a key:
"""

trainings = { "course1": {"title": "Python Training Course for Beginners", 
                         "location": "Frankfurt", 
                         "trainer": "Steve G. Snake"},
              "course2": {"title": "Intermediate Python Training",
                         "location": "Berlin",
                         "trainer": "Ella M. Charming"},
              "course3": {"title": "Python Text Processing Course",
                         "location": "München",
                         "trainer": "Monica A. Snowdon"}
              }

trainings2 = trainings.copy()

print(id(trainings["course1"]))  # ID of the original inner dict
print(id(trainings2["course1"]))  # Should be the same for shallow copy


trainings["course2"] = {"title": "Perl Seminar for Beginners",
                         "location": "Ulm",
                         "trainer": "James D. Morgan"}

print(trainings["course2"])

#OUTPUT:{'title': 'Perl Seminar for Beginners', 'location': 'Ulm', 'trainer': 'James D. Morgan'}

print(trainings2["course2"])

#OUTPUT:{'title': 'Perl Seminar for Beginners', 'location': 'Berlin', 'trainer': 'Ella M. Charming'}




#clear() Method in Python

"""The clear() method in Python is used to remove all items from a dictionary, effectively emptying it. 
After using the clear() method, the dictionary will still exist, but it will be empty."""

# Syntax : dictionary.clear()

"""Key Points

1-Mutates the Dictionary:

    -The clear() method modifies the dictionary in place.

    -It does not return any value (None).

2-Does Not Delete the Dictionary:

    -The dictionary object itself remains; it just becomes empty.

3-Usage:

    -It's useful when you want to retain the dictionary object but remove its contents.
"""

# Example:

# Define a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Clear the dictionary
my_dict.clear()

# Print the dictionary
print(my_dict)  # Output: {}

"""Behavior with References
If another variable references the same dictionary, clearing it will affect all references, 
as both point to the same object in memory.

Example:"""

# Create a dictionary and reference it
original = {"a": 1, "b": 2}
reference = original

# Clear the dictionary
original.clear()

# Both variables now reference the empty dictionary
print(original)   # Output: {}
print(reference)  # Output: {}


#When to Use clear()
"""
-To reset a dictionary without deleting it.
-When working with shared references to ensure all references see an empty dictionary."""



#Update: Merging Dictionaries

"""What about concatenating dictionaries, like we did with lists? There is someting similar for dictionaries: 
the update method update() merges the keys and values of one dictionary into another, 
overwriting values of the same key:"""

knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge)

#OUTPUT:{'Frank': {'Perl', 'Python'}, 'Monica': {'C', 'C++'}, 'Guido': {'Python'}}



#Iterating over a Dictionary
"""
No method is needed to iterate over the keys of a dictionary:"""

d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
     print(key) 

"""
OUTPUT:
a
b
c
d


However, it's possible to use the method keys(), we will get the same result:"""

for key in d.keys():
     print(key) 


"""OUTPUT:
a
b
c
d


The method values() is a convenient way for iterating directly over the values:"""

for value in d.values():
    print(value)


"""OUTPUT:
123
34
304
99


The above loop is logically equivalent to the following one:""" #logically, because the second way is less efficient!

for key in d:
    print(d[key])


"""OUTPUT:
123
34
304
99"""

