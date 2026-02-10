class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        count = 1
        maxlen = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
            else:
                maxlen = max(maxlen , count)
                count = 1

        return max(maxlen,count)
               
