def format_list(my_list):
    return my_list[:-1:2] + ['and '+my_list[-1]]

def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))

if __name__ == "__main__":
    main()
