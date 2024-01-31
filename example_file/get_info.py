# a_file = open("example_file/stored_info.txt", "rt")

# file_lines = a_file.readlines()

# count = 0 

# for line in file_lines:
#     count += 1 
#     print(f"Line {count}: {line.strip()}")

# a_file.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - -
count = 0 

with open("example_file/stored_info.txt", "rt") as a_file:
    for line in a_file:
        count += 1
        print(f"Line {count}: {line.strip()}")


