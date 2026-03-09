n , k , q = map(int, input().split())
 
MAX = 200000
array = [0]*(MAX+2)
 
for _ in range(n):
    l, r = map(int, input().split())
    array[l] += 1
    array[r+1] -= 1
 
for i in range(1, MAX+1):
    array[i] += array[i-1]
 
good = [0]*(MAX+1)
 
for i in range(1, MAX+1):
    if array[i] >= k:
        good[i] = 1
 
for i in range(1, MAX+1):
    good[i] += good[i-1]
 
for _ in range(q):
    l, r = map(int, input().split())
    print(good[r] - good[l-1])