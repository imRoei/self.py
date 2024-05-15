# the function check if the player met the winning condition
def check_win(secret_word, old_letters_guessed):
    if show_hidden_word(secret_word, old_letters_guessed).replace(' ','') == secret_word:
        return True
    return False

# return a dictionary of the state of the hangman
def dict_print_hangman():
    hangman_dict = {}
    hangman_dict[0]='x-------x'
    hangman_dict[1] =''' 
x-------x
|
|
|
|
|
    '''
    hangman_dict[2] = '''
x-------x
|       |
|       0
|
|
|
      '''

    hangman_dict[3] = '''
x-------x
|       |
|       0
|       |
|
|
      '''
    hangman_dict[4]='''
x-------x
|       |
|       0
|      /|\\
|
|
      '''

    hangman_dict[5] = '''
x-------x
|       |
|       0
|      /|\\
|      /
|
      '''

    hangman_dict[6] = '''
x-------x
|       |
|       0
|      /|\\
|      / \\
|
      '''
    return hangman_dict

# return the state of the player by printing how close he is to guessing the word and the letters he guessed correctly
def show_hidden_word(secret_word, old_letters_guessed):
    word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word += ' '+letter+' '
        else:
            word += " _ "
    return word

# check if the word is legal
def is_valid_input(letter_guessed):
    if (len(letter_guessed)==1 
        and letter_guessed.isalpha()):
        return True
    return False

# check if the guess is correct
def check_valid_input(letter_guessed, old_letters_guessed):
    return (is_valid_input(letter_guessed) and (letter_guessed.lower() not in old_letters_guessed))

# the function receives a guess try and the last guesses and returns if the guess is correct or 
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if(check_valid_input(letter_guessed,old_letters_guessed)==False):
        print('X')
        print(' -> '.join(sorted(old_letters_guessed[:])))
        return False
    old_letters_guessed.append(letter_guessed)
    return True
    
# the function recives the path of file and an index and returns the word at the index 
def choose_word(file_path, index): 
    file = open(file_path, 'r')
    words = list(dict.fromkeys(file.read().split()))
    print(words)
    if(index-1>len(words)):
        return (len(words), words[0])
    return words[index-1]

def enter_screen(max_tries):
    print('''
     _    _                                    
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/
''')
    print(max_tries)

def main():
    MAX_TRIES = 6 # maximum amount of tries till failure
    enter_screen(MAX_TRIES) # print enter screen
    path = input("Enter path to the text file: ") #path to text file 
    number = int(input("Enter word index in text file:")) #index in file
    HANGMAN_PHOTOS = dict_print_hangman()
    num_of_tries = 0 
    secret_word = choose_word(path, number) #take the word out of the text file
    old_letters_guessed = [] 
    
    # game loop 
    while (num_of_tries<MAX_TRIES and not check_win(secret_word,old_letters_guessed)):
        #show the player state in the game
        print (HANGMAN_PHOTOS[num_of_tries])
        print(show_hidden_word(secret_word,old_letters_guessed))
        
        #get new letter
        letter_guessed = input("Enter a letter: ")
        
        #loop until find a letter that is legal
        while(try_update_letter_guessed(letter_guessed, old_letters_guessed)==False):
            letter_guessed = input("Enter a letter: ")
        #update num of tries if letter is wrong 
        if letter_guessed not in secret_word:
            num_of_tries+=1
    
    #player ran out of tries
    if(num_of_tries== MAX_TRIES):
        print(HANGMAN_PHOTOS[num_of_tries])
        print("Lose")
    #win case
    else:
        print(show_hidden_word(secret_word,old_letters_guessed))
        print("Win")


if __name__ == "__main__":
    main()

