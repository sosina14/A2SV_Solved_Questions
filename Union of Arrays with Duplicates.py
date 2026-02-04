class Solution:    
    def findUnion(self, a, b):
        # code here
        arr = []
        for i in a:
            arr.append(i)
        for i in b:
            arr.append(i)
        arr.sort()
        x = set(arr)
        return x
        
                
