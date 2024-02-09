with open("csv_files/csv/countydata.csv") as a_file:
    read_data = a_file.read()
    list_data = []

    split_data = read_data.split(",")
    list_data.append(split_data)
    print(list_data)

    # for row in list_data:
    #     print(row)

    