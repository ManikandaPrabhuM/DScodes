from collections import Counter
t,n=map(int,input().split())
strings=[list(input()) for i in range(t)]
val=list(zip(*strings))
res=[]
for i in val:
    ob=Counter(sorted(list(i)))
    high_val=ob.most_common(1)
    res.append(high_val[0][0])
print("".join(res))
