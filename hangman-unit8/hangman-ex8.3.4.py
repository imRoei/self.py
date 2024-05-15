def inverse_dict(my_dict):
    new_dict = {}
    for node in my_dict.items():
        if node not in new_dict:
            new_dict[node[1]] = node[0]
        else:
            new_dict[node[1]]
    print(new_dict)

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
inverse_dict(course_dict)