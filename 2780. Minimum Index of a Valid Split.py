class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = Counter(nums)
        left = defaultdict(int)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            l = i + 1
            r = len(nums) - i - 1

            if 2 * left[nums[i]] > l and 2 * right[nums[i]] > r:
                return i

        return -1
