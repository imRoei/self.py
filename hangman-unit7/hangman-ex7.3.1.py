def show_hidden_word(secret_word, old_letters_guessed):
    word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word += ' '+letter+' '
        else:
            word += " _ "
    return word

secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))
