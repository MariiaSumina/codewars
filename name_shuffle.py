def name_shuffler(str_):
    first = str_.split(" ")
    res = first[1] + " " + first[0]
    return res


assert name_shuffler('john McClane') == 'McClane john'