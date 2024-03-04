import csv

my_list = []


with open('csv_files/csv_module/states-agegroup-2020.csv', 'r') as read_data:
    new_data = csv.reader(read_data)

    for i in new_data:
        my_list.append(i)

    # print(my_list)




with open('csv_files/csv_module/csv_mod_data.csv', 'w') as data:
    new_data = csv.writer(data)
    csv_list = []
   
    for row in my_list:
        temp_row = [row[0], row[8], row[10], row[3], row[6]]
        csv_list.append(temp_row)
        
    new_data.writerows(csv_list)
            



        
with open('csv_files/csv_module/csv_mod_data.csv', 'r') as read_data:
    new_data = csv.reader(read_data)
    headers = next(new_data)

    dash = '-'

    print(f'\n{headers[0]:<13} {headers[1]:<45} {headers[2]:<50} {headers[3]:<45} {headers[4]}\n')
    # print(f'{dash*len(headers[0]):<13} {dash*len(headers[1]):<13} {dash*len(headers[2]):<13} {dash*len(headers[3]):<13} {dash*len(headers[4]):<13}')

    for row in new_data:
        print(f'{row[0]:<25} {row[1]:>30} {row[2]:>48} {row[3]:>45} {row[4]:>32}')



    
     


    


