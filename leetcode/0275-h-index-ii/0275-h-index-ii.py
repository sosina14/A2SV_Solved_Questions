class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def checker(n):
            c = 0
            for i in citations:
                if i >= mid:
                    c+=1
                    if c == mid:
                        return True
            return False
        
        l = 1
        r = max(citations)

        while l<= r:
            mid = (l+r)//2
            if mid == 0:
                return 0
    
            if checker(mid):
                l = mid+1
            else:
                r = mid-1

        return r