class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 ==0:
            return n
        else:
            return n*2
#or
#class Solution:
#   def smallestEvenMultiple(self, n: int) -> int:
#        return lcm(2,n)

