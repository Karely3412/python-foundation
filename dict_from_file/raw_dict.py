empty_dict = {}


with open('dict_from_file/raw_dictionary.txt', 'rt') as a_file:
    read_data = a_file.read()

    split_code = read_data.split('\n')
    
    for i in split_code:
        sec_split_code = i.split(' ')
        empty_dict[sec_split_code[0]] = sec_split_code[1]

    print(empty_dict)
        

