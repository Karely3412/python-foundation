# Exsersie -> String Interpolation 
""" 
You can use:
name:.2f -> gives money 
name:<8  -> pushes out way to the right
name:>8  -> pushes out way to the right
name:^8  -> centers
name:08  -> this will give it multiple digets of integers.

"""
# - - - - - - - - - - - - - - - - - -
name = 'Name'
city = 'City'
state = 'State'
age = 'Age'

name1 = 'Jane'
name2 = 'Fred'
name3 = 'Betsy'

city1 = 'Boston'
city2 = 'Portland'
city3 = 'Orlando'

state1 = 'Massachusetts'
state2 = 'Oregon'
state3 = 'Florida'

age1 = 24
age2 = 31
age3 = 29

dash = '-'

# print(f'{name:<8}{city:<11}{state:<13}{age:>4}')
# print(f'{dash*7} {dash*10} {dash*13} {dash*4}')
# print(f'{name1:<8}{city1:<10}{state1:<13}{age1:>4}')
# print(f'{name2:<8}{city2:<10}{state2:<13}{age2:>4}')
# print(f'{name3:<8}{city3:<10}{state3:<13}{age3:>4}')


# For the header you can do it like this instead of using a variable because the header names are only being used as is.
# print(f"{'Name':<8}{'City':<11}{'State':<13}{'Age':>4}")

# You can also so do:
# Go over the video to get better detail on this example.
# print(f"{name1:<{col1}}")


    # peoples_list = {
    #     "name": name,
    #     "city": city,
    #     "state": state,
    #     "age": age
    # }
    # peeps_info = f'{header}\n{dashes}\n{person.name:<8}{person.city:<14}{person.state:<14}{person.age:>4}'


# def people_info(persons_list):

#     dash = '-'
#     header = 'Name' + ' '*4 + 'Ctiy' + ' '*10 + 'State' + ' '*10 + 'Age'
#     dashes = f'{dash*6}  {dash*12}  {dash*13}  {dash*4}'

#     persons_info = ""
#     for person in persons_list:
#         person_info = f'{person[0]:<8}{person[1]:<14}{person[2]:<14}{person[3]:>4}\n'
#         persons_info += person_info   # <-- persons_info = persons_info + person_info (longer version)
        

#     peeps_info = f"{header}\n{dashes}\n{persons_info}"


#     return peeps_info

    
# persons_list = [
#     ['Mini', 'Aniheim', 'Califonia', "100"],
#     ['Donald', 'Aniheim', 'Califonia', "100"],
#     ['Mickey', 'Aniheim', 'Califonia', "100"]
#     ]

# print(people_info(persons_list))



# Needed results:

# Name   City       State         Age
# ------ ---------- ------------- ----
# Jane   Boston     Massachusetts  24
# Fred   Portland   Oregon         31
# Betsy  Orlando    Florida        29




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Excersie -> Inputs
"""
When adding inputs make you are casting data types. Make sure you're adding strings to strings or integers to integers.


"""



# def input_func():
#     question_1 = input (" ")
    


















# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Excersie -> Data Type Conversons 
"""
Notes:
Go back to video to see the examples again. 


"""
    
# Implicit:
     
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

# print("datatype of num_int:",type(num_int))
# print("datatype of num_flo:",type(num_flo))

# print("Value of num_new:",num_new)
# print("datatype of num_new:",type(num_new))


# Explicit:

# x = 5
# print('I have ' + str(x) + ' dollars')
    

# a = 6
# b = 5.5
# c = a * b
# print(int(c))
# 33


# s = "John"
# k = "95"
# print(s + k)
# #John95


# g = 3.14159265
# print(int(g))
# 3


# c = "Done"
# d = str(100)
# j = c + d
# print(j)
# it'll give you an error if d isn't casted as a string


# r = 4.345
# d = 99.1
# print(float(r) + float(d))
# 103.445

# def data_type_conversion(data):
#     if data:




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# def input_answers():
#     print('What ethinicity is your dad? ')
#     answer_1 = input()

#     print('What ethinicity is your mom? ')
#     answer_2 = input()
    

#     return f'You are {answer_1} & {answer_2}!'


# print(input_answers())


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# number = 8
# point_num = 8.8
# my_string = "888"
# the_bool = True

# def type_casting(input):
#     if type(input) == int:
#         return str(input)
#     if type(input) == str:
#         return int(input)
#     if type(input) == float:
#         return bool(input)
#     if type(input) == bool:
#         return 0
    

# print(type_casting(9))
# print(type_casting('989890'))
# print(type_casting(989.1))
# print(type_casting(True))

# print(type(int))



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# num1 = 369532456
# num2 = 32


# print(num1 / num2)



# print(6.6 * 6.6)
# 43.559999999999995
# print(6.6 * 6.6 * 6.6)
# 287.496
# print(0.1 + 0.2)
# 0.30000000000000004

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    

"""
True
True 
True
False
True
False
"""
