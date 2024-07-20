a = 2
print(a)
print(type(a))

b = "hello word"
print(b)
print(type(b))

"""
id() => basically use to print located memory
"""

c = 3
print(c)
print(id(c))
c = c + 1
print(c)
print(id(c))
c = 6
print(id(c))
c = 3
print(id(c))

d = 2 + 8j
print(d)
print(type(d))

e = 1000
print(e)
e = 10000000000000000000000000000000000000
print(e)

print(f"============ Arithmatic Operator =============")
a = 10
b = 3
print(f"sum is {a + b}")
print(f"minus is {a - b}")
print(f"mul is {a * b}")
print(f"divide is {a / b}")
print(f"divide_v1 is {a // b}")
print(f"exponential is {a ** b}")
print(f"remainder is {a % b}")
print(f"============ Input Taking =============")
# b = input()
# print(f"value of b is {b} and type is {type(b)}")
# b = int (b)
# print(f"value of b after type-casting is {b} and type is {type(b)}")
# c = input("enter the value of c")
# print(f"value of c is {c} and type is {type(c)}")


print(f"============ Boolean =============")
c = True
c1 = False

print(f"boolean type, value of c is {c} and value of c1 is {c1}")

print(f"============ if-else =============")

a = 22
if a > 2:
    print("a is greater than 2!")
elif a < 2:
    print("a is less than 2!")
else:
    print("a is 2")

a = True  # a=1
if a > 2 and a < 12:
    print("condition first")
elif a > 13 or a > 9:
    print(f"condition second  {a}")
else:
    print("boolean condition")

print(f"============ range in python =============")
"""
[_,_,_]
[including, excluding, steps]
"""

a = 10
for ele in range(4, a):
    print(f"value of ele is {ele}")

print("****************")
for ele in range(a, 0, -1):
    print(f"value of ele is {ele}")

print("****************")
for ele in range(a, -5, -3):
    print(f"value of ele is {ele}")
"""
negative-case
[big, small, step]
[10, 0, -2] 10|8|6|4|2
[small, big, step]
[0,10,-2]

"""

print("****************")
for ele in range(0, 10, -3):
    print(f"value of ele is {ele}")

print(f"============ pattern 1 =============")

flag = False
for r_n in range(4):
    pr_ele = r_n + 1
    ele_in_row = 2 * r_n + 1
    mid_ele = ele_in_row // 2 + 1
    sp_ele = 4 - mid_ele
    # printing space
    for ele in range(0, sp_ele):
        print(' ', end='')
    # printing increasing order
    for ele in range(0, mid_ele):
        print(pr_ele, end='')
        pr_ele = pr_ele + 1
    # printing decreasing order
    pr_ele = pr_ele - 2
    for ele in range(mid_ele, ele_in_row):
        print(pr_ele, end='')
        pr_ele = pr_ele - 1
    print()

print(f"============ pattern 1 v1 =============")

for i in range(1, 5):
    for s in range(4 - i):
        print(' ', end='')
    for j in range(i, i * 2, 1):
        print(j, end='')
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end='')
    print()

print(f"============ ASCI VALUE =============")
print(ord('A'))
print(ord('a'))
print(chr(65))
print(chr(64))
print(chr(999))

print(f"============ pattern 2 =============")

c = 65
for r in range(1, 5):
    for c in range(1, 5):
        print(chr(c + 64), end=' ')
    print()

print(f"============ pattern 3 =============")

n = 6
n1 = n // 2 + 1
n2 = n1 - 1
i = 0
while n1 - i >= 0:
    for s in range(0, n1 - i, 1):
        print(' ', end='')
    for e in range(0, 2 * i + 1, 1):
        print('*', end='')
    print()
    i = i + 1
i = i - 2
ele = 1
while i >= 0:
    for s in range(0, n2 - i + 1, 1):
        print(' ', end='')
    for e in range(0, 2 * i + 1, 1):
        print('*', end='')
    print()
    i = i - 1

print(f"============ Is prime code =============")


def isPrime(num: int) -> bool:
    for ele in range(2, num):
        if num % ele == 0:
            return False
    return True


print(isPrime(21))
print(isPrime(61))
