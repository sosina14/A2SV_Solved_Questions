class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = {}
        result = []

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r+c not in dic:
                    dic[r+c] = []
                dic[r+c].append(mat[r][c])

        for key in sorted(dic.keys()):
            if key % 2 == 0:
                result.extend(dic[key][::-1])
            else:
                result.extend(dic[key])

        return result

       
                
