class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                dup = nums[i]
            else:
                seen[nums[i]] = True

        for i in range(1, len(nums)+1):
            if i not in seen:
                miss = i
                break

        return dup,miss