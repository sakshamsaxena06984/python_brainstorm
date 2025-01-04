from sys import setrecursionlimit


def helper(arr, ele, index):
    if index < 0: return -1
    if arr[index] == ele:
        return index
    return helper(arr, ele, index - 1)


if __name__ == '__main__':
    setrecursionlimit(1000)
    n = int(input())
    arr = [int(ele) for ele in input().strip().split(' ')]
    ele = int(input())
    print(helper(arr, ele, len(arr) - 1))
