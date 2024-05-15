guessed_letter = input("Guess a letter: ")


if (len(guessed_letter)==1):
    if (guessed_letter.isalpha()):
        print(guessed_letter)
    else:
        print("E2")
else:
    if(guessed_letter.isalpha()):
        print("E1")
    else:
        print("E3")