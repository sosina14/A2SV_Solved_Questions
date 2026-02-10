class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_t = list(t)
        arr_s = list(s)
        arr_t.sort()
        arr_s.sort()
        if arr_s == arr_t:
            return True
        else:
            return False
