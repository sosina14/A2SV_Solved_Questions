class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
    
        def checker(mid):
            c = 0
            for i in candies:
                c += i // mid
                
            return c >= k

        l = 1
        r = max(candies)

        while l <= r:
            mid = (l+r)//2

            if mid == 0: 
                l = 1
                break

            if checker(mid):
                l = mid+1
            else:
                r = mid-1

        return r


