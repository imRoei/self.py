def seven_boom(end_number):
    my_list = list()
    for i in range(0,end_number+1):
        if(i%7==0 or i%10==7):
            my_list.append("BOOM")
        else:
            my_list.append(i)

    return my_list

print(seven_boom(17))