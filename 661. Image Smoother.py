class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = copy.deepcopy(img)
        for r in range(len(img)):
            for c in range(len(img[0])):
                summ = img[r][c]
                count = 1
                if r-1 >= 0:
                    summ += img[r-1][c]
                    count += 1
                if r+1 < len(img):
                    summ += img[r+1][c]
                    count += 1
                if c-1 >= 0:
                    summ += img[r][c-1]
                    count += 1
                if c+1 < len(img[0]):
                    summ += img[r][c+1]
                    count += 1
                    
                if r-1 >= 0 and c-1 >= 0:
                    summ += img[r-1][c-1]
                    count += 1
                if r+1 < len(img) and c-1 >= 0:
                    summ += img[r+1][c-1]
                    count += 1
                if r-1 >= 0 and c+1 < len(img[0]):
                    summ += img[r-1][c+1]
                    count += 1
                if r+1 < len(img) and c+1 < len(img[0]):
                    summ += img[r+1][c+1]
                    count += 1
                average = summ// count
                result[r][c] = average
        return result
                
