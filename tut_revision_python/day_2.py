'''
global vs local variable
'''

a = 12


def fun():
    a = 13
    print(f"local score : {a}")


print(f"global scope : {a}")
fun()
print(f"global scope : {a}")

print("********** use of global keyword ***************")


def fun1():
    global a
    a = 45
    print(f"inside the fun1 : {a}")


print(f"before function fun1 call : {a}")
fun1()
print(f"after function fun1 call : {a}")

print("********** list ***************")
'''
List is Heterogeneous
'''
li = []
li1 = [1, 2, "one", "two"]
print(li)
print(li1)
print(type(li))
print(f"access element in list via index  : {li1[1]}")
li2 = [1, 2, 3, 4, 5, "one", "two", "three", "four", "five"]
print(li2[1:6:2])
li2.insert(0, "ONE")
print(li2)
print(f"len of li2 is {len(li2)}")
li2.insert(11, "eleven")
print(li2)
print(f"len of li2 is {len(li2)}")
li2.insert(15, "dfk")
print(li2)
print(f"len of li2 is {len(li2)}")
print(f"before append length is {len(li2)}")
li2.append([11, 22, 33])
print(li2)
print(f"after append length is {len(li2)}")
li2.extend([44, 55, 66])
print(li2)
li2.pop()
print(li2)
li2.pop()
print(li2)
li2.pop()
print(li2)
li2.pop()
print(li2)
for ele in li2:
    print(ele)

print("------")
for ele in range(2, len(li2)):
    print(ele)
    print(li2[ele])
print("------ via [including:excluding:steps] ------")
for ele in li2[2:4]:
    print(f"value of ele is : {ele} and their corresponding value is : {li2[ele]}")
print(f"using negative index in list : {li2[-1]}")
# for ele in li2[-1:]:
#     print(li2[ele])
print("--|||||--")
print(li2)
print("--|||||--")
for ele in li2[-1 * len(li2):]:
    print(f"value of ele is : {ele}")

print("**************** input taking ways in the list *********************")
# lii = []
# n = int(input("enter the size of list"))
# for ele in range(n):
#     l = int(input("enter the integer"))
#     lii.append(l)
# print(lii)
# print("another way of taking input in python list")
# str = input("enter the element in the list")
# str_li = str.split(' ')
# print(f"type of str_li is {type(str_li)}")
# lii1=[]
# for ele in str_li:
#     lii1.append(int(ele))
#
# print(lii1)

# lii2 = [int(ele) for ele in input().split(' ')]
# print(lii2)

print("reversing of list")
lp = [1, 2, 3, 4]
print(lp)
print(lp[3::-1])  # reversing via slicing
for i in range(len(lp) // 2):
    lp[i], lp[len(lp) - i - 1] = lp[len(lp) - i - 1], lp[i]

print(lp)

print("way of selection sort in list :::::  ")
li = [1, 3, 7, 2, 5]
for i in range(len(li) - 1):
    min_index = i
    for ele in range(i + 1, len(li)):
        if li[min_index] > li[ele]:
            min_index = ele
    # will perform sorting
    li[i], li[min_index] = li[min_index], li[i]

print(li)

print("-- bubble sort")
li = [6, 4, 8, 3, 1, 2]
for i in range(0, len(li) - 1):
    for j in range(0, len(li) - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)
print("--- insertion sort")
li = [9, 8, 5, 6, 7, 1]
for i in range(1, len(li)):
    j = i - 1
    temp = li[i]
    while j >= 0 and li[j] > temp:
        li[j + 1] = li[j]  # it is insert step
        j = j - 1
    li[j + 1] = temp

print(li)

print("**************** string related operation *********************")
str = "hello"
if 'h' in str:
    print("YES")
else:
    print("NO")

if 'l' not in str:
    print("YES")
else:
    print("NO")

v = "samsung version 1.2"
print(v)
v = v.replace("1.2", "1.3")
print(v)
print(f"use if start with is : {v.startswith('s')}")

print("**************** 2D arrays *********************")

l_2d = [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]]
print(l_2d)
print(type(l_2d))
print(f"pic one element is : {l_2d[0][0]}")
print(f"row is : {len(l_2d)}")
print(f"col is : {len(l_2d[0])}")

print("**************** List Comprehension *********************")
li = [1, 2, 3, 4]
li_sqr = [ele ** 2 for ele in li]
print(li_sqr)
li_even = [ele for ele in li if ele % 2 == 0]
print(li_even)

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 3, 5, 6]
l_com = []
for x in l1:
    for y in l2:
        if x == y:
            l_com.append(x)

print(f"common element is {l_com}")

l_com1 = [x for x in l1 for y in l2 if x == y]
print(f"common element is {l_com1}")

li = [2, 3, 4, 41, 565]
li_ans = [x ** 2 if x % 2 == 0 else x for x in li]
print(li_ans)

li_2d = ["john", "jaxen", "hello-word"]
li_2d_com = [[s for s in ele] for ele in li_2d]
print(li_2d_com)

print("**************** taking input in 2d list *********************")
# str = input("enter number of row and col").split(' ')
# r, c = int(str[0]), int(str[1])
# li_2 = [[int(j) for j in input().split(' ')] for i in range(r)]
# print(li_2)
# print("printing the 2d list ---")
# for i in range(0,len(li_2)):
#     for j in range(len(li_2[i])):
#         print(li_2[i][j],end=' ')
#     print()
print('xy'.join('abcd'))
print("**************** tuples *********************")
a = (1, 2)
print(a)
print(type(a))
'''
follow index from 0 to len of tuple & negative
can apply splice
Immutable in nature
'''
b = (3, 4)
print(f"in use : {2 in a}")
print(f"len of tuple a : {len(a)}")
print(f"concatenation in tuple : {a + b}")
print(f"append in tuple: {a, b}")
print(f"repetitions in tuple: {a * 4}")
print(f"max ele is : {max(a)}")
print(f"min ele is : {min(a)}")
lo = [1, 2, 3, 4]
print(lo)
lot = tuple(lo)
print(lot)
print("**************** dictionary *********************")
x = {}
print(x)
print(type(x))
x = {"this": 1, "is": 2, "an": 3, "example": 4}
print(x)
print(f"len of dict : {len(x)}")
x_c = x.copy()
print(x_c)
x1 = dict([("this", 3), ("is", 2), ("an", 1), ("example", 5)])
print(x1)
x2 = dict.fromkeys(["ksmd",2,3,4,55])
print(x2)
x3 = dict.fromkeys(["sldm","Sds",3,4],11)
print(x3)
print(f"accessing the element in dict like : {x['this']}")
print(f"accessing the element in dict like : {x.get('this')}")
print(f"accessing the element in dict like : {x.get('thisss')}")
# print(f"accessing the element in dict like : {x['thisss']}") # not valid
print(f"accessing the element in dict like : {x.get('thisss','value not present')}")
print(f"keys in x : {x.keys()}")
print(f"values in x : {x.values()}")
print(f"items : {x.items()}")
for i in x:
    print(i,x.get(i))

x['this']='this_v1'
print(x)
x[1]="msmd"
print(x)
x['is']="msmd"
print(x)
x['dic']={"k":1,"l":2}
print(x)
x_c={"this":"this_v2","is":"is_2"}
x.update(x_c)
print(x)
x.pop('dic')
print(x)
del x['is']
print(x)
print("calculating the freq")
li=[1,2,2,3,3,44,2,1,1,1]
d_ans={}
for ele in li:
    if d_ans.get(ele)==None:
        d_ans[ele]=1
    else:
        d_ans[ele]=d_ans[ele]+1

print(d_ans)
d_ans1={}
for ele in li:
    if ele in d_ans1:
        d_ans1[ele]=d_ans1[ele]+1
    else:
        d_ans1[ele]=1
print(d_ans1)

d_ans2={}
for ele in li:
    d_ans2[ele]=d_ans2.get(ele,0)+1
print(d_ans2)

print("**************** set *********************")
s={1,23,3}
print(s)
print(type(s))
print(f"len of set s is {len(s)}")
s.add("sm")
print(s)
b={"sl,d","one",1}
s.update(b)
print(s)
s.remove(1)
print(s)
# print(s.discard(1))
# print(s.discard(3))
# print(s.remove(23))
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
se={}
print(se)
print(type(se))
se1=set()
print(se1)
print(type(se1))
