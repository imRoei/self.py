def do_something(file_path):
    function = input("Enter a task:")
    file = open(file_path,'r')
    list_file = file.read()
    if (function == 'sort'):
        print(sorted(set(list_file.split())))
    elif (function == 'rev'):
        print(str(list_file)[::-1])
    elif (function == 'last'):
        last_line = input("Enter a number: ")
        print(str(list_file.split('\n'))[int(last_line):])
    file.close()


def main():
    path = "C:/Users/roeig/CodingFolder/python/self/hangman-unit9/sampleFile.txt"
    do_something(path)

if __name__ == "__main__":
    main()