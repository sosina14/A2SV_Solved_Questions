t = int(input())
for _ in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))

    m = int(input())
    mlist = list(map(int, input().split()))


    pre = 0
    maxx = 0
    for i in nlist:
        pre+=i
        maxx = max(maxx, pre)

    p = 0
    maxm = 0
    for j in mlist:
        p +=j
        maxm = max(maxm,p)

    result = maxx + maxm

    
    print(max(0,result))