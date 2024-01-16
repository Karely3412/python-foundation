# print(f"""        September 2021    

#    S   M   T   W   T   F   S

#                1   2   3   4

#    5   6   7   8   9  10  11

#   12  13  14  15  16  17  18

#   19  20  21  22  23  24  25

#   26  27  28  29  30""")



def month_of_sept():
    print('S  M  T  W  T  F  S')


    for i in range(1,31):
        # print(i, end='')
        if i >= 1 and i <= 4:
            print(f'{i:>2}', end="")



month_of_sept()