from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))


freq = defaultdict(int)
l = 0
c = 0
unique = 0

for r in range(len(nums)):
    if freq[nums[r]] == 0:
        unique += 1
    freq[nums[r]] += 1

    while unique > k:
        freq[nums[l]] -= 1
        if freq[nums[l]] == 0:
            unique -= 1
        l += 1

    c += r - l + 1

print(c)
