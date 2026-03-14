class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for c1, c2 in costs:
            x = c2 - c1
            diffs.append([x, c1, c2])

        res = 0
        diffs.sort()

        for i in range(len(diffs)):
            if i < len(costs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]

        return res