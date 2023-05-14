def quadrant(x, y):
    if x <= 0 and y <= 0:
        ans = 3
    elif x <= 0 and y >= 0:
        ans = 2
    elif x >= 0 and y >= 0:
        ans = 1
    elif x >= 0 and y <= 0:
        ans = 4
    return ans