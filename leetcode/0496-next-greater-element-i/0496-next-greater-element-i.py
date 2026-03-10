class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = len(nums2)-1
        stack = [nums2[x]]
        y = nums2[x]

        dic = {y:-1}
        for i in range(len(nums2)-2,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                dic[nums2[i]] = -1
            else:
                dic[nums2[i]] = stack[-1]

            stack.append(nums2[i])

    
        ans = []
        for i in nums1:
            ans.append(dic[i])
        return ans



        