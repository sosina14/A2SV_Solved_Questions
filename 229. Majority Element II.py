class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        arr = Counter(nums)
        result = []
        for key , val in arr.items():
            if val > n:
                result.append(key)
        return result

