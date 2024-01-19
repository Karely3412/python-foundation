"""

For this assignment, you will write a program that will prompt the user to enter a year (after 1752 AD)

The program will then print True or False

True, if the year is a leap year

False, if the year is NOT a leap year

A year IS a leap IF:

1) It is divisible by 4,

AND

2) It is NOT divisible by 100,

3) Unless it is also divisible by 400

"""


# def leap_year():

#     while True:
#         year_question = int(input('Please enter a year after 1752 AD: '))

#         if year_question < 1752:
#             print('Year is before 1752. Try again..')
#             continue

#         if year_question % 400 == 0:
#             print(f'{year_question} is leap year.. True 1')
#             break

#         elif year_question % 100 == 0:
#             print('Not a leap year. Try again.. False 1')

#         elif year_question % 4 == 0:
#             print(f'{year_question} is leap year.. True 2')
#             break
#         else:
#             print('Not a leap year. Try again.. False 2')

                


# leap_year()


def leap_year():

    while True:
        year_question = int(input('Please enter a year after 1752 AD: '))

        if year_question < 1752:
            print('Year is before 1752. Try again..')
            continue


        if (year_question % 4 == 0) and not year_question % 100 == 0 or year_question % 400 == 0:
            print(f'{year_question} is leap year.. True')
            break

        else:
            print('Not a leap year. Try again.. False')

                
"""

** Boolean Order of Operations **
Parentheses (  )
NOT
AND
OR
left-to-right

"""

leap_year()