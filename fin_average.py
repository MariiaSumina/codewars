def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0


assert find_average([1, 2, 3]) == 2
assert find_average([]) == 0