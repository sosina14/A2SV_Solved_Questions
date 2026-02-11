class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arrs = sorted(s)
        arrt = sorted(t)

        i = j = 0
        steps = 0

        while i < len(s) and j < len(t):
            if arrs[i] == arrt[j]:
                i += 1
                j += 1
            elif arrs[i] > arrt[j]:
                steps += 1
                j += 1
            else: 
                i += 1

        steps += (len(t) - j)

        return steps
