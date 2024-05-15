def is_valid_input(letter_guessed):
    if (len(letter_guessed)==1 
        and letter_guessed.isalpha()):
        return True
    return False
    

def check_valid_input(letter_guessed, old_letters_guessed):
    return (is_valid_input(letter_guessed) and (letter_guessed.lower() not in old_letters_guessed))

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if(check_valid_input(letter_guessed,old_letters_guessed)==False):
        print('X')
        print(' -> '.join(sorted(old_letters_guessed[:])))
        return False
    old_letters_guessed.append(letter_guessed)
    return True
    

old_letters = ['a', 'p', 'c', 'f']
try_update_letter_guessed('A', old_letters)
try_update_letter_guessed('s', old_letters)
print(old_letters)
