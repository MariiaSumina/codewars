def points(games):
    ans = []
    for i in games:
        if i[0] > i[2]:
            ans.append(3)
        elif i[0] == i[2]:
            ans.append(1)
    return sum(ans)


assert points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']) == 30
