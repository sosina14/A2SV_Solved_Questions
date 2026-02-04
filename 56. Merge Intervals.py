class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x : x[0])
        arr = [intervals[0]]
        for i , j in intervals[1:]:
            x = arr[-1][1]
            if i <= x:
                arr[-1][1] = max(x,j)
            else:
                arr.append([i , j])
       
        return arr
