class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
 
        dic1 = sorted(dic.items() , key = lambda x:x[1], reverse = True)
        
        result = ""
        
        for key , val in dic1:
            result += key*val
        
        return result
        
     
