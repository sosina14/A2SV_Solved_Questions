class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(com):
            if len(com) == len(nums) :
                ans.append(com[:])
                return
    
            for num in nums:
                if num not in com:
                    com.append(num)
                    backtrack(com)
                    com.pop()
            
        ans = []
        backtrack([])
        return ans