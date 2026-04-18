class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def checker(n):
            c = 1
            j = 0
            for i in range(len(position)):
                if position[i] - position[j] >= n:
                    c += 1
                    j = i
            return c >= m
        
        l = 1
        r = max(position)

        while l <= r:
            mid = (l+r)//2

            if checker(mid):
                l = mid+1
            else:
                r = mid-1
        return r
