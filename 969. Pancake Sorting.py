class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []
        ans = []

        n = len(arr)
        while n > 1:
            x = arr.index(n) 
            arr[:x+1] = arr[:x+1][::-1]
            ans.append(x+1)
            arr[:n] = arr[:n][::-1]
            ans.append(n)
            n -= 1

        return ans
