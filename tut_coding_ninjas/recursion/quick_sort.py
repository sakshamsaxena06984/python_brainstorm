from typing import List


def helper(arr: List[int], st: int, ed: int):
    c = 0
    ele_f = arr[st]
    for ele in range(st+1,ed+1):
        if arr[ele] < ele_f:
            c += 1
    pivot_index = c + st

    arr[st], arr[pivot_index] = arr[pivot_index], arr[st]
    i = st
    j = pivot_index+1

    while i <= pivot_index and j<= ed:
        if arr[i]<=arr[pivot_index]:
            i+=1
        elif arr[j]>arr[pivot_index]:
            j+=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1

    return pivot_index


def quickSort(arr: List[int], st: int, ed: int):
    if st<ed:
        p_index = helper(arr, st, ed)
        quickSort(arr, st, p_index)
        quickSort(arr, p_index + 1, ed)


    # p_index = helper(arr, st, ed)
    # quickSort(arr, st, p_index)
    # quickSort(arr, p_index + 1, ed)


if __name__ == '__main__':
    li = [4, 3, 2, 1, 5]
    quickSort(arr=li, st=0, ed=4)
    print(li)
