def extend_list_x(list_x,list_y):
    list_z = list_x
    list_z[:0] = list_y
    return list_z

def main():
    list_x = [4,5,6]
    list_y = [1,2,3]
    list_x=extend_list_x(list_x,list_y)
    print(list_x)

if __name__ == '__main__':
    main()

