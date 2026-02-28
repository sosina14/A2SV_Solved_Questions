class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            u = 0
            l = 0
            maxl = 0
            freq = defaultdict(int)
            for r in range(len(nums)):
                if freq[nums[r]] == 0:
                    u += 1
                freq[nums[r]] += 1
                while u > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        u -= 1
                    l += 1
                maxl += (r-l+1)
            return maxl
        return atMost(k) - atMost(k-1)