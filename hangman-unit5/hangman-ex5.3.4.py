def last_early(my_str):
    if(my_str[:-1].find(my_str[-1])!=-1):
        return True
    else:
        return False
    
print(last_early("best of luck"))