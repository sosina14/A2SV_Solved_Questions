from collections import Counter
n , m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0
fre1 = Counter(arr1)
fre2 = Counter(arr2)

for k in fre1:
    if k in fre2:
        mul = fre1[k] * fre2[k]
        count += mul

print(count)
