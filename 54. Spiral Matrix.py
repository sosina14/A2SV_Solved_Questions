class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, top = 0, 0
        r, bot = len(matrix[0]), len(matrix)
        result = []
        
        while l < r and top < bot:
            for i in range(l, r):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bot):
                result.append(matrix[i][r - 1])
            r -= 1

            if not (top < bot and l < r):
                break

            for i in range(r - 1, l - 1, -1):
                result.append(matrix[bot - 1][i])
            bot -= 1

            for i in range(bot - 1, top - 1, -1):
                result.append(matrix[i][l])
            l += 1

        return result
