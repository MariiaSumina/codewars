
def number(bus_stops):
    add = []
    sub = []
    for i in bus_stops:
        add.append(i[0])
        sub.append(i[1])
    return sum(add) - sum(sub)