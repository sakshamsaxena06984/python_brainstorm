def helper(n):
    opt = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if n == 0:
        li = [""]
        return li

    sn = n // 10
    rn = n % 10
    ans=helper(sn)
    s_ans=opt[rn]
    out=[""]
    out*=len(ans)*len(s_ans)
    k=0
    for i in range(len(s_ans)):
        for j in range(len(ans)):
            out[k]=ans[j]+s_ans[i]
            k+=1
    return out




if __name__ == '__main__':
    n = int(input())
    ans=helper(n)
    print(ans)
