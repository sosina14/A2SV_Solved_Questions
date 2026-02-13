    matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
