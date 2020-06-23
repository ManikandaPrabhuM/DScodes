n=int(input("Enter n: "))
li=[]
while n%2==0:
    n=n//2
    li.append(2)
for i in range(3,n//2,2):
    while(n%i==0):
        n=n//i
        li.append(i)
if n!=1:
    li.append(n)
print(li)
k=int(input("Enter K: "))
if len(li)<k:
    print("Invalid position in factors available:",-1)
else:
    print("Kth position factor is:",li[k-1])
