n = int(input())
arr = list(map(int, input().split()))
 
arr.sort()
count = 0
i = 1
 
for num in arr:
    if num >= i:
        count += 1
        i += 1
        
print(count)
