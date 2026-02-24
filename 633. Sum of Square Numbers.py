class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = ceil(sqrt(c))
        while i <= j:
            x = i * i + j * j
            if x > c:
                j -= 1
            elif x < c:
                i += 1
            else:
                return True
        return False
            
        
