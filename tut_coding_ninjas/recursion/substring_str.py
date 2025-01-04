
def sub_string(s:str):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            print(s[i:j])

def sub_string_recur(s:str,st:int,en:int):
    if len(s)==st:
        return
    if en<=len(s):
        print(s[st:en])
        sub_string_recur(s,st,en+1)
    else:
        sub_string_recur(s,st+1,st+2)
if __name__=='__main__':
    str="abc"
    sub_string(str)
    print("===========")
    sub_string_recur(str,0,1)
