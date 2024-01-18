"""
1. Create a Python List with at least 10 elements.
2. Create an empty List, then using a for loop, add the numbers 1-100 to the list

3.Given the list:
my_list = ["a", "b", "c", "d", "b", "a", "e"]

write code to loop through the list and print only the vowels

4. Separate odds and evens. Write code that will take a list of positive integers and will create a new list with all of the odds at the beginning of the list and all of the evens at the end of the list. For example:
a_list = [1,5,8,2,4,8,1,3,5,9]

# ... your code goes here

new_list = [1,5,1,3,5,9,8,2,4,8]

print(new_list)

5. Manually reverse the elements in a list, without using "slicing". See the following example:
my_list = [1,2,3,4,5,6,7,8]

# After your code

my_list = [8,7,6,5,4,3,2,1]


"""

# 1.
list_one = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# 2.
list_sec = []

# for i in range(1,101):
#     list_sec.append(i)

# print(list_sec)

# 3. 
# my_list = ["a", "b", "c", "d", "b", "a", "e"]

# for i in my_list:
#     if i == 'a' or i == 'e':
#         print(i)

# 4. Separate odds and evens. Write code that will take a list of positive integers and will create a new list with all of the odds at the beginning of the list and all of the evens at the end of the list. For example:
# a_list = [1,5,8,2,4,8,1,3,5,9,4,8,1,3,5,4,8,1,3,5,1,5,8,2,4]


# def rearranged_list(list):
#     b_list = []

#     for i in list:
#         if i % 2 != 0:
#             b_list.append(i)

#     for i in list:
#         if i % 2 == 0:
#             b_list.append(i)


#     print(b_list)

# rearranged_list(a_list)

# 5.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# new_list = []

# for i in my_list:
#     new_list.insert(0, i)

# print(new_list)      
  
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(my_list) // 2):
    first = i
    second = len(my_list) - 1 -i
    # second = - 1 -i
    # temp = my_list[first]
    # my_list[first] = my_list[second]
    # my_list[second] = temp
    my_list[first], my_list[second] = my_list[second], my_list[first]

print(my_list)