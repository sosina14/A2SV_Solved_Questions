class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums.copy()
        arr.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            s = arr[i] + arr[j]
            if s == target:
                break
            elif s > target:
                j -= 1
            else:
                i += 1

        ans = []
        for index in range(len(nums)):
            if nums[index] == arr[i] or nums[index] == arr[j]:
                ans.append(index)
        return ans

        
            
