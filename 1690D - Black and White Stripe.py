t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    s = input()
 
    l = 0
    minw = float("inf")
    b = 0
    w = 0
 
    for r in range(n):
    
        if s[r] == "B":
            b += 1
        else:
            w += 1
 
        while r-l+1 > k:
 
            if s[l] == "B":
                b -= 1
            else:
                w -= 1
            l += 1
        
        if r-l+1 ==k:
            minw = min(minw, w)
      
    
    print(minw)
