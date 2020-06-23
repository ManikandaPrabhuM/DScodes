from itertools import permutations
import math
n=int(input())
arr=list(range(1,n+1))
res=0
val=list(permutations(arr,2))
print(val)
for i in val:
    if math.gcd(i[0],i[1])==i[1]:
        res+=1
res+=n
print(res)
