class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        mat = []
        for i in range(len(image)):
            mat.append(image[i][::-1])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    mat[r][c] = 1
                else:
                    mat[r][c] = 0
        return mat
