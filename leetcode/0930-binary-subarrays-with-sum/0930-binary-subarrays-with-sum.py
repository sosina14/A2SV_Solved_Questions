class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atMost(k):
            if k < 0:
                return 0
            l,summ,ans = 0 , 0 ,0 
            for r in range(len(nums)):
                summ += nums[r]
                while summ > k:
                    summ -= nums[l]
                    l += 1
                ans += (r - l + 1)
            return ans
        
        return atMost(goal) - atMost(goal-1)