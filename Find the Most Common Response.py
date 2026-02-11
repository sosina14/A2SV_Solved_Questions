class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = { }

        for i in responses:
            for j in set(i):
                dic[j] = dic.get(j,0) + 1
                
        maxv = max(dic.values())
        dic2 = sorted(dic)
      
        for key in dic2:
            if dic[key] == maxv:
                return key
        
