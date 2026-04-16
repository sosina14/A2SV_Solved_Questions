class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def merge(left, right):
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
            return arr

        def mergeSort(left, right):
            if left == right:
                return [nums[left]]

            mid = (left + right)// 2

            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)

            return merge(left_half, right_half)

        sortedlist = mergeSort(0, len(nums) - 1)

        sortedlist.reverse()

        return sortedlist[k-1]

        