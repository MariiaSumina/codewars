def find_multiples(integer, limit):
    res = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            res.append(i)

    return res


assert find_multiples(5, 25) == [5, 10, 15, 20, 25]