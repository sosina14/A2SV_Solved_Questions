class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        p = sorted(points, key=lambda x: x[1])

        i = 0
        count = 1
        end = p[0][1]

        while i < len(p):
            if p[i][0] > end:
                count += 1
                end = p[i][1]
            i += 1

        return count
