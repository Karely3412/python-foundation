def is_leap_year(year):
    return (year % 4 == 0) and not year % 100 == 0 or year % 400 == 0


def print_cal_month(month, year):
    title = f"        {month} {year}\n"
    print(f'{title}')
    week_days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    



    for i in range(1,31):
        if i == 5 or i == 12 or i == 19 or i == 26:
            print("\n")
        print(f'{i:>4}', end="")

    print()



# is_leap_year()
print_cal_month('january', 2023)


# start_day_of_week, days_in_month