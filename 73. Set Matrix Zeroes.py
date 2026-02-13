rows, cols = set(), set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        # Set entire row to 0
        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        # Set entire column to 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
