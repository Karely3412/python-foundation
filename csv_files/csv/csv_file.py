with open("csv_files/csv/countydata.csv") as a_file:
    list_data = []

    header = a_file.readline()
    split_data = header.strip().split(",")
    print(f'{split_data[0]:20} {split_data[1]:>8} {split_data[-1]:>8}')
    print('----------------- -------- -------- -------- ---------')

    for i in a_file:
        split_data = i.split(",")
        list_data.append((split_data[0], split_data[1], split_data[-1]))

    for x in list_data:
        print(f'{x[0]:17} {x[1]:>8} {x[-1]:>9}', end="")

    

    