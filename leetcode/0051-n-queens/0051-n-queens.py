class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset = set()
        negdig = set()
        posdig = set()

        res = []
        matrix= [["."] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                ans = ["".join(row) for row in matrix] 
                res.append(ans)
                return 

            for c in range(n):
                if c in colset or (r-c) in negdig or (r+c) in posdig:
                    continue
                colset.add(c)
                negdig.add(r-c)
                posdig.add(r+c)
                matrix[r][c] = "Q"

                backtracking(r+1)

                colset.remove(c)
                negdig.remove(r-c)
                posdig.remove(r+c)
                matrix[r][c] = "."
            

        backtracking(0)
        return res
