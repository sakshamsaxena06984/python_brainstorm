def helper(n):
    return lambda a: a * n


if __name__ == '__main__':
    m = lambda x, y: x + y
    print(m(2, 3))

    val = helper(4)
    print(val(2))
