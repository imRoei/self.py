def is_greater(my_list,n):
    greater_list = list()
    for num in my_list:
        if num > n:
            greater_list.append(num)
    return greater_list

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)