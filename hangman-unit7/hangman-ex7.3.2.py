def show_hidden_word(secret_word, old_letters_guessed):
    word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word += ' '+letter+' '
        else:
            word += " _ "
    return word

def check_win(secret_word, old_letters_guessed):
    if show_hidden_word(secret_word, old_letters_guessed).replace(' ','') == secret_word:
        return True
    return False

secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))