def stockSpan(price, n):
    ans = []
    ans.append(1)
    st = []
    st.append(0)
    for i in range(1, len(price)):
        while len(st) != 0 and price[st[len(st) - 1]] < price[i]:
            # print(f"i : {i} and price[st[len(st) - 1] : {price[st[len(st) - 1]} ")
            st.pop()
        if len(st) == 0:
            ans.append(i + 1)
        if len(st) != 0:
            ans.append(i - st[len(st)-1])
        st.append(i)

    return ans

if __name__=='__main__':
    price=[]
    # price.append(70)
    # price.append(50)
    # // int []price={60 ,70 ,80 ,100 ,90 ,75 ,80 ,120};
    price.append(60);
    price.append(70);
    price.append(80);
    price.append(100);
    price.append(90);
    price.append(75);
    price.append(80);
    price.append(120);
    ans=stockSpan(price,2)
    for ele in ans:
        print(ele)
