def even_or_odd(number):
    res = number % 2
    if res == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(2)) # even
print(even_or_odd(1)) # odd