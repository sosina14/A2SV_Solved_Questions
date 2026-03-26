class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)
            
        backtrack(0)
        return ans
