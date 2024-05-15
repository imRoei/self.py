def print_hangman(num_of_tries):
    if num_of_tries == 0:
        print('x-------x')
    elif num_of_tries == 1:
        print(''' 
x-------x
|
|
|
|
|
    ''')
    elif num_of_tries == 2:
        print('''
x-------x
|       |
|       0
|
|
|
      ''')

    elif num_of_tries == 3:
        print('''
x-------x
|       |
|       0
|       |
|
|
      ''')

    elif num_of_tries == 4:
        print('''
x-------x
|       |
|       0
|      /|\\
|
|
      ''')

    elif num_of_tries == 5:
        print('''
x-------x
|       |
|       0
|      /|\\
|      /
|
      ''')

    elif num_of_tries == 6:
        print('''
x-------x
|       |
|       0
|      /|\\
|      / \\
|
      ''')
        
num_of_tries = 6
print_hangman(num_of_tries)

      