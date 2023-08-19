def array(string):
    res = []
    string = string.split(",")
    if len(string) > 2:
        for i in string:
            res.append(i)
        ans = ' '.join(res[1:-1])
    else:
        ans = None
    return ans
