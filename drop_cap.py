l2 = []
def drop_cap(words):
    words = words.lower()
    l = words.split(" ")
    for i in l:
        if len(i) > 2:
            i1 = i.capitalize()
            l2.append(i1)
        else:
            l2.append(i)
    x = " ".join(l2)
    return x

drop_cap("appLe of banana")