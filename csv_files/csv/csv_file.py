with open("csv_files/csv/countydata.csv") as a_file:
    list_data = []

    header = a_file.readline()
    split_data = header.strip().split(",")
    print(f'{split_data[0]:17} {split_data[1]:>9} {split_data[-1]:>8} {"Growth":>8} {"Rate":>9}')
    print('----------------- -------- -------- -------- ---------')

    for i in a_file:
        split_data = i.strip().split(",")
        list_data.append((split_data[0], split_data[1], split_data[-1]))


    for x in list_data:
        growth_calc = int(x[-1]) - int(x[1])
        percentage = (growth_calc/int(x[1])) * 100
        formatted_rate = f'{percentage:.2f}'
        
  
        print(f'{x[0]:17} {x[1]:>8} {x[-1]:>8} {growth_calc:>8} {formatted_rate:>9} %')

    
    


    