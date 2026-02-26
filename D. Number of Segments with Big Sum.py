
t , n = map(int, input().split())
arr = list(map(int, input().split()))

summ = 0
c = 0
left = 0

for r in range(t):
    
    summ += arr[r]

    while summ >= n:
        c += t-r
        summ -= arr[left]
        left += 1

print(c)

