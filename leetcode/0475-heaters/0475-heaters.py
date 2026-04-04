class Solution:
    def findRadius(self, ho: List[int], he: List[int]) -> int:
        ho.sort()
        he.sort()
        ans = float('-inf')
        for n in ho:
            idx = bisect_left(he, n)
            yene = float('inf')
            if idx < len(he):
                yene = min(yene, abs(he[idx] - n))
            if idx + 1 < len(he):
                yene = min(yene, abs(he[idx + 1] - n))
            if idx - 1 >= 0:
                yene = min(yene, abs(he[idx - 1] - n))
            ans = max(ans, yene)
        return ans