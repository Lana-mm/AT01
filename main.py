def remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно.")
    return dividend % divisor