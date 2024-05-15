def sequence_del(my_str):
    shorter_str = ''
    for tav in my_str:
        if(tav not in shorter_str):
            shorter_str+= tav
    print(shorter_str)

sequence_del("ppyyyyythhhhhooonnnnn")