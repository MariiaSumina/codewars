def expression_matter(a, b, c):
    operator = [
        a * (b + c),
        a * b * c,
        a + b * c,
        (a + b) * c,
        a + b + c,

    ]

    return max(operator)