

if __name__=='__main__':
    li=[1,2,3,4]
    print(f"before comprehension : {li}")
    li_1=[ele*2 for ele in li if ele!=2]
    print(f"after compreshension : {li_1}")

    dc ={1:11,2:22,3:33}
    print(f"before comprehension : {dc}")
    dc_1={ele:ele*2 for ele in dc}
    print(f"after comprehension : {dc_1}")

    dc_2={k:v+1 for k,v in dc.items()}
    print(dc_2)

    a=[1,2,3]
    b=[11,22,33]
    print([(x+y) for (x,y) in zip(a,b)])
    print([(x+y) for x in a for y in b])
