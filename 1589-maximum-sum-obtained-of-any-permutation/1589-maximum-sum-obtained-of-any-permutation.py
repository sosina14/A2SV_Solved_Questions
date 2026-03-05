class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0]*(len(nums)+1)

        for l , r in requests:
            arr[l] += 1
            arr[r+1] -= 1

        for i in range(1, len(arr)):
            arr[i] += arr[i-1]

        arr = arr[:-1]
        
        nums.sort(reverse = True)
        arr.sort(reverse = True)

        summ = 0
        for i in range(len(nums)):
            mul = nums[i] * arr[i]
            summ += mul
            
        return summ % (10**9 + 7)