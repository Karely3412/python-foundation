# print(f"""        September 2021    

#    S   M   T   W   T   F   S

#                1   2   3   4

#    5   6   7   8   9  10  11

#   12  13  14  15  16  17  18

#   19  20  21  22  23  24  25

#   26  27  28  29  30""")



def month_of_sept():
    print(' '*8, 'September 2021\n')
    print('   S   M   T   W   T   F   S\n')
    print(' '*12, end='')

    for i in range(1,31):
        if i == 5 or i == 12 or i == 19 or i == 26:
            print("\n")
        print(f'{i:>4}', end="")

    print()



month_of_sept()