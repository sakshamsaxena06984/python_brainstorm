from tut_first.enforce_pos import enforce_positional_arguments


@enforce_positional_arguments(2)
def sum_num(a, b):
    return a + b


print(sum_num(2, 3))

try:
    result = sum_num(5)
except TypeError as e:
    print(e)  # Output: Function add expects 2 positional arguments, got 1.
