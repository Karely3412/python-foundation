def is_leap_year(year):
    print(' '*8, 'September 2021\n')
    print('   S   M   T   W   T   F   S\n')
    print(' '*12, end='')

    for i in range(1,31):
        if i == 5 or i == 12 or i == 19 or i == 26:
            print("\n")
        print(f'{i:>4}', end="")

    print()