def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            ans = i
    return(ans)