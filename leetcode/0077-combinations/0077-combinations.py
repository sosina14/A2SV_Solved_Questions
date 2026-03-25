class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, com):
            if len(com) == k:
                ans.append(com[:])
                return
    
            for num in range(start,n+1):
                com.append(num)
                backtrack(num+1, com)
                com.pop()
            
        ans = []
        backtrack(1,[])
        return ans