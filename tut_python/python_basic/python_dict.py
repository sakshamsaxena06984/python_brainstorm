"""
It is mutable.....
"""

if __name__ == '__main__':
    # a={"one":1,"two":2,"three":3}
    # print(a)
    # print(type(a))
    # print(len(a))
    # b=a.copy()
    # print(b)
    # print(id(a))
    # print(id(b))

    # -- way of creating the dictionary
    # a1 = {"one": 1, "two": 2}
    # print(a1)
    # a2 = dict([("one", 1), ("two", 2)])
    # print(a2)
    # print(type(a2))
    # a3 = dict.fromkeys(["nsk", 1, 2, 3])
    # print(type(a3))
    # print(a3)
    # a3v1 = dict.fromkeys(["nsk", 1, 2, 3], 12)
    # print(type(a3v1))
    # print(a3v1)
    #

    a = {1: 2, 3: 4, "list": [1, 2, 3], "dict": {"one": 1}}
    print(a)
    print(type(a))

    print(a['list'])
    print(a.get(1))
    print(a.get('dict'))
    print(a.get(234))  # if key is not available, then return None
    print(a.get(234, 'not found'))  # if key is not available, then return 'not found'

    print(a.keys())
    print(a.values())

    # - counting the frequency of list element
    li = [1, 2, 3, 12, 2, 2, 4, 5]
    mp={}
    for ele in li:
        if ele in mp:
            mp[ele]=mp[ele]+1
        else:
            mp[ele]=1

    print(mp)
