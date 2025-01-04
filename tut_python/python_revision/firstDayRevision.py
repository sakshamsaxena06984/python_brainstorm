import sys
import datetime

sys.setrecursionlimit(1000)
from datetime import date


class student:
    passing_mark = 33

    def __init__(self, name, age=22, percent=70):
        self.name = name
        self.age = age
        self.percent = percent

    @classmethod
    def from_birth_year(cls, name):
        return cls(name, date.today().year)


def funct(a, b):
    print(f" sum of {a} and {b} is :  {a + b}")
    return 11


def pattern(n):
    for i in range(1, n + 1, 1):
        for j in range(n - i):
            print(" ", end=" ")
        for j in range(i, 2 * i, 1):
            print(j, end=" ")
        for j in range(2 * i - 2, i - 1, -1):
            print(j, end=' ')
        print()


def selection_sort(li):
    length = len(li)
    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if (li[j] < li[index]):
                index = j
        li[i], li[index] = li[index], li[i]


def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def pass_by_value(n):
    print(f" value of n is : {n}")
    n = 23
    print(f" value of n is : {n}")


def selection_sort(li):
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = temp


class stu:
    __passing = 40
    college = "NIT JAMSHEDPUR"

    def __init__(self, name):
        self.name = name


def freq_count(li):
    mp = {}
    for ele in li:
        if ele in mp:
            mp[ele] = mp[ele] + 1
        else:
            mp[ele] = 1

    print(mp.values())
    print(mp.keys())
    print(mp.items())


if __name__ == '__main__':
    # li1 = [1, 2, 3, 4]
    # li2= li1
    # print(li1)
    # print(li2)
    # li1[0]=100
    # print(f"after the change ")
    # print(li2)
    # print(li1)
    # li2 = li1.copy()
    #
    # print(funct.__doc__)
    # print(funct(112,33).__doc__)

    # print(3/2)
    # print(3//2)

    # a = input()
    # print(type(a))
    # a = int(input())
    # print(f"type of the input is : {type(a)}")
    # c = 1 + 3j
    # print(f"complex type value is : {type(c)}")

    # n=int(input())
    # pattern(n)

    # li=[1,2,2.2,"skmd"]
    # print(li)
    # print(li[0])
    # print(li[-1])
    # print(li[1:2])
    # print(li[0:len(li)])
    # li.insert(0,100)
    # print(li)
    # li.insert(71,89)
    # print(li)
    # li.append(122)
    # print(li)
    # li.extend([234,4323])
    # print(li)
    # li.append([9,9,0])
    # print(li)

    # -> way of taking input in python list 1. line separated. & 2. Space Separated.
    # li = []
    # str = input()
    # for ele in str.split(' '):
    #     li.append(ele)
    #
    # print(li)
    # li = [ele for ele in input().split(' ')]
    # print(li)

    # li=[23,3,5]
    # print(li)
    # li[0]=100
    # print(li)

    # li = [1, 2, 3, 4]
    # print(li)
    # li.reverse()
    # print(li)
    # for i in range(len(li) // 2):
    #     li[i], li[len(li) - 1 - i] = li[len(li) - 1 - i], li[i]
    #
    # print(li)
    # print(li[len(li) - 1::-1])

    # print("====  performing selection sort  ======")
    # li = [5, 4, 2, 3, 0]
    # selection_sort(li)
    # print(li)
    # bubble_sort(li)
    # print(li)

    # n = 22
    # print(f"before call, n value is : f{n}")
    # pass_by_value(n)
    # print(f"after call, n value is : f{n}")

    # print("selection sort")
    # li = [4,3,2,1,9]
    # print(li)
    # selection_sort(li)
    # print(li)

    # print("list comprehension")
    # li = [1, 2, 3, 4, 5, 6]
    # li_ans = [ele ** 2 for ele in li]
    # print(li_ans)
    # li_if = [ele for ele in li if ele % 2 == 0]
    # print(li_if)
    # li1 = [1, 2, 3, 7, 8, 9]
    # li_both = [e1 for e1 in li1 for e2 in li if e1 == e2]
    # print(li_both)
    # str = "saksham"
    # li_str = [e for e in str]
    # print(li_str)
    # li_str_one = ['saksham', 'saxena']
    # li_2d = [ [s for s in ele]  for ele in li_str_one]
    # print(li_2d)
    # print(len(li_2d))
    # print(len(li_2d[0]))

    # li = [[1,2,3],[4,5,6],[7,8,9]]
    # for i in range(len(li)):
    #     for j in range(len(li[i])):
    #         print(li[i][j],end=' ')
    #     print()

    # t=(1,2,2,2)
    # print(type(t))
    # print(t)
    # for e in t:
    #     print(e)
    # print(1 in t)
    # print(23 in t)
    # print(len(t))
    # tl = list(t)
    # print(tl)
    # print("set functionality")
    # st={1,2,3}
    # print(st)
    # print(type(st))
    # st.add(2)
    # print(st)
    # print(2 in st)
    # print("dictionary")
    # dc={"one":1,"two":2,"three":3}
    # print(dc)
    # print(type(dc))
    # print(len(dc))
    # for e in dc:
    #     print(e,' ',dc[e])
    # print(dc.values())
    # print(dc.keys())
    # print(dc.items())
    # dc.pop('one')
    # print(dc)
    # del dc["two"]
    # print(dc)

    # mp = dict("one"=1,2="two")
    # print(mp)
    # my_dict = dict(key1="1", key2=2)
    # print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}
    # mp=dict([("msknd",1),("kmd",2)])
    # print(mp)
    # mp_comp = {ele:ele**2 for ele in range(1,4)}
    # print(mp_comp)
    #
    # li=["hello","word","hello","world1"]
    # freq_count(li)

    # print(f"current date is : {datetime.datetime.now()}")
    #
    # obj = student("rohan", 22)
    # sub_obj = obj.from_birth_year("ksd")
    # print(sub_obj)
    # print(type(sub_obj))
    # print(sub_obj.name)
    # print(sub_obj.age)

    obj = stu("msdk")
    print(obj.college)
    print(obj._stu__passing)
