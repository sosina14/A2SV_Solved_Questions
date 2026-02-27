class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        left = 0
        maxl = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            maxl = max(maxl , right - left)
        return maxl
