class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        summ = 0
        n = len(piles)//3
        piles.sort()
        if len(piles) == 3:
            return piles[1]
        else:
            i = len(piles)-2
            for _ in range(n):
                summ += piles[i]
                i -= 2
        return summ
            

                # maxv = max(piles)
                # piles.remove(maxv)
                # maxv = max(piles)
                # summ += maxv
                # piles.remove(maxv)
