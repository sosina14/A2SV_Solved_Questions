class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row , col = len(matrix) , len(matrix[0])
        self.prefixsum =[[0]* (col+1) for r in range(row+1)] 

        for r in range(row):
            pre = 0
            for c in range(col):
                pre += matrix[r][c] 
                above = self.prefixsum[r][c+1]
                self.prefixsum[r+1][c+1] = pre + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2 = row1+1, row2+1 , col1+1 , col2+1

        botRight = self.prefixsum[r2][c2]
        above = self.prefixsum[r1-1][c2]
        left = self.prefixsum[r2][c1-1]
        topleft = self.prefixsum[r1-1][c1-1]

        return botRight - above - left + topleft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)