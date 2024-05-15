def copy_file_content(source, destination):
    with open(source, 'r') as copy_file:
        with open(destination, 'w') as write_file:
            write_file.write(copy_file.read())

copy_file_content('C:/Users/roeig/CodingFolder/python/self/hangman-unit9/copy.txt','C:/Users/roeig/CodingFolder/python/self/hangman-unit9/paste.txt')

