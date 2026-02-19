n = int(input())
 
arr = list(map(int, input().split()))

x = n//2 
if n % 2 != 0:
    x += 1
    
arr.sort()
print(arr[x-1])
