class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        count = 0
        dic = defaultdict(int)
        dic[0] = 1
        
        for i in range(len(nums)):
            summ += nums[i]
            x = summ - k
            if x in dic:
                count += dic[x]

            dic[summ] += 1
        
        return count 