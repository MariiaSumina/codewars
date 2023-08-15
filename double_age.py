def twice_as_old(dad, son):
    if dad == son * 2:
        return 0
    else:
        res = dad - son * 2
        if res < 0:
            return res * -1
        else:
            return res


assert twice_as_old(55, 30) == 5
