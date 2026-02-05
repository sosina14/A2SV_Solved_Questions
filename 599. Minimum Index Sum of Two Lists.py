class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {}
        dic2 = {}
        for i in range(len(list1)):
            dic1[list1[i]] = i
        for i in range(len(list2)):
            dic2[list2[i]] = i
    
        summ = 0
        arr = []
        for key,val in dic1.items():
            if key in dic2:
                summ = dic1[key]+dic2[key]
                arr.append(summ)
        minv = min(arr)
        ans = []
        for key,val in dic1.items():
            if key in dic2 and  dic1[key] + dic2[key] == minv:
                ans.append(key)
        return ans

     
