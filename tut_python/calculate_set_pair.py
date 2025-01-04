def print_pairs(arr, N):
    hash_set = set()
    for i in range(len(arr)):
        val = N - arr[i]
        if (val in hash_set):
            print(f"Pairs : {arr[i]} & {val}")
        hash_set.add(arr[i])

from datetime import datetime

if __name__ == '__main__':
    li = [1, 2, 40, 3, 9, 4]
    N = 3
    # print_pairs(li, N)
    a, b = 2, 3
    while b != 0:
        d = a & b
        a = a ^ b
        b = d << 1
    print(a)

    s='ab{4,8}'
    print(s)

    final_date = datetime.strptime("2021-08-01","%Y-%m-%d").strftime("%d:%m:%Y")
    print(final_date)
    print(type(final_date))
