def is_valid_input(letter_guessed):
    if (len(letter_guessed)==1 
        and letter_guessed.isalpha()):
        return True
    return False
    

def check_valid_input(letter_guessed, old_letters_guessed):
    return (is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed)


old_letters = ['a', 'b', 'c']
print(check_valid_input('C', old_letters)
)
print(check_valid_input('ep', old_letters)
)
print(check_valid_input('$', old_letters)
)
print(check_valid_input('s', old_letters)
)
