"""
Tuple: It is immutable. [mean, can't modify]
"""


def func1():
    return 1, 2, 3, 4, 5


# - imp
def func(a, b, *c):
    print(f"value of a : {a} and type of a : {type(a)}")
    print(f"value of b : {b} and type of b : {type(b)}")
    print(f"value of c : {c} and type of c : {type(c)}")


if __name__ == '__main__':
    a = (1, 2)
    print(a)
    print(type(a))
    print(a[0])
    print(a[1])
    print(a[-1])
    print(a[-2])
    print(a[0:len(a)])
    a1 = tuple(reversed(a))
    print(a1)
    na = a * 3
    print(na)
    s_na = tuple(sorted(na))
    print(s_na)
    print(max(s_na))
    print(min(s_na))
    func(1, 2, 9, 2, 2, 2)
    k=func1()
    print(f"value of k : {k} and type of k : {type(k)}")
