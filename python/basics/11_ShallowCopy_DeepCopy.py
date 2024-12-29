#Shallow Copy:

"""A shallow copy creates a new object but does not create copies of nested objects. 
Instead, it references the original objects inside the container.
Changes to nested objects in the copied object will reflect in the original object and vice versa.
Example:"""

import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

shallow_copied[0][0] = 99
print(original)  # Output: [[99, 2, 3], [4, 5, 6]]

#Deep Copy:

"""A deep copy creates a new object and recursively copies all objects inside the container. 
This ensures the new object is entirely independent of the original.
Changes to the deep-copied object do not affect the original.
Example:"""

import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

deep_copied[0][0] = 99
print(original)  # Output: [[1, 2, 3], [4, 5, 6]]


#Key Differences
"""

Feature	        |                 Shallow Copy	                   |                Deep Copy
__________________________________________________________________________________________________________________
Copy Type	    |     Copies references to nested objects	       |   Creates copies of all nested objects
__________________________________________________________________________________________________________________
Mutual Changes	|     Changes to nested objects affect both copies |   Changes do not affect the other object
__________________________________________________________________________________________________________________
Use Cases	    |     Faster for small and flat structures	       |   Safer for complex/nested data structures
__________________________________________________________________________________________________________________
"""

"""Notes

1.Copy Module:

    -Use copy.copy() for shallow copy.
    -Use copy.deepcopy() for deep copy.

2.Built-in Data Types:

    -Shallow copies of immutable types (e.g., integers, strings, tuples) are identical to the original.
    -For lists, dictionaries, or sets with nested objects, understanding the difference between shallow and deep copies is essential.

3.Custom Classes:

Shallow and deep copy behavior depends on the class's implementation. Overriding __copy__ and __deepcopy__ can customize this behavior.
"""

#Important Questions with Answers on Shallow and Deep Copy
"""Q1: What is the key difference between shallow copy and deep copy?
Answer:

Shallow Copy: Creates a new object, but nested objects inside it are referenced, not copied.
Deep Copy: Creates a new object and recursively copies all nested objects, making it independent of the original.

Q2: Why do changes in a shallow copy reflect in the original object?
Answer:
In a shallow copy, only the top-level container is copied. 
The references to nested objects are shared between the original and the copied object. 
Hence, changes to these nested objects affect both.

Q3: Write a Python program to demonstrate the difference between shallow copy and deep copy.
Answer:
"""

import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

# Shallow Copy
shallow_copied = copy.copy(original)
shallow_copied[0][0] = 99  # Modify shallow copy
print("After shallow copy modification:")
print("Original:", original)  # Reflects changes
print("Shallow Copy:", shallow_copied)

# Reset original
original = [[1, 2, 3], [4, 5, 6]]

# Deep Copy
deep_copied = copy.deepcopy(original)
deep_copied[0][0] = 99  # Modify deep copy
print("\nAfter deep copy modification:")
print("Original:", original)  # No changes
print("Deep Copy:", deep_copied)

"""Q4: What happens when you use copy.deepcopy() on an object with self-references?
Answer:
copy.deepcopy() handles self-references by maintaining a memo dictionary to track objects already copied. 
This prevents infinite recursion.

Example:
"""

import copy

a = []
a.append(a)  # Self-reference

deep_copied = copy.deepcopy(a)
print(deep_copied)  # Output: [[]] (no infinite loop)

"""Q5: When would you prefer using a deep copy over a shallow copy?
Answer:
You would prefer a deep copy when:

-The object contains nested structures, and you want to modify them independently of the original.
-Sharing references between objects can lead to unintended side effects.

Q6: Predict the output of the following code snippet.

import copy

original = [1, [2, 3], 4]
shallow_copied = copy.copy(original)
shallow_copied[1][0] = 99
print(original)

# Output:
[1, [99, 3], 4]

Explanation: The shallow copy only copies the outer list, 
so the nested list [2, 3] is still shared between original and shallow_copied.

Q7: Is it possible to create a shallow copy without using the copy module?
Answer:
Yes, you can create a shallow copy using slicing (for lists) or the dict() constructor (for dictionaries).

Example:
"""
# Using slicing for lists
original_list = [1, 2, 3]
shallow_copied_list = original_list[:]

# Using dict() for dictionaries
original_dict = {'a': 1, 'b': 2}
shallow_copied_dict = dict(original_dict)

"""Q8: Can immutable objects like integers or strings be shallow or deep copied?
Answer:
No, immutable objects (e.g., integers, strings, tuples) are not affected by shallow or deep copying because 
their value cannot change. Copies of these objects simply reference the same value.


Q9: What is the role of the __copy__ and __deepcopy__ methods in custom classes?
Answer:

__copy__: Defines how shallow copies are made for objects of a custom class.
__deepcopy__: Defines how deep copies are made for objects of a custom class.
Example:"""

class Custom:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Shallow copy invoked")
        return Custom(self.value)

    def __deepcopy__(self, memo):
        print("Deep copy invoked")
        return Custom(self.value)

"""Q10: Modify the nested dictionary using shallow and deep copy to illustrate their differences.
Answer:
"""

import copy

# Nested dictionary
original_dict = {'a': {'x': 1, 'y': 2}, 'b': 3}

# Shallow Copy
shallow_copied = copy.copy(original_dict)
shallow_copied['a']['x'] = 99
print("Original after shallow modification:", original_dict)

# Deep Copy
original_dict = {'a': {'x': 1, 'y': 2}, 'b': 3}
deep_copied = copy.deepcopy(original_dict)
deep_copied['a']['x'] = 99
print("Original after deep modification:", original_dict)


#Output:
"""
# Shallow copy affects the original:
Original after shallow modification: {'a': {'x': 99, 'y': 2}, 'b': 3}

# Deep copy does not affect the original:
Original after deep modification: {'a': {'x': 1, 'y': 2}, 'b': 3}
"""

#Conceptual Questions

"""Q1: What happens when you modify an immutable object inside a shallow or deep copy?
Answer:

-Shallow Copy: If an immutable object (like a string, integer, or tuple) is part of a container, 
modifying it creates a new object, leaving the original container unchanged.

-Deep Copy: The same behavior applies since immutable objects cannot be changed in place, 
regardless of whether the copy is shallow or deep.

Q2: How does the copy module handle circular references during a deep copy?
Answer:
The copy.deepcopy() function maintains a memo dictionary to track objects that have already been copied. 
This prevents infinite recursion by ensuring that self-references are preserved correctly.

Q3: What are some performance implications of using deep copy in large datasets?
Answer:

-Memory Usage: Deep copying large datasets can consume significant memory because 
it creates independent copies of all nested objects.

-Time Complexity: Deep copy operations can be slow, especially for deeply nested or highly complex structures, 
as it recursively traverses and copies all elements.

-Optimization Tip: Use shallow copies or manual copying when full independence of nested objects is unnecessary.

"""

#Scenario-based Questions

"""Q1: You are cloning a configuration object that is frequently updated by multiple threads. 
Which type of copy will you use and why?
Answer:

1.Use a deep copy if the configuration contains nested structures and each thread needs its independent copy to 
prevent race conditions or side effects.

2.Use a shallow copy only if nested structures are not being modified, as it is faster and uses less memory.


Q2: How would you explain the behavior of shallow and deep copies to a non-technical team member?
Answer:

Imagine you have a blueprint of a house:

-Shallow Copy: You photocopy the blueprint. If someone modifies a specific room design, 
both the original and the copy show the changes because they share the same room designs.

-Deep Copy: You create a completely new blueprint. Any changes to one blueprint do not affect the 
other since they are entirely independent."""

#Practical Code Challenges
"""
Q1: Implement a custom deep copy function without using the copy module.
Q2: Given a nested dictionary with unknown depth, demonstrate how to create a deep copy manually.
"""
