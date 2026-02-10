class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        for i in range(len(s)):
            dic[indices[i]] = s[i]

        res = ""
        for key in sorted(dic):   
            res += dic[key]
        return res
