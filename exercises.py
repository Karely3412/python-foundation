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


"""
 Needed results:

 Name   City       State         Age
 ------ ---------- ------------- ----
 Jane   Boston     Massachusetts  24
 Fred   Portland   Oregon         31
 Betsy  Orlando    Florida        29
"""




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Excersie -> Inputs
"""
When adding inputs make you are casting data types. Make sure you're adding strings to strings or integers to integers.

"""

# def input_answers():
#     print('What ethinicity is your dad? ')
#     answer_1 = input()

#     print('What ethinicity is your mom? ')
#     answer_2 = input()
    

#     return f'You are {answer_1} & {answer_2}!'


# print(input_answers())


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
"""
Mathematics 

| Operation      | Operator | Example |
| -------------- | -------- | ------- |
| Addition       |    +     |  x + y  | <- basic adding 
| Subtraction    |    -     |  x - y  | <- basic subtracting 
| Multiplication |    *     |  x * y  | <- basic mutiplication 
| Division       |    /     |  x / y  | <- basic division with a remainder
| Modulus        |    %     |  x % y  | <- how many time can a number go evenly into an other
| Exponent       |    **    |  x ** y | <-  
| Floor Division |    //    |  x // y | <- this will give you back a whole number
| -------------- | -------- | ------- | 

** Order of Operations **

Parentheses
Exponents
Multiplication
Division
Addition
Subtraction

** scientific notation: Look this up **

"""
# 6.1 Integer Arithmetic exercises

# num1 = 369532456
# num2 = 32


# print(num1 / num2)

# 6.2 Floating Point Arithmetic exercises

# print(6.6 * 6.6)
# 43.559999999999995
# print(6.6 * 6.6 * 6.6)
# 287.496
# print(0.1 + 0.2)
# 0.30000000000000004

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    
# Boolean excercises
"""

** Boolean Order of Operations **
Parentheses (  )
NOT
AND
OR
left-to-right

"""
# 1. True -> True AND False OR True
# 2. True -> False OR True AND NOT False
# 3. True -> True OR (False OR True) AND False
# 4. False -> NOT(True OR False) AND NOT(True XOR True)
# 5. True -> True OR False AND True OR False
# 6. False -> True AND (False AND (True OR False))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    
# Examples
"""
new_number = 150

if new_number > 100:
    print(new_number, "too big")

- - - - - - - - - - - - - - - -
password = 'abc123'

if password == "abc123"
    print("Welcome")
else:
    print("Access Denied")

- - - - - - - - - - - - - - - -
if role == "standard":
    print("User Dasboard")
elif role == "admin":
    print("Admin Panel")
else:
    print("Not Authorized")

- - - - - - - - - - - - - - - -
user_name = "John"
email = "john_wick@gmail.com"
password = "I'mBack"

if (user_name == "John" or email == "john_wick@gmail.com") and password == "I'mBack":
    print("Welcome duder!")
else:
    print("No business on Continental grounds!")

"""

# score = float(input("Input score: "))

# if score >= 90:
#     print("Your score is: A")
# elif score >= 80:
#     print("Your score is: B")
# elif score >= 70:
#     print("Your score is: C")
# elif score >= 60:
#     print("Your score is: D")
# elif score < 50 and score > 0:
#     print("Your score is: F")
# else:
#     print("You've failed.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# for i in range(1,101):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# for i in range(101,1,-1):
#     print(i)


# name = ""
# for char in "Karely":
#     print(char)
#     name += char

# # print (name)

# name = []
# for char in "Karely":
#     print(char)
#     name += char

# print (name)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# x = 1
# while x < 6:
#     print(x)
#     x += 1


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(1, 11):
#     if i >= 2 and i <= 7:
#         print(i)



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# for x in [1,2,3]:
#     for y in ['a', 'b', 'c']:
#         print(y)
#     print(x)


# for x in [1,2,3]:
#     for y in ['a', 'b', 'c']:
#         print(y)
#         break
#     print(x)

# for x in range(1,5):
#     print(f'Loop#{x} starts here')
#     for y in range(10,20):
#         if y == 15:
#             print(y*2)
#             break
#         print(y)
#     print(f'Loop#{x} end here')


# for x in range(1,5):
#     print(f'Loop# {x} starts here')
#     for y in range(10,20):
#         if y == 15:
#             print('skip me')
#             continue
#         print(y)
#     print(f'Loop# {x} end here')


# for val in [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5]:
#     if type(val) == int:
#         continue
#     print(val)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Write a loop that iterates over a range of numbers from 1 to 20. After printing 15, use break to stop printing numbers.

# Write a loop that takes the input of "1111111devpipeline2222222" and uses continue and break to leave us with the output of "devpipeline".
    
# for i in range(1, 20):
#     if i == 15:
#         break
#     print(i)

# for val in ("1111111devpipeline2222222"):
#     if val == '1' or val == '2':
#         continue
#     print(val, end='')

# for val in ("1111111devpipeline2222222"):
#     if val.isalpha():
#       print(val, end='')


# name = ''
# for val in ("1111111devpipeline2222222"):
#     if val != '1' or val != '2':
#         name += val
#         continue
#     print(name)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
** Dictionaries **
Examples:

NBA Teams

Uta - Jazz
Boston - Celtics
Phoenix - Suns
Houston - Rockets
Miami - Heat

Altering values syntax -> mascots['UCLA'] = 'Bears'
Useful -> del mascots['utah']
Nested Dictionary in a list -> mascots[0] for the index of the list & ['Key_name'] to get the value of the by the key name. mascots[0]['key_name']

We could declare a empty dictionary then assign a key:value pairs to it with the syntax above
"""

# dict = {
#     'user' : 'super-admin',
#     'active' : True,
#     'meta_data' : {
#         'user_uuid' : '8984d3df98fg4',
#         'last_login' : '01/24/2024 03:42:00',
#         'account_type' : 'paid',
#     },
#     'contact_info': {
#         'f-name' : 'karely',
#         'l-name' : 'partida',
#         'phone' : '0000000000',
#         'address' : '1234 street'
#     },
#     'profile_pics' : [
#         1,
#         2,
#         3
#     ]
# }


# dict_2 = {
#     'user' : 'super-admin',
#     'active' : True,
#     'meta_data' : {
#         'user_uuid' : '8984d3df98fg4',
#         'last_login' : '01/24/2024 03:42:00',
#         'account_type' : 'paid',
#     },
#     'contact_info': {
#         'f-name' : 'karely',
#         'l-name' : 'partida',
#         'phone' : '0000000000',
#         'address' : '1234 street'
#     },
# }


# dict.update(dict_2)

# dict['meta_data']['account_type'] = 'free'  # <- this is replacing a nested value 

# if 'user' in dict:
#     print(dict['user'])

# print(len(dict))  
# print(dict.get('active', 'not found'))  
# print(dict.items())  
# print(dict.keys())  


# for key,value in dict.items():
#     print(key,value)


# for key in dict.keys():
#     print(key)


# for key in dict.values():
#     print(key)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Functions


def math(num1, num2):
    x = num1
    y = num2

    modu = x % y

    if modu == 0:
        return f' {x} is evenly divided {y}!'
    elif modu != 0:
        return f' {x} is not evenly divided {y}. Results {modu}'
    

print(math(20, 2))
        
    




