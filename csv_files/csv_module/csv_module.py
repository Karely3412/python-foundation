import csv

my_list = []


with open('csv_files/csv_module/states-agegroup-2020.csv', 'r') as read_data:
    new_data = csv.reader(read_data)

    for i in new_data:
        my_list.append(i)

    header = my_list[0][0]
    header_field = my_list[0][8]
    dash = '-'

    print (f'\n{header} {header_field}')
    print(f'{dash*len(header)} {dash*len(header_field)}\n\n{my_list[5][0]} {my_list[5][8]}\n')


    
    # if len(header_field):
    #     print(header_field)
    # for i in my_list[0]:
    #     print(i)
    
    # for i in my_list:
    #     if i[0] == 'Utah':
    #         print(i[0])



    




# with open('csv_files/csv_module/nation-agegroup-2020.csv', 'w') as data:
#     new_data = csv.writer(data)

#     new_data.writerows(rows)

    
    


