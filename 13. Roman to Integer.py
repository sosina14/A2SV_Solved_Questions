class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {"I": 1, "V" :5, "X": 10, "L":50 , "C":100, "D":500, "M":1000}
        count = 0
        pre_val = 0
        for i in reversed(s):
            cur_val = my_dict[i]
            if cur_val < pre_val:
                count -= cur_val
            else:
                count += cur_val
            pre_val = cur_val
        return count

        
