class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        def mergesort(left, right):
            i , j = 0 , 0
            arr = []
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    arr.append(left[i])
                    i += 1
                elif left[i][0] == right[j][0]:
                    arr.append(left[i])
                    arr.append(right[j])
                    i += 1
                    j += 1
                else:
                    arr.append(right[j])
                    j += 1
            arr.extend(left[i:])
            arr.extend(right[j:])
            return arr

        def divide(left, right):
            if left == right:
                return [[nums[left],left]]

            mid = (left+right)//2

            l = divide(left , mid)
            r = divide(mid+1 , right)
      
            for val,idx in l:
                i = bisect.bisect_left(r,val , key=lambda x: x[0])
                ans[idx] += i

            return mergesort(l , r)

        divide(0, len(nums) - 1)
        return ans 

