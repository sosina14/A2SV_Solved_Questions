class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        flag = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                arr.append(matrix[r][c])
                if matrix[r][c] == target:
                    flag = True
            
        copy = arr[::]
        copy.sort()

        if copy == arr and flag:
            return True
        else:
            return False

