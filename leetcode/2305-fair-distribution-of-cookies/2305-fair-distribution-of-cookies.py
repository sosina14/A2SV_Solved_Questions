class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        arr = [0]*k
       
        def backtrack(i):
            nonlocal ans , arr
            if i == len(cookies):
                ans = min(ans , max(arr))
                return 
            if ans <= max(arr): return 
            
            for j in range(k):
                arr[j] += cookies[i]
                backtrack(i+1)
                arr[j] -= cookies[i]
                
        
        backtrack(0)
        return ans