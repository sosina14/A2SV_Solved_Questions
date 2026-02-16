class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            self.rotate(mat)
            if mat == target:
                return True
        return False
