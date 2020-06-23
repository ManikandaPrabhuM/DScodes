arr=list(map(int,input().split()))
k=int(input())
cnt=0
for i in arr:
    if i%k!=0:
        cnt+=1
if cnt==0 and min(arr)!=k:
    print(1)
else:
    print(cnt)
