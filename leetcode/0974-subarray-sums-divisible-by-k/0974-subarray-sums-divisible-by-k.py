class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            pref += num
            r = pref % k

            count += freq.get(r, 0)
            freq[r] = freq.get(r, 0) + 1

        return count
