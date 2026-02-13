class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    count += 1   
                    j += 1 
                else:
                    j += 1
        return count 
        

           
