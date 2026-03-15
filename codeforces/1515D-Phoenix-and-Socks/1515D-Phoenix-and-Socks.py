from collections import Counter
t=int(input())

for _ in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))

    c1=Counter(arr[:l])
    c2=Counter(arr[l:])
    cost=0

    for c in list(c1.keys()):
        m=min(c1[c],c2[c])
        c1[c]-=m
        c2[c]-=m
        l-=m
        r-=m
    
    if l<r:
        c1,c2=c2,c1
        l,r=r,l
    
    diff=l-r

    for c in c1:
        while c1[c]>=2 and diff>0:
            c1[c]-=2
            diff-=2
            cost+=1
    
    cost+=diff//2
    rem=sum(c1.values())+sum(c2.values())
    cost+=rem//2
    print(cost)