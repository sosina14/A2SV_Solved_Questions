class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                arr.append(matrix[r][c])
        arr.sort()
        # if k <= len(arr):
        return arr[k-1]
            
