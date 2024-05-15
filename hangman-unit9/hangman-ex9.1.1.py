def are_files_equal(file1, file2):
    file1 = open(file1, 'r')
    file2 = open(file2, 'r')
    for line1,line2 in zip(file1,file2):
        if line1 != line2:
            return False
    return True

print(are_files_equal("C:/Users/roeig/CodingFolder/python/self/hangman-unit9/vacation.txt"
                , "C:/Users/roeig/CodingFolder/python/self/hangman-unit9/work.txt"))