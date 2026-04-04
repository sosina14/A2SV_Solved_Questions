class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(w):
            count = 1
            summ = 0
            for n in weights:
                if n > w: return False
                summ += n
                if summ > w:
                    count += 1
                    summ = n
            return count <= days
   
        l = 0
        r = sum(weights)
        while l <= r:
            mid = (l+r)//2
            if checker(mid):
                r = mid-1
            else:
                l = mid+1
        return l