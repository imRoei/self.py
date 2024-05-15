def count_chars(my_str):
    dic = {}
    for c in my_str:
        if(c.isalpha()):
            if(c in dic):
                dic[c] += 1
            else:
                dic[c] = 1
    print(dic)

magic_str = "abra cadabra"
count_chars(magic_str)