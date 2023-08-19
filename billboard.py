def billboard(name, price=30):
    cost = []
    for i in name:
        cost.append(price)
    return sum(cost)