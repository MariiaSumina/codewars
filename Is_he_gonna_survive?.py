def hero(bullets, dragons):
    ans = bullets//2
    if ans == dragons or ans > dragons:
        res = True
    else:
        res = False
    return res