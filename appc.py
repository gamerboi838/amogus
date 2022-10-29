q=int(input())
for i in range(0,q):
    stuff=input().split()
    n=int(stuff[0])
    t=int(stuff[1])        
    tn=[]
    sn=[]
    tx=input().split()
    for i in range(0,n):
        tn.append(int(tx[i]))
    sx=input().split()
    for i in range(0,n):
        sn.append(int(sx[i]))
    ef=[]
    for i in range(0,n):
        ef.append(sn[i]/tn[i])
    max = float(0)
    maxs=0
    while t>0:
        for i in range(0,n):
            if(ef[i]>=float(max) and tn[i]<=t):
                max=ef[i]
                ind=i
        if(not ef):
            break
        n-=1
        s1=sn[ind]
        t1=tn[ind]
        maxs+=s1
        t-=t1
        tn.pop(ind)
        sn.pop(ind)
        ef.pop(ind)
        max=0
        ind=0
    print(maxs)
