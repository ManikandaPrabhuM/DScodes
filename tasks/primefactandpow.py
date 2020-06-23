import math
n=int(input("Enter n: "))
cnt=0
while n%2==0:
    cnt+=1
    n=n//2
if cnt!=0:
    print(2,cnt)
for i in range(3,int(math.sqrt(n)),2):
    cnt=0
    while(n%i==0):
        cnt+=1
        n=n//i
    if cnt!=0:
        print(i,cnt)
    if n==1:
        break
if n!=1:
    print(n,1)
