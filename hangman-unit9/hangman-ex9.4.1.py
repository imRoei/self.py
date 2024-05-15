def choose_word(file_path, index):
    file = open(file_path, 'r')
    words = list(dict.fromkeys(file.read().split()))
    print(words)
    if(index-1>len(words)):
        return (len(words), words[0])
    return (len(words), words[index-1])

print(choose_word("C:/Users/roeig/CodingFolder/python/self/hangman-unit9/words.txt", 15))