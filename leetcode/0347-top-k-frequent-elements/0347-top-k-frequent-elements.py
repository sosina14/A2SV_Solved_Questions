class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        mydic = sorted(dic.items(), key=lambda item: item[1], reverse=True)

        result = []
        c = 0
        for key,val in mydic:
            result.append(key)
            c += 1
            if c == k:
                return result


