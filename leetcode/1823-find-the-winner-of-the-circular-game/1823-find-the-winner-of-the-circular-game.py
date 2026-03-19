class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def win(n,k):
            if n == 1:
                return 0
            return (win(n - 1, k) + k) % n
        return win(n,k)+1