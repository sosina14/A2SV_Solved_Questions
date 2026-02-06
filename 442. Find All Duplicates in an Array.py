class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        arr = []
        for key,val in dic.items():
            if val > 1:
                arr.append(key)
        return arr
