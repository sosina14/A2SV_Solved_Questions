class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        dic = defaultdict(int)
        for i in bills:
            dic[i] += 1
            ch = i - 5
            if ch == 5:
                dic[5] -= 1
            elif ch == 15:
                if dic[10] > 0:
                    dic[10] -= 1
                else:
                    dic[5] -= 2
                dic[5] -= 1
            if dic[10] < 0 or dic[5] < 0:
                return False

        return True
