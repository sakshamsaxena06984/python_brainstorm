"""
In python: String is Immutable [can't modify]
"""
if __name__ == '__main__':
    str = 'this is the string concept'
    print(str)
    print(str[0])
    # concatenation
    str_con=str+" -concatenation- "
    print(str_con)
    str_con=str_con*3
    print(str_con)
    print("for iteration")
    for ele in str:
        print(ele, end=' ')
    for i in range(0, len(str),1):
        print(str[i], end=' ')
    print()
    print(str.startswith("t",0))
