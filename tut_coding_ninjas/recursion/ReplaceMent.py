

def help(s, c1,c2):
    if len(s)==0:
        return ''
    c='';
    if(s[0]==c1):
        c=c2
    else:
        c=s[0]
    return c+help(s[1:],c1,c2)


if __name__=='__main__':
    s=input()
    c1,c2=[ele for ele in input().strip().split(' ')]
    print(help(s,c1,c2))
    k=1
    num1=2
    L=[None]*num1
    print(L)



