class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(nums,idx,path):
            if len(path) >= 2:
                res.add(tuple(path))
            
            for i in range(idx,len(nums)):
                if not path or nums[i] >= path[-1]:
                    dfs(nums,i+1,path+[nums[i]])

        dfs(nums,0,[])
        return list(res)