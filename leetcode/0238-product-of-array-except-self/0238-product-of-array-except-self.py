class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        x = 1
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                x = x * nums[i]

        for i in nums:
            if zero > 1:
                arr.append(0)

            elif zero == 1:
                if i == 0:
                    arr.append(x)
                else:
                    arr.append(0)

            else:
                arr.append(x//i)
   
        return arr