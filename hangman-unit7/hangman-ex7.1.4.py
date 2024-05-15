def squard_numbers(start,stop):
    squard_list=list()
    while start <= stop:
        squard_list.append(start**2)
        start+=1
    return squard_list


def main():
    print(squard_numbers(4,8))

if __name__ == '__main__':
    main()
