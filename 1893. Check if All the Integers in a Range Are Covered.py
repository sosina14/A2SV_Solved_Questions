class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges,key = lambda x : x[0])
        
        i = 0
        for j in range(left , right+1):
            c = False
            while i < len(ranges):
                if ranges[i][0] <= j and j <= ranges[i][1] :
                    c = True
                    break
                i += 1

        if not c:   
                return False
        return True
        
