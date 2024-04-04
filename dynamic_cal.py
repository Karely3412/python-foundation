"""
Algorithm -> Logic

Function
    - Month
    - Year
    - Print the calendar
    Funcs required:
        - func for comparing months
            - conditional (if statement)
            if !leap year or it's !30 days:
                print(31 day calendar)
            if !leap year or it's !31 days:
                print(30 day calendar)
            else:
                print(leap calendar)

        - func for comparing years

Formatting
    - f'string
    - 

    

* get_days_in_month(month, year) - Given a month number (1-12) and the year, this function will return the number of days in the month. The year is required just in case the year is a leap year and the month is February (2). The number of days in the month should return:
    a. 31 days - January (1), March (3), May (5), July (7), August (8), October (10), December (12)
        - 
    b. 28 days - February (2) unless a leap year, then 29
        -
    c. 30 days - April (4), June (6), September (9), November (11)
        -
            
"""



def is_leap_year(year):
    #true or false
    print("is_leap_year")


def days_in_a_month(month, year):
    months_31_days = [0, 2, 4, 6, 7, 9, 11]
    months_30_days = [3, 5, 8, 10]
    names_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


    # if not months_30_days and not months_31_days:
    #      return (False, 'Invalid month. Enter a digit between 1-12')


    if month-1 in months_31_days:
        print(names_of_months[month-1])
            
        # return 31
    elif month-1 in months_30_days:
        print(names_of_months[month-1])
        # return 30
    else:
        if is_leap_year(year):
            return 29
        return 28
    

days_in_a_month(3, 2012)

# def month_formatter():
    # """
    # compare 28 30 31 & isleap year
    # Need to figure out how to print(the name of the month)
    # """
#     print("formatter")
    


# while True:
#     month_question = input('Enter a month from (1-12): ')
#     year_question = input('Enter a year after 1970: ')
#     if 
#     if !is_leap_year || it's !30 days:
#         print(31 day calendar)
#     if !leap year or it's !31 days:
#         print(30 day calendar)
#     else:
#         print(leap calendar)






