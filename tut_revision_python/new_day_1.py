def isPrime(n) -> bool:
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

a=12
def func():
    global a
    a=13
    print(f"inside the function : {a}")
    print(f"inside the function id of a : {id(a)}")

if __name__ == '__main__':
    # print("Hello World")
    # a=1000101010101010
    # print(a)
    # print(id(a))
    #
    # n=True
    # print(not n)

    # - range concept
    # n=int(input())
    # for i in range(0,n,1):
    #     print(i, end=' ')
    # print()
    # for i in range(n,0,-1):
    #     print(i, end=' ')
    # print()

    # print(ord('A'))
    # print(ord('B'))
    # print(chr(66))
    # print(chr(67))
    # print(f"5 is prime or not {isPrime(5)}")
    # print(f"10 is prime or not {isPrime(10)}")
    # print(f"61 is prime or not {isPrime(61)}")

    print(f"before the function call, value of a : {a}")
    print(f"before the function call, id of a : {id(a)}")
    func()
    print(f"after the function call, value of a : {a}")
    print(f"after the function call, id of a : {id(a)}")


