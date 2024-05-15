string = input("Please enter a string: ")
print(string[:int(len(string)/2)] + string[int(len(string)/2):].upper())