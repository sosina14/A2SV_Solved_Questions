class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i

        end = dic[s[0]]
        ans = []
        size = 0

        for i in range(len(s)):
            size += 1
            end = max(dic[s[i]],end)
            
            if i == end:
                ans.append(size)
                size = 0

        return ans

           

        # 8,5,7   ---> 8+1 = 9
        # 14,15,11 ---> 15  15-8 = 7
        # 13,19,22,23,20 ---> 23  32-15 = 8
