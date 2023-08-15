def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m

assert paperwork(10, 5) == 50