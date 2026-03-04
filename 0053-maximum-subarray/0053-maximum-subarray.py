class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float("-inf")
        pre = 0
        for i in nums:
            pre += i
            if pre < i:
                pre = i
            total = max(total , pre)
        return total
