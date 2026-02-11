class Solution:
    def findValidPair(self, s: str) -> str:
        dic = Counter(s)
        for i in range(len(s)-1):
            if int(s[i]) != int(s[i+1]) and int(s[i]) == dic[s[i]] and int(s[i+1]) == dic[s[i+1]]:
                return s[i:i+2]
        return ""
