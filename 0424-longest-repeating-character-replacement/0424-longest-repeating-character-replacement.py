class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0
        l = 0
        freq = defaultdict(int)
        nums = list(s)
        c = 0
        for r in range(len(s)):
            freq[nums[r]] += 1
            c = max(c, freq[nums[r]])
            while (r-l+1) - c > k:
                freq[nums[l]] -= 1
                l += 1

            maxl = max(maxl, r-l+1)

        return maxl