class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        new_matrix = []
        for row in range(len(matrix[0])):
            arr = []
            for col in range(len(matrix)):
                arr.append(matrix[col][row])
            new_matrix.append(arr)
        return new_matrix
