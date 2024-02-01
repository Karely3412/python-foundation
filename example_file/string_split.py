
split_code = []

with open('example_file/string_split.txt', 'rt') as a_file:
    my_file = a_file.read()
    split_code += my_file.split('. ')

    for i in split_code:
        print(i)


# with open('example_file/string_split.txt', 'rt')
