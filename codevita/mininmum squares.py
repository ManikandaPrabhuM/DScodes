for _ in range(int(input())):
    l,r=[],[]
    for i in range(int(input())):
        left,right=map(int,input().split())
        l.append(left)
        r.append(right)
    lmin,lmax=min(l),max(l)
    rmin,rmax=min(r),max(r)
    lside,rside=0,0
    if (lmin<0 and lmax<0) or (lmin>0 and lmax>0):
        lside=abs(lmax+lmin)
    else:
        lside=lmax-lmin
    if (rmin<0 and rmax<0) or (rmin>0 and rmax>0):
        rside=abs(rmax+rmin)
    else:
        rside=rmax-rmin
    print(max(rside,lside)**2)
