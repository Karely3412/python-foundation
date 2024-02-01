with open ('example_file/raw_data.txt', 'rt') as a_file:
    read_file_split = a_file.read().split('|')
    print(read_file_split)


with open('example_file/new_data.txt', 'w') as n_file:
    new_data = ', '.join(read_file_split)
    n_file.write(new_data)
    

