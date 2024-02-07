with open("csv_files/testing_csv_file/testing_csv_file.csv", 'r') as csvfile:
    results = []
    for line in csvfile:
        words = line.split(',')
        results.append((words[0], words[1:]))
    print(results)