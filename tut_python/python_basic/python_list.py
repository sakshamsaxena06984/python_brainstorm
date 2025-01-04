def func1(li):
    li[0] = 122
    print(f"inside the function : {li}")


def func(a):
    a = 122
    print(f"Inside the function : {a}")


def reversing(li):
    for i in range(len(li) // 2):
        li[i], li[len(li) - i - 1] = li[len(li) - 1 - i], li[i]


if __name__ == '__main__':
    # li = [1, 2, 3, "one", "tow", 3.3, 2 + 6j, True]
    # print(li)
    # for i in range(0,len(li)):
    #     print(li[i],end=' ')
    # print()
    #
    # for ele in li:
    #     print(ele, end=' ')
    # print()
    # print(li[2:len(li)])
    # print(li[0:len(li):2])
    # print(li[len(li):0:-1])
    # print(li[len(li)::-1])  # printing the reverse order of the list

    # -- taking input in the list
    # via normal
    # n = int(input("Enter the number of elements"))
    # li = []
    # for i in range(n):
    #     li.append(int(input()))
    # print(li)

    # via advance way
    # li = [int(ele) for ele in input().split(' ')]
    # print(li)

    # -- pass by value|list concept in python
    # a = 12
    # print(f"without calling the function : {a}")
    # func(a)
    # print(f"with calling the function : {a}")
    #
    # li = [1, 2]
    # print(f"without calling the function : {li}")
    # func1(li)
    # print(f"with calling the function : {li}")

    li = [1, 2, 3, 43, 5, 6]
    # print(li)
    # print(reversing(li))
    # print(li)

    # inbuilt function for reversing
    # print(li)
    # li.reverse()  # it will change the original value
    # print(li)
    #
    # li1 = list(reversed(li))
    # print(li1)
    # li1.sort()
    # print(li1)
    # li2 = sorted(li1)  # it will not modify the existing list
    # print(li2)
    # li2_rev = sorted(li2, reverse=True)
    # print(li2_rev)

    # 2d list

    # li=[[1,2,3],[4,5,6],[7,8,9]]
    # print(li)
    # for ele in li:
    #     print(ele)

    # -- way of generating the lis
    str="saksham"
    li=[ele for ele in str]
    print(str)
    print(li)

    li=['saksham','rohit','sankalp','rahul']
    li_2d=[[e for e in ele] for ele in li]
    print(li_2d)

    # -- taking input in the 2d list
    print("enter the number of row and col")
    nm=input().split()
    print(nm)
    print(nm[0])
    n=int(nm[0])
    m=int(nm[1])

    li=[[j for j in input().split(' ')] for i in range(n)]
    print(li)
