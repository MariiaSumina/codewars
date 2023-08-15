def distinct(seq):
    mylist = list(dict.fromkeys(seq))
    return mylist


distinct([1, 2])