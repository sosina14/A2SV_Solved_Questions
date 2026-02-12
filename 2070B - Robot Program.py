t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
 
    for i in range(n):
        if s[i] == "L":
            x -= 1
        else:
            x += 1
        k -= 1
        if x == 0:
            first_hit = i + 1
            break
    else:
        print(0)
        continue
 
    ans = 1
 
    for i in range(n):
        if s[i] == "L":
            x -= 1
        else:
            x += 1
 
        if x == 0:
            ans += k // (i + 1)
            break
 
    print(ans)
