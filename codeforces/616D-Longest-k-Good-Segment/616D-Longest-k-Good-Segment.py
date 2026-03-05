n , k = map(int, input().split())
arr = list(map(int, input().split()))

c = 0          
l = 0         
seen = {}      
best_l, best_r = 0, 0  

for i in range(len(arr)):
   
    seen[arr[i]] = seen.get(arr[i], 0) + 1
    if seen[arr[i]] == 1:
        c += 1

    while c > k:
        seen[arr[l]] -= 1
        if seen[arr[l]] == 0:
            c -= 1
        l += 1

    if i - l > best_r - best_l:
        best_l, best_r = l, i

print(best_l + 1, best_r + 1)