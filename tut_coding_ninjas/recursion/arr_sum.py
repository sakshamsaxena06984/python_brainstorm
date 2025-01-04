from sys import setrecursionlimit


def helper(li, index):
    if len(li) == index:
        return 0
    return li[index] + helper(li, index + 1)


def check_ele(li, index, ele):
    if len(li) == index:
        return False
    if li[index] == ele:
        return True
    return check_ele(li, index + 1, ele)

def isPalindrome(string: str) -> bool:
    n=len(str)
    print(f"value of n : {n} and str : {str}")
    if(n<=1):
        return True
    if(str[0]!=str[n-1]):
        return False
    return isPalindrome(str[1:-1])

if __name__ == '__main__':
    setrecursionlimit(11000)
    # n = int(input("Enter the size of list "))
    # arr = [int(ele) for ele in input().strip().split(' ')]
    # print(arr)
    # print(f"sum of array element in recursive way : {helper(arr, 0)}")
    # print(f"element is present/not-present in the array : {check_ele(arr,0,3)}")
    # print(2**2)
    # int s=1234
    # print(len(str))
    n=123
    print(n/10)
    print(n//10)
    print(n%10)
