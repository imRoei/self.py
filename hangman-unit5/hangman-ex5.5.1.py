def is_valid_input(letter_guessed):
    if (len(letter_guessed)==1 
        and letter_guessed.isalpha()):
        return True
    return False
    
print(is_valid_input('B'))