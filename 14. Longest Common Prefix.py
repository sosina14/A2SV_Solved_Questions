class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        for i in strs:
            min_len = min(min_len, len(i))
        r = ""
        for i in range(min_len):
            found = True
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]:
                    found = False
                    break
            if found:
                r += strs[0][i]
            else:
                break
        return r
