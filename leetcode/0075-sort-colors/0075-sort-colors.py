class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort() this is not good girl plssssssssssss 
        j = len(nums)-1
        i = 0
        x = 0
        # count = 0
        while x <= j:
            if nums[x] == 2:
                nums[x], nums[j] = nums[j], nums[x]
                j -= 1
            elif nums[x] == 0:
                nums[x], nums[i] = nums[i], nums[x]
                i += 1
                x += 1
            else: 
                x += 1
