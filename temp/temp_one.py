def perform_operation(a, b):
    if a + b == 3:
        return add(a, b)
    elif a + b < 3:
        return minus(a, b)
    elif a + b > 3:
        return multiply(a, b)
    else:
        raise ValueError("No valid operation for the given inputs.")

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b
