def who_is_missing(file_name):
    missing_numbers = list()
    with open(file_name, 'r') as f:
        numbers = sorted(map(int,f.read().split(',')))
        for num in range(numbers[0],numbers[-1]+1):
            if num not in numbers:
                missing_numbers.append(num)
    with open('C:/Users/roeig/CodingFolder/python/self/hangman-unit9/found.txt', 'w') as w:
        w.write((str(missing_numbers)))

# Example usage:
who_is_missing('C:/Users/roeig/CodingFolder/python/self/hangman-unit9/findMe.txt')
