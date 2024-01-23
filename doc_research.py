"""
Method syntax -> list.count(element)

- Param Val -> Required

- The parameter takes in ANY data type. Essentially the value is to search for.

- Return value/data type is an int & returns the number or occurrences

- Example:
my_list = ["apples", "bananas", "apples", "oranges"]

fruit_search_count = my_list.count("apples")

print(fruit_search_count)

- Description: 
The .count() method will take in any data type. 
It'll search the list for the value entered & 
outputs the number of occurrences it finds in the list.

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""

Method syntax -> list.count(element)

- Param Val -> Required

- The parameter takes in ANY data type. Essentially the value is to search for.

- Return the first occurrence of the value


- Example:
my_list = [28, 21, 8, 5, 13, 19, 20, 23, 15, 25]

x = my_list.index(8)

print(x)

- Description: 
The .index() method will take in any data type. 
It'll return the first value found even if there's mutilpe of the same values in the list


"""


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

Method syntax -> list.extend(element)

- Param Val -> Required

- The parameter takes in ANY data type. 

- Adds the specified list elements (or any iterable) to the end of the current list


- Example:
char_list = ["apples", "bananas", "apples", "oranges"]
num_list = [28, 21, 8, 5, 13, 19, 20, 23, 15, 25]

char_list.extend(num_list)

print(char_list)

- Description: 
The .extend() method will take in any data type.
It'll add a new list on to any list 

"""