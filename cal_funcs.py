def is_leap_year(year):
    return (year % 4 == 0) and not year % 100 == 0 or year % 400 == 0


def print_cal_month(month, year, start_day_of_week, days_in_months):
    title = f"        {month} {year}\n"
    week_days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']

    print(f'{title}')

    for day in week_days:
        print(f'{day:>2}  ', end='')
    print('\n')
    
    count = 0

    for i in range(1 - start_day_of_week, days_in_months + 1):
        count += 1

        if i >= 1:
            print(f'{i:>2}  ', end='')
        if i < 1:
            print(f'{" "*4}', end='')

        if count % 7 == 0:
            print('\n')
    print()
            
    

print(is_leap_year(2024))
print_cal_month("February", "2024", 0, 29)



            