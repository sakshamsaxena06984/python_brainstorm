
def helper(str):
    st=list()
    print(st)
    
    for i in range(len(str)):
        if str[i]=='(':
            st.append(str[i])
        elif str[i]==')':
            if len(st)==0:
                return False
            tp=st.pop()
            if str[i]==')' and tp=='(':
                continue
            else:
                return False
    if len(st)==0:
        return True
    else:
        return False



if __name__=='__main__':

    str="(()()()))"
    print(helper(str))



