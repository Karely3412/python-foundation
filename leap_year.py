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


def leap_year(input):

    while True:

        if input < 1752:
            print('Please enter a year after 1752 AD.')
        elif input > 1752 and input % 4 == 0:
            print('is divisible by 4')


leap_year(1751)