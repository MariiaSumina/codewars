def last_man_standing(n):
    odd = []
    even = []
    for i in range (1, n+1):
        if i % 2 == 0:
            even.append(i)

        else:
            odd.append(i)
    print(even[-1])
    return

last_man_standing(9)