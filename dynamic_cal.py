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
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
        print('True')
        return True
    else:
        print('False')
        return False



def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3

    # print((year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7)
    return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7
     


def days_in_a_month(month, year):
    months_31_days = [0, 2, 4, 6, 7, 9, 11]
    months_30_days = [3, 5, 8, 10]
    names_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    my_return = []


    if month-1 in months_31_days:
        my_return.append(31)
        my_return.append(names_of_months[month-1])
        # print(my_return)
        return my_return
            
    elif month-1 in months_30_days:
        my_return.append(30)
        my_return.append(names_of_months[month-1])
        # print(my_return)
        return my_return
    else:
        if is_leap_year(year):
            my_return.append(29)
            my_return.append(names_of_months[month-1])
            # print('29')
            return my_return
        # print('28')
        my_return.append(28)
        my_return.append(names_of_months[month-1])
        return my_return
    



def month_formatter(month, year):
    my_return_month = days_in_a_month(month, year)
    my_return_day = day_of_week(year, month, 1)
    days_in_week = ['S', 'M', 'T', 'W', 'T', 'F', 'S']

    print(f'{my_return_month[1]:>14} {year}\n')

    for i in days_in_week:
        print(f'{i:>2}  ', end='')
    print('\n')

    count = 0
    for i in range(1 - my_return_day, my_return_month[0] + 1):
        count += 1
        
        if i >= 1:
            print(f'{i:>2}  ', end='')
        if i < 1:
            print(f'{" "*4}', end='')
        if count % 7 == 0:
            print('\n')



days_in_a_month(5, 2012)
month_formatter(5, 2012)






    


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






