class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summ = 0
        dic = defaultdict(lambda : inf)
        dic[0] = -1
      
        flag = False
        for i in range(len(nums)):
            summ += nums[i]

            c = math.ceil(summ / k)
            x = (c*k) - summ

            if x in dic:
                if (i - dic[x]) > 1:
                    flag = True
                    break

            dic[x] = min(i, dic[x])
    
        return flag