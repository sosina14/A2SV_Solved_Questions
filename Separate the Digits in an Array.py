class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = "".join(str(i) for i in nums)
        res = list(map(int, result))
        return res
