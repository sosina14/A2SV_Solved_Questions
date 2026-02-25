n , k = map(int, input().split())
arr = list(map(int, input().split()))

new = []
for i in range(n-1):
    x = arr[i+1] - arr[i]
    new.append(x)

merge = n - k
ans = 0
new.sort()

for i in range(merge):
    ans += new[i]

print(ans)
