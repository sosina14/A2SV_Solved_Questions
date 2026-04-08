class Solution:
    def findMin(self, nums: List[int]) -> int:
        def merge(left, right):
            ans = []
            i, j = 0, 0
            arr = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr.append(left[i])
                    i += 1
                elif left[i] == right[j]:
                    arr.append(left[i])
                    arr.append(right[j])
                    i += 1
                    j += 1
                else:
                    arr.append(right[j])
                    j += 1

            arr.extend(left[i:])
            arr.extend(right[j:])
            ans = arr
            return arr

        def mergeSort(left, right):
            if left == right:
                return [nums[left]]

            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)

            return merge(left_half, right_half)

        s = mergeSort(0, len(nums) - 1)
        return s[0]