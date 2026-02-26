t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = [arr[0]]

    i = 1
    while i < n-1:
        if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
            ans.append(arr[i])
        elif arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            ans.append(arr[i])
        i += 1

    ans.append(arr[n-1])

    print(len(ans))
    print(*ans)
