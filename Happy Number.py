class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()
        while n != 1:
            if n in nset:
                return False
            nset.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n//= 10
            n = total
        return True
      
        
        
            
        
