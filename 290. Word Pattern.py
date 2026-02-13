class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        dic2 = {}
        ss = s.split()

        if len(pattern) != len(ss):
            return False

        for i in range(len(ss)):
            if ss[i] in dic and dic[ss[i]] != pattern[i]:
                return False
            if pattern[i] in dic2 and dic2[pattern[i]] != ss[i]:
                return False

            dic[ss[i]] = pattern[i]
            dic2[pattern[i]] = ss[i]

        return True
