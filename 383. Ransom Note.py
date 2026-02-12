class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        for i in range(len(r)):
            if r[i] in m:
                m.remove(r[i])
            else:
                return False
        return True
