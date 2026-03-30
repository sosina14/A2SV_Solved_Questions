from collections import defaultdict
n = int(input())
arr = []
f = True
for _ in range(n-1):
    x = int(input())
    arr.append(x)

dic = defaultdict(list)
idx = 2
for i in range(len(arr)):
    dic[int(arr[i])].append(idx)
    idx += 1

for i in range(1, n):
    count = 0
    if len(dic[i]) != 0:
        for val in dic[i]:
            if len(dic[val]) == 0:
                count += 1

        if count < 3:
            f = False
            break

if f:
    print("Yes")
else:
    print("No")