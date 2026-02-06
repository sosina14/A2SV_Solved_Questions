class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numss = set(nums)
        for i in range(len(nums)):
            if i not in numss:
                return i
        return len(nums)



# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] != i:
#                 return i
#         return len(nums)
            
