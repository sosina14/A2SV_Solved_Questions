#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code her
        # x = set(a)
        # for i in range(len(b)):
        #     if b[i] not in x:
        #         return False
        #     if b[i] in x:
        #         a.remove(b[i])
        # return True
        a.sort()
        b.sort()
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                return False
        
        return j == len(b)
    
        
        
    
