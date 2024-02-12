with open("csv_files/csv/countydata.csv") as a_file:
    list_data = []

    for i in a_file:
        split_data = i.split(",")
        joined_data = " ".join((split_data[0], split_data[1], split_data[-1]))
        list_data.append(joined_data)
    print(list_data)

    

    