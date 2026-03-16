class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        steps = 0
        right = nums[-1]

        for i in range(len(nums)-2, -1,-1):
            left = nums[i]
            if left > right:
                p = math.ceil(left/right)
                steps += p -1
                right = left//p 
            else:
                right = left

        return steps