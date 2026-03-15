t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for z in range(n-1, -1, -1):
        i = 0
        j = z - 1

        target = max(arr[-1], 2 * arr[z])
        need = target - arr[z]

        while i < j:
            if arr[i] + arr[j] > need:
                ans += j - i
                j -= 1
            else:
                i += 1

    print(ans)