class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c = haystack.count(needle)
        if c == 0:
            return -1
        else:
            return haystack.find(needle)
