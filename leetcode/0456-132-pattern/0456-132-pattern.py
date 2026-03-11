class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [nums[-1]]
        ii = []
        mn = float("inf")
        for num in nums:
            ii.append(mn)
            mn = min(mn, num)

        # print(ii)
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            while stack and stack[-1] <= ii[i]:
                stack.pop()
                
            if stack and num > ii[i] and num > stack[-1]:
                return True
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
            
        
        return False

