class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = 0
        for i in nums:
            if i%2 == 0:
                summ += i

        ans = []
        for i in range(len(queries)):
            val = queries[i][0]
            idx = queries[i][1]

            if nums[idx] % 2 == 0:
                summ -= nums[idx]
                nums[idx] += val
                if nums[idx] % 2 == 0:
                    summ += nums[idx]
                ans.append(summ)
            else:
                nums[idx] += val
                if nums[idx] % 2 == 0:
                    summ += nums[idx]
                ans.append(summ)
    
        return ans
