def shift_left(my_list):
    my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2], my_list[0]
    return my_list

def main():
    my_list = [1, 2, 3]
    print(my_list)
    print(shift_left(my_list))

if __name__ == '__main__':
    main()