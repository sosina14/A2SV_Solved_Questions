class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        l = 0
        ans = 0
        
        for r in range(len(nums)):
            while maxq and maxq[-1] < nums[r]:
                maxq.pop()
            while minq and minq[-1] > nums[r]:
                minq.pop()

            minq.append(nums[r])
            maxq.append(nums[r])

            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[l]:
                      maxq.popleft()
                if minq[0] == nums[l]:
                      minq.popleft()
                l += 1
            ans  = max(ans, (r-l+1))
        return ans
        
        